from django.test import TestCase
from api.integrations.github import GithubApi

# Create your tests here.
gitApi = GithubApi()

class GithubApiTestCase(TestCase):
  
  def test_get_organization(self):
    
    response = gitApi.get_organization(login='Netflix')
    
    self.assertEqual(response.status_code, 200)

  def test_get_organization_public_members(self):
    
    response = gitApi.get_organization_public_members(login='Netflix')
    
    self.assertEqual(response, 21)

