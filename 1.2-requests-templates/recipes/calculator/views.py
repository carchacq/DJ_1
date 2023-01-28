from django.shortcuts import render
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}
dict = {'omlet': 'омлет', 'pasta': 'паста', 'buter': 'бутер'}
def home(request):
    return HttpResponse('Выберите: омлет (omlet), паста (pasta), бутеры (buter)')
def recipe_book(request, get_recipe):
    servings = int(request.GET.get('servings'))
    recipe = DATA[get_recipe]
    for ingredient, amount in recipe.items():
        recipe[ingredient] = amount * servings
    context = {
        'recipe': recipe,
        'recipe_rus': dict[get_recipe]
    }

    return render(request, 'calculator/index.html', context)

