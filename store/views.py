from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import Product, Category, Cart, CartItem, Order, OrderItem
from .forms import CustomUserCreationForm

def product_list(request):
    products = Product.objects.filter(available=True)
    categories = Category.objects.all()
    
    # Search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        products = products.filter(
            name__icontains=search_query
        ) | products.filter(
            description__icontains=search_query
        ) | products.filter(
            category__name__icontains=search_query
        )
    
    return render(request, 'store/product_list.html', {
        'products': products,
        'categories': categories,
        'search_query': search_query
    })

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    return render(request, 'store/product_detail.html', {'product': product})

def category_products(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category, available=True)
    categories = Category.objects.all()
    return render(request, 'store/product_list.html', {
        'products': products,
        'categories': categories,
        'current_category': category
    })

@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'store/cart.html', {'cart': cart})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    messages.success(request, f'{product.name} added to cart!')
    return redirect('cart_detail')

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    cart_item.delete()
    messages.success(request, 'Item removed from cart!')
    return redirect('cart_detail')

@login_required
def update_cart(request, item_id):
    if request.method == 'POST':
        cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
        quantity = int(request.POST.get('quantity', 1))
        
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()
    
    return redirect('cart_detail')

@login_required
def checkout(request):
    from .models import Address
    cart = get_object_or_404(Cart, user=request.user)
    
    if request.method == 'POST':
        # Get address details
        full_name = request.POST.get('full_name')
        phone = request.POST.get('phone')
        address_line1 = request.POST.get('address_line1')
        address_line2 = request.POST.get('address_line2', '')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        save_address = request.POST.get('save_address')
        
        payment_method = request.POST.get('payment_method', 'cod')
        razorpay_payment_id = request.POST.get('razorpay_payment_id', '')
        
        # Create or get address
        address = None
        if save_address:
            address, created = Address.objects.get_or_create(
                user=request.user,
                full_name=full_name,
                phone=phone,
                address_line1=address_line1,
                address_line2=address_line2,
                city=city,
                state=state,
                pincode=pincode
            )
        
        # Format shipping address text
        shipping_address = f"{full_name}\n{phone}\n{address_line1}"
        if address_line2:
            shipping_address += f"\n{address_line2}"
        shipping_address += f"\n{city}, {state} - {pincode}"
        
        # Create order
        order = Order.objects.create(
            user=request.user,
            total_amount=cart.get_total(),
            shipping_address=shipping_address,
            address=address,
            payment_method=payment_method,
            payment_id=razorpay_payment_id,
            status='pending' if payment_method == 'cod' else 'processing'
        )
        
        # Create order items
        for item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )
        
        # Clear cart
        cart.items.all().delete()
        
        if payment_method == 'razorpay' and razorpay_payment_id:
            messages.success(request, f'Payment successful! Order #{order.id} placed.')
        else:
            messages.success(request, f'Order #{order.id} placed successfully! Pay on delivery.')
        
        return redirect('order_detail', order_id=order.id)
    
    # Prepare Razorpay data
    from django.conf import settings
    from .models import Address
    
    cart_total = cart.get_total()
    cart_total_paise = int(float(cart_total) * 100)  # Convert to paise
    saved_addresses = Address.objects.filter(user=request.user)
    
    context = {
        'cart': cart,
        'razorpay_key_id': settings.RAZORPAY_KEY_ID,
        'cart_total_paise': cart_total_paise,
        'saved_addresses': saved_addresses,
    }
    
    return render(request, 'store/checkout.html', context)

@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'store/order_detail.html', {'order': order})

@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'store/order_list.html', {'orders': orders})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('product_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'store/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {username}!')
            return redirect('product_list')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'store/login.html')

def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully!')
    return redirect('login')
