from django.urls import path  # Importamos la función 'path' para definir patrones de URL
#from .views import get_instagram_posts  # Importamos la vista 'get_instagram_posts' desde nuestro archivo views.py
from .views import news_feed

#Creamos una lista donde almacenaremos todos los patrones de URL de nuestra aplicación.
urlpatterns = [
    #path('get-posts/<str:account>/', get_instagram_posts, name='get_instagram_posts'),
    #path('instagram-posts/<str:account>/', get_instagram_posts, name='get_instagram_posts'),
    path('instagram-posts/<str:account>/', news_feed, name='news_feed'),
   
]

















#'get-posts/<str:account>/': Esta es la parte de la URL que coincidirá con las solicitudes de los usuarios.
#'get-posts/': Parte fija de la URL.
#<str:account>: Parte variable de la URL que representa el nombre de la cuenta de Instagram. 
#Esta parte será capturada y pasada como argumento a la vista.

#get_instagram_posts: Indica que cuando se haga una solicitud a esta URL, 
# se ejecutará la función get_instagram_posts en el archivo views.py.

#`name='get_posts'``: Asigna un nombre a este patrón de URL. 
# Este nombre se puede usar en otras partes de la aplicación (por ejemplo, en plantillas o formularios)
#  para generar enlaces a esta URL.