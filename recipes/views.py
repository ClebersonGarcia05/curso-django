from django.shortcuts import get_list_or_404, get_object_or_404, render

from recipes.models import Recipe


def home(request):
    recipes = Recipe.objects.filter(
        is_published=True
    ).order_by('id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })


def category(request, category_id):
    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id,
            is_published=True,
        ).order_by('id'))

    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f'Category {recipes[0].category.name} | Recipes'
    })


def recipes(request, id):
    recipe = get_object_or_404(
        Recipe,
        pk=id,
        is_published=True,
    )

    return render(request, 'recipes/pages/recipe-detail.html', context={
        'recipe': recipe,
        'is_datail_page': True,
    })
