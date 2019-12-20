from api.factory import FactoryInvitation, UserFactory
from rest_framework.test import APITestCase
from api.models import Invitation

class TestInvitaionModel(APITestCase):

	def setUp(self):
		self.user = UserFactory()
		self.invitation = FactoryInvitation(creator=self.user)

	def test_invitaion_model(self):
	
		invitation_obj = Invitation.objects.get(id=self.invitation.id)
		assert invitation_obj == self.invitation
		assert invitation_obj.id == self.invitation.id
		assert invitation_obj.creator_id == self.invitation.creator_id
		assert invitation_obj.email == self.invitation.email
		assert invitation_obj.used == self.invitation.used
		assert invitation_obj.created_time == self.invitation.created_time