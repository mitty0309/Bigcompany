from django.shortcuts import render, get_object_or_404
from intro.models import Intro
from .forms import IntroForm


def intro(request):
  q = request.GET.get('q', None)
  intros = ''
  if q is None or q is "":
    intros = Intro.objects.all()
  elif q is not None:
    intros = Intro.objects.filter(title__contains=q)
  return render(request, 'intro/intro.html', {'intros': intros})


def idetail(request, slug=None):
  intro = get_object_or_404(Intro, slug=slug)
  return render(request, 'intro/detail.html', locals())


def icreate(request):
  if request.method == 'POST':
    form = IntroForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      #return HttpResponseRedirect('flower/')
      return render(request, 'intro/intro.html', {'form': IntroForm()})
  else:
    form = IntroForm()
  return render(request, 'intro/edit.html', {'form': form})


def iedit(request, pk=None):
  intro = get_object_or_404(Intro, pk=pk)
  if request.method == "POST":
    form = IntroForm(request.POST, instance=intro)
    if form.is_valid():
      form.save()
      #return HttpResponseRedirect('intro/')
      return render(request, 'intro/intro.html', {'form': IntroForm()})
  else:
    form = IntroForm(instance=intro)
  return render(request, 'intro/edit.html', {'form': form})


def idelete(request, pk=None):
  intro = get_object_or_404(Intro, pk=pk)
  intro.delete()

  return render(request, 'intro/')
