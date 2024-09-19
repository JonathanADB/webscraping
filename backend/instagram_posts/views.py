""" from django.http import JsonResponse
from django.conf import settings
from pathlib import Path
import instaloader
import logging

logger = logging.getLogger(__name__)

MAX_POSTS = 10

def download_instagram_posts(account):
    loader = instaloader.Instaloader()
    posts = []
    
    try:
        profile = instaloader.Profile.from_username(loader.context, account)
        
        # Recoge los datos de seguidores y cuentas seguidas
        followers = profile.followers
        followees = profile.followees
        
        for post_count, post in enumerate(profile.get_posts()):
            if post_count < MAX_POSTS:
                # Define el directorio donde se guardarán las imágenes
                account_dir = Path(settings.MEDIA_ROOT) / account
                account_dir.mkdir(parents=True, exist_ok=True)
                image_file = account_dir / f'post_{post_count + 1}.jpg'
                loader.download_post(post, target=image_file)
                posts.append({
                    'url': f'{settings.MEDIA_URL}{account}/post_{post_count + 1}.jpg',
                    'date': post.date,
                    'caption': post.caption,  
                })
            else:
                break
    except instaloader.exceptions.ProfileNotExistsException:
        logger.error(f'Perfil no existe: {account}')
        return None
    except instaloader.exceptions.ConnectionException:
        logger.error(f'Error de conexión al intentar acceder a: {account}')
        return None
    except instaloader.exceptions.LoginRequiredException:
        logger.error(f'Se requiere inicio de sesión para acceder a: {account}')
        return None
    except Exception as e:
        logger.error(f'Error inesperado: {str(e)}')
        return None

    # Devuelve los datos del perfil junto con las publicaciones
    return {
        'followers': followers,
        'followees': followees,
        'posts': posts
    }

def get_instagram_posts(request, account):
    profile_data = download_instagram_posts(account)
    
    if profile_data:
        return JsonResponse(profile_data)
    else:
        return JsonResponse({'error': 'No se encontraron publicaciones o el perfil no existe.'}, status=404)

"""





from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from pathlib import Path
import instaloader
import logging
from .models import InstagramAccount, InstagramPost
import os

logger = logging.getLogger(__name__)

MAX_POSTS = 10

def download_instagram_posts(account):
    loader = instaloader.Instaloader()
    posts = []
    
    try:
        profile = instaloader.Profile.from_username(loader.context, account)
        
        # Recoge la foto de perfil
        profile_picture_url = profile.profile_pic_url

        # Define el directorio donde se guardará la foto de perfil
        account_dir = Path(settings.MEDIA_ROOT) / 'instagram' / 'user_photos' / account
        account_dir.mkdir(parents=True, exist_ok=True)
        profile_picture_path = account_dir / 'profile_picture.jpg'
        
        # Verificar si la foto de perfil ha cambiado
        if not profile_picture_path.exists() or profile_picture_path.stat().st_mtime < profile.profile_pic_url_hd_updated:
            # Descargar la foto de perfil
            loader.download_pic(profile_picture_path, profile_picture_url, mtime=None)
        
        # Actualizar el modelo InstagramAccount
        instagram_account, created = InstagramAccount.objects.update_or_create(
            username=account,
            defaults={
                'profile_picture': f'instagram/user_photos/{account}/profile_picture.jpg'
            }
        )
        
        for post_count, post in enumerate(profile.get_posts()):
            if post_count < MAX_POSTS:
                # Verificar si la publicación ya existe en la base de datos
                if not InstagramPost.objects.filter(account=instagram_account, date=post.date).exists():
                    # Define el directorio donde se guardarán las imágenes
                    post_image_path = account_dir / f'post_{post_count + 1}.jpg'
                    loader.download_post(post, target=post_image_path)
                    posts.append({
                        'url': f'{settings.MEDIA_URL}instagram/user_photos/{account}/post_{post_count + 1}.jpg',
                        'date': post.date,
                        'caption': post.caption,  
                    })
                    
                    # Guardar la publicación en la base de datos
                    InstagramPost.objects.create(
                        account=instagram_account,
                        date=post.date,
                        caption=post.caption,
                        photo=f'instagram/user_photos/{account}/post_{post_count + 1}.jpg'
                    )
            else:
                break
    except instaloader.exceptions.ProfileNotExistsException:
        logger.error(f'Perfil no existe: {account}')
        return None
    except instaloader.exceptions.ConnectionException:
        logger.error(f'Error de conexión al intentar acceder a: {account}')
        return None
    except instaloader.exceptions.LoginRequiredException:
        logger.error(f'Se requiere inicio de sesión para acceder a: {account}')
        return None
    except Exception as e:
        logger.error(f'Error inesperado: {str(e)}')
        return None

    # Devuelve los datos del perfil junto con las publicaciones
    return {
        'profile_picture_url': f'{settings.MEDIA_URL}instagram/user_photos/{account}/profile_picture.jpg',
        'posts': posts
    }

def get_instagram_posts(request, account):
    profile_data = download_instagram_posts(account)
    
    if profile_data:
        return JsonResponse(profile_data)
    else:
        return JsonResponse({'error': 'Error al descargar las publicaciones.'}, status=500)

def news_feed(request, account):
    posts = InstagramPost.objects.filter(account__username=account).order_by('-date')
    return render(request, 'instagram_posts/news_feed.html', {'posts': posts})

def clean_old_files():
    accounts = InstagramAccount.objects.all()
    for account in accounts:
        account_dir = Path(settings.MEDIA_ROOT) / 'instagram' / 'user_photos' / account.username
        if account_dir.exists():
            for file in account_dir.iterdir():
                if file.is_file() and not InstagramPost.objects.filter(photo=str(file.relative_to(settings.MEDIA_ROOT))).exists():
                    os.remove(file)






""" AQUI LA SOLUCION GUAY ES USAR CELERY(CREO), PERO NO ME DA TIEMPO
    Manejo de Errores en get_instagram_posts: Ahora devuelve un mensaje de error genérico y un código de estado HTTP 500 en caso de fallo.
    Descarga de la Foto de Perfil: Se verifica si la foto de perfil ha cambiado antes de descargarla nuevamente.
    Seguridad: Se proporciona un mensaje genérico en caso de error.
    Limpieza de Archivos Antiguos: Se incluye una función clean_old_files para eliminar archivos antiguos que ya no existen en la base de datos.
 """