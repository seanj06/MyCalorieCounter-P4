from django.shortcuts import render


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