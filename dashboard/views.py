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


def indexAll(request):
    data = Freetime.objects.all().order_by("department", "-days")
    if request.method == "POST":
        form = FreetimeForm(request.POST)
        if form.is_valid():
            form.save()
            indexAll_url = reverse("indexAll")
            return redirect(indexAll_url)
    else:
        form = FreetimeForm()
    context = {
        "data": data,
        "form": form,
        "department": "All",
    }
    return render(request, "dashboard/index2.html", context)


def indexA(request):
    department = "A"
    data = Freetime.objects.filter(department__iexact=department).order_by(
        "department", "-days"
    )
    if request.method == "POST":
        form = FreetimeForm(request.POST)
        if form.is_valid():
            form.save()
            indexAll_url = reverse("indexA")
            return redirect(indexAll_url)
    else:
        form = FreetimeForm()
    context = {
        "data": data,
        "form": form,
        "department": department,
    }
    return render(request, "dashboard/index2.html", context)


def indexB(request):
    department = "B"
    data = Freetime.objects.filter(department__iexact=department).order_by(
        "department", "-days"
    )
    if request.method == "POST":
        form = FreetimeForm(request.POST)
        if form.is_valid():
            form.save()
            indexAll_url = reverse("indexB")
            return redirect(indexAll_url)
    else:
        form = FreetimeForm()
    context = {
        "data": data,
        "form": form,
        "department": department,
    }
    return render(request, "dashboard/index2.html", context)


def indexH(request):
    department = "H"
    data = Freetime.objects.filter(department__iexact=department).order_by(
        "department", "-days"
    )
    if request.method == "POST":
        form = FreetimeForm(request.POST)
        if form.is_valid():
            form.save()
            indexAll_url = reverse("indexH")
            return redirect(indexAll_url)
    else:
        form = FreetimeForm()
    context = {
        "data": data,
        "form": form,
        "department": department,
    }
    return render(request, "dashboard/index2.html", context)


def indexNull(request):
    department = ""
    data = Freetime.objects.filter(department__iexact=department).order_by(
        "department", "-days"
    )
    if request.method == "POST":
        form = FreetimeForm(request.POST)
        if form.is_valid():
            form.save()
            indexAll_url = reverse("indexNull")
            return redirect(indexAll_url)
    else:
        form = FreetimeForm()
    context = {
        "data": data,
        "form": form,
        "department": "No",
    }
    return render(request, "dashboard/index2.html", context)


def add_from_xlsx(request):
    import pandas as pd

    file = "dage.xlsx"
    df = pd.read_excel(file, usecols=["Navn", "Dage", "Afdeling"])
    print(df.head())
    df["Dage"] = df["Dage"].astype(int)
    print(df.info())
    data = df

    context = {
        "data": data,
    }
    return render(request, "dashboard/excel.html", context)
