from django.contrib import admin
from django.urls import path
from main_app.views import MainView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/', MainView.as_view()),
    path('get/', MainView.as_view()),
]
