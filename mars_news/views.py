from django.shortcuts import render

from .models import NewsEn, CategoryEn

def home_page(request):
    news = NewsEn.objects.all()
    context = {
        "news1": news.first(),
        "news2": news[1:5],
        "news3": news[5:10],
        "news4": news[11:]
    }
    return render(request, "home_page.html", context)


def news1_page(request):
    category = CategoryEn.objects.filter(title="News_1").first()

    news = NewsEn.objects.filter(category=category)
    context = {
        "news1": news.first(),
        "news2": news[1:5],
        "news3": news[5:10],
        "news4": news[11:]
    }
    return render(request, "news1.html", context)

def news2_page(request):
    category = CategoryEn.objects.filter(title="News_2").first()

    news = NewsEn.objects.filter(category=category)
    context = {
        "news1": news.first(),
        "news2": news[1:5],
        "news3": news[5:10],
        "news4": news[11:]
    }
    return render(request, "news2.html", context)

def news3_page(request):
    category = CategoryEn.objects.filter(title="News_3").first()

    news = NewsEn.objects.filter(category=category)
    context = {
        "news1": news.first(),
        "news2": news[1:5],
        "news3": news[5:10],
        "news4": news[11:]
    }
    return render(request, "news3.html", context)

def news4_page(request):
    category = CategoryEn.objects.filter(title="News_4").first()

    news = NewsEn.objects.filter(category=category)
    context = {
        "news1": news.first(),
        "news2": news[1:5],
        "news3": news[5:10],
        "news4": news[11:]
    }
    return render(request, "news4.html", context)

def news_about(request, pk):
    new  = NewsEn.objects.filter(id=pk).first()
    context = {
        "new":new
    }
    return render(request, "news_about.html", context)