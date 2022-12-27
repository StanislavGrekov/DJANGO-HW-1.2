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
    servings = int(request.GET.get('servings', 1))
    dict_omlet = {}
    for key, values in DATA.items():
        if key == 'omlet':
            for key, values in values.items():
                dict_omlet[key] = round(values*servings, 1)

    template_name = 'calculator/index.html'
    context = {
        'name_dish': f'Рецепт омлета. Количество персон - {servings}.',
        'recipe': dict_omlet
    }
    return render(request, template_name, context)


def pasta(request):
    servings = int(request.GET.get('servings', 1))
    dict_pasta = {}
    for key, values in DATA.items():
        if key == 'pasta':
            for key, values in values.items():
                dict_pasta[key] = round(values*servings, 1)

    template_name = 'calculator/index.html'
    context = {
        'name_dish': f'Рецепт пасты. Количество персон - {servings}.',
        'recipe': dict_pasta
    }
    return render(request, template_name, context)


def buter(request):
    servings = int(request.GET.get('servings', 1))
    dict_buter = {}
    for key, values in DATA.items():
        if key == 'buter':
            for key, values in values.items():
                dict_buter[key] = round(values*servings, 1)

    template_name = 'calculator/index.html'
    context = {
        'name_dish': f'Рецепт бутера. Количество персон - {servings}.',
        'recipe': dict_buter
    }
    return render(request, template_name, context)