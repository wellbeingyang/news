from django.urls import path
import news.views as views

urlpatterns = [
    path("", views.index),
	path("news/",views.news_list),
	path("news/<int:id>",views.news_content)
]