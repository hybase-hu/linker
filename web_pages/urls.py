from django.urls import path

from web_pages.views import home, create_web_page, save_request, show_request, remove_web_page, remove_request

urlpatterns = [
    path('', home, name="home"),
    path('create_web_page', create_web_page, name="create_web_page"),
    path('link/<str:uid>', save_request, name='save_request'),
    path('show/<str:id>', show_request, name='show_request'),
    path('remove/<str:pk>', remove_web_page, name='remove_web_page'),
    path('remove/request/<int:pk>', remove_request, name='remove_request')
]
