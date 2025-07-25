from django.shortcuts import render,get_object_or_404
from .models import Product
from .forms import ProductForm
from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required
def product_list(request):
    query = request.GET.get('q')
    product_list = Product.objects.all()
    if query:
        product_list = product_list.filter(name__icontains=query)
    paginator = Paginator(product_list,1) # 5 sản phẩm mỗi trang
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'shop/product_list.html',{'page_obj':page_obj,'query':query})
@login_required
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'shop/product_detail.html', {'product': product})

@login_required
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'shop/product_form.html', {'form': form})

@login_required
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk) 
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProductForm(instance=product)
    return render(request, 'shop/product_form.html', {'form': form, 'is_edit': True, 'product': product})

@login_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'shop/product_confirm_delete.html', {'product': product})

# hết

# FBV
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Product
from .forms import ProductForm

class ProductListView(ListView):
    model = Product
    template_name = 'shop/product_list.html'
    context_object_name = 'page_obj'
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get('q')
        qs = Product.objects.all().order_by('id')
        if query:
            qs = qs.filter(name__icontains=query)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context
    
class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/product_detail.html'

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'shop/product_form.html'
    success_url = reverse_lazy('product_list')

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'shop/product_form.html'

    def get_success_url(self):
        return reverse_lazy('product_detail', kwargs={'pk': self.object.pk})

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'shop/product_confirm_delete.html'
    success_url = reverse_lazy('product_list')

