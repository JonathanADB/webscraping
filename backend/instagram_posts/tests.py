from django.test import TestCase
from unittest.mock import patch
import logging
from instagram_posts.views import download_instagram_posts

class DownloadInstagramPostsTestCase(TestCase):

    @patch('instagram_posts.views.instaloader.Profile.from_username')
    def test_profile_not_exists_logging(self, mock_from_username):
        # Simula la excepción ProfileNotExistsException
        mock_from_username.side_effect = Exception('Test error: Profile not found')

        # Crea un logger en memoria para capturar los logs
        with self.assertLogs('instagram_posts.views', level='ERROR') as log:
            download_instagram_posts('non_existent_account')

        # Verifica que el log contiene el mensaje correcto
        self.assertIn('Test error: Profile not found', log.output[0])

        


logger = logging.getLogger('django')

class MyTestCase(TestCase):
    def test_error_logging(self):
        logger.info('Prueba de logging en test')  # Añade esto
        with self.assertRaises(ZeroDivisionError):
            result = 1 / 0

