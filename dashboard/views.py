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
    df = pd.read_excel(file)
    df = df.fillna("Ingen")
    afdelinger = df.Afdeling.unique()
    print(df.head())
    print(df.info())
    headers = ["Navn", "Dage", "Afdeling"]
    data = df.to_dict()

    context = {
        "data": data,
        "afdelinger": afdelinger,
        "headers": headers,
    }
    return render(request, "dashboard/excel.html", context)


from .models import Employee
import pandas as pd
from django.conf import settings
from django.core.files.storage import FileSystemStorage


def Import_csv(request):
    import os

    if request.method == "POST" and request.FILES["myfile"]:
        try:

            myfile = request.FILES["myfile"]
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            excel_file = uploaded_file_url
            empexceldata = pd.read_excel("." + excel_file)
            dbframe = empexceldata
            Employee.objects.all().delete()
            for dbframe in dbframe.itertuples():
                obj = Employee.objects.create(
                    firstName=dbframe.Navn,
                    days=dbframe.Dage,
                    department=dbframe.Afdeling,
                )
                obj.save()

            import os

            if os.path.exists("." + excel_file):
                os.remove("." + excel_file)
            else:
                print("The file does not exist")

            return render(
                request,
                "dashboard/importexcel.html",
                {"uploaded_file_url": uploaded_file_url, "data": dbframe},
            )
        except Exception as identifier:
            print(identifier)

    return render(request, "dashboard/importexcel.html", {})
