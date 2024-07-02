from django.shortcuts import render, redirect
from .forms import VeriForm
from .models import Veri
from django.db import models


def form_(request):
    if request.method == 'POST':
        form = VeriForm(request.POST)
        if form.is_valid():
            kilo = form.cleaned_data['kilo']
            boy = form.cleaned_data['boy']
            veri = Veri(kilo=kilo, boy=boy)
            veri.save()
            return redirect('result')
    return render(request, "form.html")


def result(request):
    veriler = Veri.objects.latest()
    boy_ = veriler.boy
    kilo_ = veriler.kilo
    payda = boy_ * boy_
    index2 = kilo_ / payda
    ideal_kilo_ = 24.9 * float(payda)
    z_ideal_kilo = 18.5 * float(payda)
    z_verim = z_ideal_kilo - float(kilo_)
    verim = float(kilo_) - ideal_kilo_
    index1 = round(index2, 1)

    kategori = None
    normal_kilo = None
    advice = None
    yuklem = None
    min_max = None
    cumle_giris = None
    cumle_orta = None

    if index1 < 18.5:
        kategori = "ZAYIF"
        advice = round(z_verim, 1)
        normal_kilo = round(z_ideal_kilo, 1)
        yuklem = "almalısınız."
        min_max = "Minimum"
        cumle_giris = "En azından "
        cumle_orta = " kilo "
    elif 18.5 < index1 < 24.9:
        kategori = "NORMAL"
        normal_kilo = round(ideal_kilo_, 1)
        min_max = "Maximum"
        if advice is None:
            advice = ""
        if cumle_giris is None:
            cumle_giris = ""
        if yuklem is None:
            yuklem = "TEBRİKLER... KİLONUZ İDEAL SEVİYEDE."
        if cumle_orta is None:
            cumle_orta = ""
    elif 24.9 < index1 < 29.9:
        kategori = "KİLOLU"
        normal_kilo = round(ideal_kilo_, 1)
        advice = round(verim, 1)
        yuklem = "vermelisiniz."
        min_max = "Maximum"
        cumle_giris = "En azından "
        cumle_orta = " kilo "
    elif 29.9 < index1 < 34.9:
        kategori = "OBEZ"
        normal_kilo = round(ideal_kilo_, 1)
        advice = round(verim, 1)
        yuklem = "vermelisiniz."
        min_max = "Maximum"
        cumle_giris = "En azından "
        cumle_orta = " kilo "
    elif 34.9 < index1:
        kategori = "MORBİD OBEZ"
        normal_kilo = round(ideal_kilo_, 1)
        advice = round(verim, 1)
        yuklem = "vermelisiniz."
        min_max = "Maximum"
        cumle_giris = "En azından "
        cumle_orta = " kilo "

    context = {
        'indeks': index1,
        'kategori': kategori,
        'normal_kilo': normal_kilo,
        'advice': advice,
        'yuklem': yuklem,
        'min_max': min_max,
        'cumle_giris': cumle_giris,
        'cumle_orta': cumle_orta
    }

    return render(request, "result.html", context)


def redirecting_view(request):
    if request.method == 'POST':
        return redirect('form')
    return render(request, 'result.html')



