from django.shortcuts import render

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
    # можете добавить свои рецепты ;)
}

def omlet(request):
    recipe = DATA['omlet']
    servings = int(request.GET.get('servings', 1))
    multiplied_recipe = {ingredient: round(quantity * servings, 2) for ingredient, quantity in recipe.items()}
    context =  {
        'recipe': multiplied_recipe
    }
    return render(request, 'calculator/index.html', context)

def pasta(request):
    recipe = DATA['pasta']
    servings = int(request.GET.get('servings', 1))
    multiplied_recipe = {ingredient: round(quantity * servings, 2) for ingredient, quantity in recipe.items()}
    context =  {
        'recipe': multiplied_recipe
    }
    return render(request, 'calculator/index.html', context)

def buter(request):
    recipe = DATA['buter']
    servings = int(request.GET.get('servings', 1))
    multiplied_recipe = {ingredient: round(quantity * servings, 2) for ingredient, quantity in recipe.items()}
    context =  {
        'recipe': multiplied_recipe
    }
    return render(request, 'calculator/index.html', context)

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
