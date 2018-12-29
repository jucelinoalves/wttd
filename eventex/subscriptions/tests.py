from django.test import  TestCase
from eventex.subscriptions.forms import SubscriptionForm

class SubscribeTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/inscricao/')
    def test_get(self):
        """GET /inscricao / deve retornar status code 200"""
        self.assertEqual(200,self.response.status_code)

    def test_template(self):
        """Deve usar subscriptions/subscriptions_form.html"""
        self.assertTemplateUsed(self.response,'subscriptions/subscription_form.html')

    def test_html(self):
        """Html deve conter tags de input"""
        self.assertContains(self.response,'<form')
        self.assertContains(self.response, '<input',6)
        self.assertContains(self.response, 'type="text"',3)
        self.assertContains(self.response, 'type="email"')
        self.assertContains(self.response, 'type="submit"')

    def test_csrf(self):
        """Html deve conter verificação de falha CSRF """
        self.assertContains(self.response,'csrfmiddlewaretoken')

    def test_has_form(self):
        """Deve ter um contexto para o subscription_form """
        form = self.response.context['form']
        self.assertIsInstance(form,SubscriptionForm)

    def test_form_has_fields(self):
        form = self.response.context['form']
        self.assertSequenceEqual(['name','cpf','email','phone'],list(form.fields))