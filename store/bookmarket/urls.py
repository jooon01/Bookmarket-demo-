from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='main'),
    path('book/<int:pk>', views.book, name='book'),
    path('category/<str:foo>', views.category, name="category"),
]





    # path('about/', views.about, name = 'about'),
    # path('login/', views.login, name='login'),
    # path('logout/', views.logout, name = 'logout'),
