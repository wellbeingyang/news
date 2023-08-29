from django.urls import path
import categories.views as views

urlpatterns = [
	path("",views.categories),
	path("<int:month>",views.content)
]