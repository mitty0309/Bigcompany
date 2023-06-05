from django.shortcuts import render, get_object_or_404
from product.models import Product
from .forms import ProductForm


def product(request):
  q = request.GET.get('q', None)
  products = ''
  if q is None or q is "":
    products = Product.objects.all()
  elif q is not None:
    products = Product.objects.filter(title__contains=q)
  return render(request, 'product/product.html', {'products': products})


def pdetail(request, slug=None):
  product = get_object_or_404(Product, slug=slug)
  return render(request, 'product/detail.html', locals())


def pcreate(request):
  if request.method == 'POST':
    form = ProductForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      #return HttpResponseRedirect('product/')
      return render(request, 'product/product.html', {'form': ProductForm()})
  else:
    form = ProductForm()
  return render(request, 'product/edit.html', {'form': form})


def pedit(request, pk=None):
  product = get_object_or_404(Product, pk=pk)
  if request.method == "POST":
    form = ProductForm(request.POST, instance=product)
    if form.is_valid():
      form.save()
      #return HttpResponseRedirect('product/product.html')
      return render(request, 'product/product.html', {'form': ProductForm()})
  else:
    form = ProductForm(instance=product)
  return render(request, 'product/edit.html', {'form': form})


def pdelete(request, pk=None):
  product = get_object_or_404(Product, pk=pk)
  product.delete()

  return render(request, 'product/product.html')
