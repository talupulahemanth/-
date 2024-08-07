from django.shortcuts import render
from django.db.models import Q
from .models import MenuItem

def menu_view(request):
    allergen_query = request.GET.get('allergens', '')
    search_query = request.GET.get('search', '')
    order_by = request.GET.get('order_by', 'dish_name')  # Default ordering by dish_name

    # Building the query
    query = Q()
    if allergen_query:
        allergens = allergen_query.split(',')
        for allergen in allergens:
            query &= ~Q(allergens__icontains=allergen)
    if search_query:
        query &= Q(dish_name__icontains=search_query) | Q(description__icontains=search_query)

    # Fetching menu items based on the query and ordering
    menu_items = MenuItem.objects.filter(query).order_by(order_by)

    # Fetching distinct categories for categorization functionality (if applicable)
    categories = MenuItem.objects.values_list('category', flat=True).distinct()

    # Additional context for template enhancements
    context = {
        'menu_items': menu_items,
        'allergens': allergen_query,
        'search_query': search_query,
        'order_by': order_by,
        'categories': categories,
    }
    return render(request, 'menu.html', context)

# The rest of your views remain the same.


def home_view(request):
    # You might want to add some context or logic here if needed
    return render(request, 'home.html')

def chatbot_view(request):
    # This is the new view for the chatbot
    # You can add context or logic here if needed
    return render(request, 'savoylifebot/chatbot.html')
