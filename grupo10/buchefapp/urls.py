from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
'''
*La pagina de Home Page redireccion a restaurante y review
*Restaurante redirecciona a review
*De restaurante se debe poder volver a home page
*De review a restaurante 
'''
app_name = 'buchefapp'


"""Current urls that are implemented"""
urlpatterns = [
    path('register/', views.register_user, name='register_user'), 
    path('login',views.login_user, name='login'),
    path('logout',views.logout_user, name='logout'),
    path('',views.home, name='home'),
    path('home/',views.home, name='home'),
    path('home/<int:categoria>/',views.home, name='home'),
    
    path('review/<int:local_id>/', views.review, name='review'),
    path('restaurant/<int:local_id>/', views.restaurant, name='restaurant'),
    path('agregar_local/', views.agregar_local, name='agregar_local') 

]

#debug settings

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)