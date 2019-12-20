from rest_framework.test import APITestCase
from unittest.mock import MagicMock, patch
from api.service import GetAllInvitationsService, CreateInvitationsService ,DeleteInvitationsService, UpdateInvitationsService
from api.factory import FactoryInvitation, UserFactory
from api.models import Invitation
from api.views import InvitationsViews
from collections import OrderedDict
from faker import Faker

fake = Faker()

class TestInvitationsViews(APITestCase):

	def setUp(self):
		self.email = fake.ascii_email()
		self.invitation_obj = FactoryInvitation(id="a60d18de-474c-4945-9a5f-387cc1317f40")

	def test_invitation_create(self):
		CreateInvitationsService.execute = MagicMock(return_value=self.invitation_obj)
		mock_request = MagicMock(data={"email":self.invitation_obj.email,"creator":self.invitation_obj.creator.id})
		response = InvitationsViews.post(mock_request)
		assert response.status_code == 201
		assert response.data["data"]["email"] == self.invitation_obj.email
		assert response.data["data"]["createdTime"] == self.invitation_obj.created_time
		assert response.data["data"]["used"] == self.invitation_obj.used
		assert response.data["data"]["id"] == self.invitation_obj.id
		CreateInvitationsService.execute.assert_called_once_with({'serial_data': OrderedDict([('email', response.data["data"]["email"]), ('creator', 1)])})


	@patch("api.service.DeleteInvitationsService.execute",
        MagicMock(return_value="SuccessfullyDeleted"),
    )
	def test_invitation_delete(self):
		invitaion_obj = Invitation.objects.get(id=self.invitation_obj.id)
		response = InvitationsViews.delete(MagicMock, invitaion_obj.id)
		
		assert response.data == "SuccessfullyDeleted"
		assert response.status_code == 200
		DeleteInvitationsService.execute.assert_called_once_with({"invitations_id":invitaion_obj.id})


	@patch("api.service.UpdateInvitationsService.execute",
        MagicMock(return_value="SuccessfullyUpdated")
    )
	def test_invitation_patch(self):
		mock_request = MagicMock(data={"email":self.email})
		response = InvitationsViews.patch(mock_request,"adadad2313")
		assert response.status_code == 200
		assert response.data["data"] == "SuccessfullyUpdated"
		UpdateInvitationsService.execute.assert_called_once_with({'invitations_id': 'adadad2313', 'email': self.email, 'used': None})
