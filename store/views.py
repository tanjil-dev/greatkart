from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from category.models import Category, SubCategory
from carts.models import CartItem
from carts.views import _cart_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from store.models import ReviewRating, ProductGallery
from .forms import ReviewForm
from django.contrib import messages
from orders.models import OrderProduct

# Create your views here.

def store(request, category_slug=None, subcategory_slug=None):
    products = Product.objects.filter(is_available=True)
    category = None
    subcategories = None
    selected_subcategory = None

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
        subcategories = SubCategory.objects.filter(category=category)

        if subcategory_slug:
            selected_subcategory = get_object_or_404(SubCategory, slug=subcategory_slug)
            products = products.filter(subcategory=selected_subcategory)

    categories = Category.objects.all()

    paginator = Paginator(products, 6)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)

    context = {
        'products': paged_products,
        'categories': categories,
        'category': category,
        'subcategories': subcategories,
        'selected_subcategory': selected_subcategory
    }

    return render(request, 'store/store.html', context)

def subcategory_view(request, subcategory_slug):
    subcategory = get_object_or_404(SubCategory, slug=subcategory_slug)
    products = Product.objects.filter(subcategory=subcategory)
    categories = Category.objects.all()

    context = {
        'subcategory': subcategory,
        'products': products,
        'categories': categories,
    }
    return render(request, 'store/store.html', context)

def product_detail(request, subcategory_slug, product_slug, category_slug=None):
    try:
        subcategory = get_object_or_404(SubCategory, slug=subcategory_slug)
        product = get_object_or_404(Product, subcategory=subcategory, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=product).exists()
    except Exception as e:
        raise e

    if request.user.is_authenticated:
        try:
            orderproduct = OrderProduct.objects.filter(user=request.user, product_id=product.id).exists()
        except OrderProduct.DoesNotExist:
            orderproduct = None
    else:
        orderproduct = None

    products = Product.objects.filter(is_available=True)
    category = None
    subcategories = None
    selected_subcategory = None

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
        subcategories = SubCategory.objects.filter(category=category)

        if subcategory_slug:
            selected_subcategory = get_object_or_404(SubCategory, slug=subcategory_slug)
            products = products.filter(subcategory=selected_subcategory)

    categories = Category.objects.all()

    reviews = ReviewRating.objects.filter(product_id=product.id, status=True)
    product_gallery = ProductGallery.objects.filter(product_id=product.id)

    context = {
        'product': product,
        'in_cart': in_cart,
        'orderproduct': orderproduct,
        'reviews': reviews,
        'product_gallery': product_gallery,
        'products': products,
        'categories': categories,
        'category': category,
        'subcategories': subcategories,
        'selected_subcategory': selected_subcategory
    }

    return render(request, 'store/product_detail.html', context)

def search(request):
    keyword = request.GET.get('keyword', '')
    products = Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
    product_count = products.count()

    context = {
        'products': products,
        'product_count': product_count,
    }

    return render(request, 'store/store.html', context)

def submit_review(request,product_id): 
    print(f"Received product_id: {product_id}")
    url = request.META.get('HTTP_REFERER')
    print(f"Referer URL: {url}")
    if request.method == 'POST':
        print(f"POST data: {request.POST}")
         
        try:
            
            reviews = ReviewRating.objects.get(user__id=request.user.id,product__id=product_id)
            form    = ReviewForm(request.POST,instance=reviews)
            form.save()
            messages.success(request,'Thank you! Your review hass been updated.')
            return redirect(url)
        
        except ReviewRating.DoesNotExist:
            
            form = ReviewForm(request.POST)
            if form.is_valid():
                data =  ReviewRating()
                data.subject    = form.cleaned_data['subject']
                data.rating     = form.cleaned_data['rating']
                data.review     = form.cleaned_data['review']
                data.ip         = request.META.get('REMOTE_ADDR')
                data.product_id = product_id
                data.user_id    = request.user.id
                data.save()
                messages.success(request,'Thank you! Your review hass been Submitted.')
            else:
                print(form.errors)
            return redirect(url)
            
