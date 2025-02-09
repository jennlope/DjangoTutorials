from django import forms
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.views import View
# Create your views here.

"""def homePageView(request):
    return HttpResponse('Hello World!')"""
    
class HomePageView(TemplateView):
    template_name = 'pages/home.html'

template_name="pages/products/product_success.html"
    
class AboutPageView(TemplateView):
    template_name = 'pages/about.html'
    
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs) 
        context.update({ 
            "title": "About us - Online Store", 
            "subtitle": "About us", 
            "description": "This is an about page ...", 
            "author": "Developed by: Jennifer", 
        }) 
 
        return context

class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'
    
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs) 
        context.update({ 
            "title": "Our contact - Online Store", 
            "subtitle": "Our contact", 
            "description": "email: Onlina@gmail.com/n address: Cra 57 #65-2/n Phone number:+57 310 000 0000", 
            "author": "Developed by: Jennifer", 
        }) 
 
        return context

class Product: 
    products = [ 
        {"id":"1", "name":"TV", "description":"Best TV"}, 
        {"id":"2", "name":"iPhone", "description":"Best iPhone"}, 
        {"id":"3", "name":"Chromecast", "description":"Best Chromecast"}, 
        {"id":"4", "name":"Glasses", "description":"Best Glasses"} 
    ] 
 
class ProductIndexView(View): 
    template_name = 'pages/products/index.html' 
 
    def get(self, request): 
        viewData = {} 
        viewData["title"] = "Products - Online Store" 
        viewData["subtitle"] =  "List of products" 
        viewData["products"] = Product.products 
 
        return render(request, self.template_name, viewData) 
 
class ProductShowView(View): 
    template_name = 'pages/products/show.html' 
 
 
    def get(self, request, id): 
        viewData = {} 
        try:
            product = Product.products[int(id)-1] 
        except IndexError:
            return HttpResponseRedirect(reverse('home'))
        viewData["title"] = product["name"] + " - Online Store" 
        viewData["subtitle"] =  product["name"] + " - Product information" 
        viewData["product"] = product 
 
        return render(request, self.template_name, viewData)
    
class ProductForm(forms.Form): 
    name = forms.CharField(required=True) 
    price = forms.FloatField(required=True) 
 
 
class ProductCreateView(View): 
    template_name = 'pages/products/create.html' 
 
    def get(self, request): 
        form = ProductForm() 
        viewData = {} 
        viewData["title"] = "Create product" 
        viewData["form"] = form 
        return render(request, self.template_name, viewData) 
 
    def post(self, request): 
        form = ProductForm(request.POST) 
        if form.is_valid(): 
            name = form.cleaned_data["name"]
            price = form.cleaned_data["price"]
            
            new_product = {
                "id": str(len(Product.products) + 1),  # Generar un ID basado en la cantidad actual
                "name": name,
                "description": "New product",
                "price": price
            }
            
            Product.products.append(new_product)

            messages.success(request, "Successfully!")
            return redirect('product_success')  
        else: 
            return render(request, self.template_name, {"title": "Create product", "form": form})
        
class SuccessView(TemplateView):
    template_name = 'pages/products/product_success.html'