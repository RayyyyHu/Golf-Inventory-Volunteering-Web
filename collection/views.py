from django.shortcuts import render

# Create your views here.

from django.db.models import Q  # Import Q for complex lookups
from .models import GolfItem

def inventory_list(request):
    # Start with all items
    items = GolfItem.objects.all()
    
    # 1. Get the search query and category filter from the request
    query = request.GET.get('q')
    selected_category = request.GET.get('category')
    
    # 2. Apply filtering based on selected category
    # Only filter if the selected_category is not 'ALL' and not None
    if selected_category and selected_category != 'ALL':
        items = items.filter(category=selected_category)

    # 3. Apply filtering based on search query (description)
    if query:
        # Use icontains (case-insensitive contains) to search the description
        items = items.filter(Q(description__icontains=query))
    
    # Get all distinct categories for the dropdown menu
    # This ensures the dropdown options are always correct, even if you add more later.
    category_choices = GolfItem.CATEGORY_CHOICES 

    # 4. Pass the filtered data and context to the template
    context = {
        'items': items,
        'query': query,
        'selected_category': selected_category,
        'category_choices': category_choices,
    }
    return render(request, 'collection/inventory_list.html', context)   