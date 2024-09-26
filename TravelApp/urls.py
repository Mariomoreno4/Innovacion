from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('listPlaces', views.listPlaces, name='listPlaces'),
    path('placeDetails/<int:placeId>', views.placeDetails, name='placeDetails'),
    #path('addComment/<int:placeId>', views.addComment, name='addComment'),

]