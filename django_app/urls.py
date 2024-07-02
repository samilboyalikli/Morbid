from django.urls import path
from . import views


urlpatterns = [
    path("", views.form_, name="form"),
    # burada "name" eklemediğim taktirde program,
    # html dosyasında kodladığımız DTL kodundaki url'i buradaki url'le eşleştiremiyor
    path("result", views.result, name="result"),
    path("", views.redirecting_view, name="redirecting")
]
