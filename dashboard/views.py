from django.shortcuts import render, redirect
from django.urls import reverse
from .models import CountryData, Freetime
from .forms import CountryDataForm, FreetimeForm

# Create your views here.


def index(request):
    data = CountryData.objects.all()
    if request.method == "POST":
        form = CountryDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = CountryDataForm()
    context = {
        "data": data,
        "form": form,
    }
    return render(request, "dashboard/index.html", context)


def index2(request):
    data = Freetime.objects.all().order_by("department", "-days")
    if request.method == "POST":
        form = FreetimeForm(request.POST)
        if form.is_valid():
            form.save()
            index2_url = reverse("index2")
            return redirect(index2_url)
    else:
        form = FreetimeForm()
    context = {
        "data": data,
        "form": form,
        "department": "All",
    }
    return render(request, "dashboard/index2.html", context)

def indexA(request):
    data = Freetime.objects.all().order_by("department", "-days")
    if request.method == "POST":
        form = FreetimeForm(request.POST)
        if form.is_valid():
            form.save()
            index2_url = reverse("index2")
            return redirect(index2_url)
    else:
        form = FreetimeForm()
    context = {
        "data": data,
        "form": form,
    }
    return render(request, "dashboard/index2.html", context)
