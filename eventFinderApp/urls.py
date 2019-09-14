from django.urls import path, include

from . import views


app_name = 'eventFinderApp'

urlpatterns = [
    # event-finder/
    path('', views.IndexView.as_view(), name='index'),
    # event-finder/1
    path('<int:pk>/', views.EventView.as_view(), name='event'),
    # event-finder/my-account
    path('create/', views.EventCreate.as_view(), name='create'),
    path('my-account/', views.account, name='account'),
    path('users/', include('django.contrib.auth.urls'))
]