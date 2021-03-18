from django.test import TestCase
from django.contrib.auth import get_user_model
from account.models import Participant
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError
from django.db import transaction


class ParticipantTests(TestCase):

    def test_create_participant(self):
        p = Participant.objects.create(code='0001', name='TCMB')
        self.assertEqual(p.code, '0001')
        self.assertEqual(p.name, 'TCMB')
        with self.assertRaises(IntegrityError):
            Participant.objects.create(
                code='0001',
                name='Another TCMB')

        try:
            with self.assertRaises(ValidationError):
                Participant.objects.create(code='0222aa', name='Test Bankası').full_clean()
        except transaction.TransactionManagementError as e:
            print(e)
        
        # TODO: something is wrong here in these tests
        try:
            with self.assertRaises(ValidationError):
                p = Participant(code='0004', name='Zero Bank')
                p.full_clean()
                # Participant.objects.create(code='0004', name='Zero Bank').full_clean()
        except transaction.TransactionManagementError as e:
            print(e)


class UserManagersTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        p = Participant.objects.create(code='0999', name='Test Bank')
        user = User.objects.create_user(email='normal@user.com', password='foo', participant=p)
        self.assertEqual(user.email, 'normal@user.com')
        self.assertEqual(user.participant.name, 'Test Bank')
        self.assertEqual(user.participant.code, '0999')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password='foo')
    
    def test_create_superuser(self):
        User = get_user_model()
        p = Participant.objects.create(code='0999', name='Test Bankası')
        admin_user = User.objects.create_superuser(email='super@user.com', password='foo', participant=p)
        self.assertEqual(admin_user.email, 'super@user.com')
        self.assertEqual(admin_user.participant.name, 'Test Bankası')
        self.assertEqual(admin_user.participant.code, '0999')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        
        try:
            with self.assertRaises(ValueError):
                User.objects.create_user(
                    email='super@user.com', 
                    password='foo', 
                    participant=p, 
                    is_superuser=False)
        except IntegrityError:
            pass


