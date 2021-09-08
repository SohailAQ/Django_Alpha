from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView
)
from .models import Products


class ProductListView(ListView):
    model = Products


class ProductCreateView(CreateView):
    model = Products
    fields = ['name', 'ingredients', 'price']


class ProductDetailView(DetailView):
    model = Products


class ProductUpdateView(UpdateView):
    model = Products
    fields = ['name', 'ingredients', 'price']


class ProductDeleteView(DeleteView):
    model = Products
    success_url = '/'
