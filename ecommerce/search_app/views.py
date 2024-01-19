from django.shortcuts import render
from ecommerceapp.models import Product,Category
from django.db.models import Q

# Create your views here.

def SearchResult(request):
    products = None
    query = None

    try:
        if 'q' in request.GET:
            query = request.GET.get('q')
            products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    except Exception as e:
        # Handle the exception (e.g., log it or render an error page)
        print(f"An error occurred: {e}")
        products = None  # Set products to None to indicate an error

    return render(request, 'search.html', {'query': query, 'products': products})