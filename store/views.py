from django.shortcuts import render, get_object_or_404
from store.models import Store
from .forms import StoreForm


def stores(request):
  q = request.GET.get('q', None)
  stores = ''
  if q is None or q is "":
    stores = Store.objects.all()
  elif q is not None:
    stores = Store.objects.filter(title__contains=q)
  return render(request, 'store/store.html', {'stores': stores})


def sdetail(request, slug=None):
  store = get_object_or_404(Store, slug=slug)
  return render(request, 'store/detail.html', locals())


def screate(request):
  if request.method == 'POST':
    form = StoreForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      #return HttpResponseRedirect('store/')
      return render(request, 'store/store.html', {'form': StoreForm()})
  else:
    form = StoreForm()
  return render(request, 'store/edit.html', {'form': form})


def sedit(request, pk=None):
  store = get_object_or_404(Store, pk=pk)
  if request.method == "POST":
    form = StoreForm(request.POST, instance=store)
    if form.is_valid():
      form.save()
      #return HttpResponseRedirect('store/')
      return render(request, 'store/store.html', {'form': StoreForm()})
  else:
    form = StoreForm(instance=store)
  return render(request, 'store/edit.html', {'form': form})


def sdelete(request, pk=None):
  store = get_object_or_404(Store, pk=pk)
  store.delete()

  return render(request, 'store/store.html')
