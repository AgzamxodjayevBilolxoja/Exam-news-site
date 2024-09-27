from django.urls import path

from .views import home_page, news1_page, news2_page, news3_page, news4_page, news_about

urlpatterns = [
    path("", home_page, name="home_page"),
    path("news1/", news1_page, name="news_1"),
    path("news2/", news2_page, name="news_2"),
    path("news3/", news3_page, name="news_3"),
    path("news4/", news4_page, name="news_4"),
    path("new_about/<int:pk>", news_about, name="news_about")
]