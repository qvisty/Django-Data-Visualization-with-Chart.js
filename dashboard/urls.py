from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="dashboard-index"),
    path("indexAll", views.indexAll, name="indexAll"),
    path("indexA", views.indexA, name="indexA"),
    path("indexB", views.indexB, name="indexB"),
    path("indexH", views.indexH, name="indexH"),
    path("indexNull", views.indexNull, name="indexNull"),
    path("excel", views.add_from_xlsx, name="excel"),
    # path('export_users_csv/', views.export_users_csv,name="export_users_csv"),
    path("Import_csv/", views.Import_csv, name="Import_csv"),
]
