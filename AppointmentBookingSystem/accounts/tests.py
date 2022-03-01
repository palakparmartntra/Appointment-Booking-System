from django.test import TestCase
from accounts.constants import ROLE, SPECIALITIES
from accounts.models import User
# Create your tests here.

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="viruu", role=ROLE[0][0], specialities=SPECIALITIES[0][0])

    def test_1(self):
        user = User.objects.get(username="viruu")
        self.assertEqual(str(user), user.username)

    def test_2(self):
        role = User.objects.get(role=ROLE[0][0])
        spec = User.objects.get(specialities = SPECIALITIES[0][0])
        self.assertFalse(True)
            
        # self.assertEqual(role.specialities, role.specialities!=None)
