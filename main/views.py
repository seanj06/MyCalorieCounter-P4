from django.shortcuts import render
from .models import Food, FoodCategory


def home(request):
    return render(request, 'index.html')


def food_search(request):
    import json
    import requests
    if request.method == 'POST':
        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get(api_url + query, headers={'X-Api-Key': 'tldMqAXTOtpoSr5T432O1g==K0Dxn4weDQfFnZfJ'})
        try:
            api = json.loads(api_request.content)
            print(api_request.content)
        except Exception as e:
            api = "something went wrong"
            print(e)    
        return render(request, 'food_search.html', {'api': api})
    else:
        return render(request, 'food_search.html', {'query': 'Enter a valid query'})


def food_list_view(request):
    '''
    It renders a page that displays all food items
    Food items are paginated: 4 per page
    '''
    foods = Food.objects.all()

    for food in foods:
        food.image = food.get_images.first()

    # Show 4 food items per page
    page = request.GET.get('page', 1)
    paginator = Paginator(foods, 4)
    try:
        pages = paginator.page(page)
    except PageNotAnInteger:
        pages = paginator.page(1)
    except EmptyPage:
        pages = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {
        'categories': FoodCategory.objects.all(),
        'foods': foods,
        'pages': pages,
        'title': 'Food List'
    })        