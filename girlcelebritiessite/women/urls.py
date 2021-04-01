from django.urls import path
from .views import *

urlpatterns = [
    path('', WomenHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('add_page/', AddPage.as_view(), name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('registration/', RegistrationUser.as_view(), name='registration'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:category_slug>/', WomenCategory.as_view(), name='category')
]
