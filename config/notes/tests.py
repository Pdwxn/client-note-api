from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from clients.models import Client
from notes.models import Note

class NoteTestCase(APITestCase):

    def authenticate(self):
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}'
        )

    def setUp(self):
        self.user = User.objects.create_user(
            username='test',
            password='123456'
        )

    def test_requires_authentication(self):
        response = self.client.get('/api/notes/')
        self.assertEqual(len(response.data), 0)

    def test_get_notes_authenticated(self):
        self.authenticate()

        response = self.client.get('/api/notes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cannot_see_others_notes(self):
        user2 = User.objects.create_user(username='other', password='123456')

        client = Client.objects.create(user=user2, name='Client X')

        Note.objects.create(
            user=user2,
            client=client,
            title='Secret Note',
            content='Hidden',
            type='idea'
        )

        self.authenticate()

        response = self.client.get('/api/notes/')

        self.assertEqual(len(response.data), 0)
    
    def test_cannot_create_note_with_other_users_client(self):
        user2 = User.objects.create_user(username='other', password='123456')

        client = Client.objects.create(user=user2, name='Client X')

        self.authenticate()

        data = {
            "title": "Hack attempt",
            "content": "test",
            "type": "idea",
            "client": client.id
        }

        response = self.client.post('/api/notes/', data)

        self.assertEqual(response.status_code, 400)

    def test_create_note_success(self):
        self.authenticate()

        client = Client.objects.create(user=self.user, name='My Client')

        data = {
            "title": "Valid note",
            "content": "OK",
            "type": "idea",
            "client": client.id
        }

        response = self.client.post('/api/notes/', data)

        self.assertEqual(response.status_code, 201)

    def test_cannot_update_other_users_note(self):
        user2 = User.objects.create_user(username='other', password='123456')

        client = Client.objects.create(user=user2, name='Client X')

        note = Note.objects.create(
            user=user2,
            client=client,
            title='Secret',
            content='Hidden',
            type='idea'
        )

        self.authenticate()

        data = {
            "title": "Hacked"
        }

        response = self.client.patch(f'/api/notes/{note.id}/', data)

        self.assertEqual(response.status_code, 403)

    def test_cannot_delete_other_users_note(self):
        user2 = User.objects.create_user(username='other', password='123456')

        client = Client.objects.create(user=user2, name='Client X')

        note = Note.objects.create(
            user=user2,
            client=client,
            title='Secret',
            content='Hidden',
            type='idea'
        )

        self.authenticate()

        response = self.client.delete(f'/api/notes/{note.id}/')

        self.assertEqual(response.status_code, 403)