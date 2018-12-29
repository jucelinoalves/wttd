from django.test import TestCase

# Create your tests here.

class HomeTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/')

    def teste_get(self):
        """GET / retorna o status code 200 """
        self.assertEqual(200,self.response.status_code)

    def test_template(self):
        """Deve usar index.html"""
        self.assertTemplateUsed(self.response, 'index.html')

    def test_subscription_lin(self):
        self.assertContains(self.response,'href="/inscricao/"')