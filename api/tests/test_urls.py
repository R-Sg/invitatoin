from django.urls import reverse, resolve
from rest_framework import status
from rest_framework.test import APITestCase
import uuid
from api.factory import FactoryInvitation
from api.views import InvitationsViews

class TestFirstApi(APITestCase):
    """
    """

    def setUp(self):
        self.first_url = reverse("invitations")
        self.invitation = FactoryInvitation()
        self.second_url =reverse("delete_invitations", args=[self.invitation.id])
        
    def test_invitation_get_all_api(self):
        """
        """
        response = self.client.get(self.first_url)
        result = resolve(self.first_url)
        assert result.func.view_class == InvitationsViews
        # Check status code for success url.
        assert response.status_code == status.HTTP_200_OK


    def test_invitation_get_api(self):
        """
        """
        response = self.client.delete(self.second_url)
        result = resolve(self.second_url)
        assert result.func.view_class == InvitationsViews
        # Check status code for success url.
        assert response.status_code == status.HTTP_200_OK
