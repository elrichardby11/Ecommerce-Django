from .models import Category

def global_category(request):
    menu_links = Category.objects.all()
    return dict(menu_links=menu_links)