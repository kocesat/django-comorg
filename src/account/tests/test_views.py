from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import Group, Permission
from django.contrib.auth import get_user_model
from account.models import Participant, User


class AssignRoleViewTests(TestCase):
    fixtures = [
        "groups.json",
        "permissions.json",
    ]

    def setUp(self):
        tcmb = Participant.objects.create(code="0001", name='TCMB')
        garanti = Participant.objects.create(code='0062', name='Garanti Bankası')
        sys_admin_group = Group.objects.get(name='SYSTEM_ADMIN')
        p_admin_group = Group.objects.get(name='PARTICIPANT_ADMIN')
        p_business_group = Group.objects.get(name='PARTICIPANT_BUSINESS')
        # create an admin_user
        admin_user = User.objects.create(
            email='admin@admin.com',
            password='admin',
            participant=tcmb
        )
        # assing admin_user to SYSTEM_ADMIN role
        sys_admin_group.user_set.add(admin_user)
        # create a participant admin user
        p_admin_user = User.objects.create(
            email='p_admin@garanti.com',
            password='p_admin',
            participant=garanti
        )
        # assing p_admin_user to PARTICIPANT_ADMIN role
        p_admin_group.user_set.add(p_admin_user)
        # create a participant business user
        p_business_user = User.objects.create(
            email='p_business@garanti.com',
            password='p_business',
            participant=garanti
        )
        # assing p_admin_user to PARTICIPANT_ADMIN role
        p_business_group.user_set.add(p_business_user)
    
    def test_sys_admin_can_assing_role(self):
        """
        SYSTEM_ADMIN role can assing role to every user
        """
        self.client.login(email='admin@admin.com', password='admin')
        user_id = User.objects.get(email='p_admin@garanti.com').id
        response = self.client.post(
            reverse('account:role_assing', kwargs={'user_id': user_id}),
            data={
                "chosen_role": "PARTICIPANT_ADMIN",
                "user_id": user_id
            })
        self.assertRedirects(response, 'account:account_list')
