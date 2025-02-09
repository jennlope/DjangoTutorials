from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView,ProductIndexView,ProductShowView, ProductCreateView, SuccessView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('products/', ProductIndexView.as_view(), name='index'),
    path('products/create', ProductCreateView.as_view(), name='form'),
    path('products/<str:id>', ProductShowView.as_view(), name='show'),
    path('products/success/', SuccessView.as_view(), name='product_success'),
]
