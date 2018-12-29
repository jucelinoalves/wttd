from django.core import mail
from django.test import TestCase

from eventex.subscriptions.forms import SubscriptionForm


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Jucelino Alves',cpf='12345678901',email='jucelino@alves.net',phone='41-9854-4265')
        self.response = self.client.post('/inscricao/',data)

    def test_post(self):
        """Valida POST, e redireciona para /inscricao"""
        self.assertEqual(302,self.response.status_code)

    def test_send_subscribe_email(self):
        self.assertEqual(1,len(mail.outbox))

class SubscribeGet(TestCase):
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
        tags = (('<form',1),('<input', 6),('type="text"',3),('type="email"',1),('type="submit"',1))
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.response,text,count)

    def test_csrf(self):
        """Html deve conter verificação de falha CSRF """
        self.assertContains(self.response,'csrfmiddlewaretoken')

    def test_has_form(self):
        """Deve ter um contexto para o subscription_form """
        form = self.response.context['form']
        self.assertIsInstance(form,SubscriptionForm)


class SubscribePostInvalid(TestCase):
    def setUp(self):
        self.response = self.client.post('/inscricao/',{})

    def test_post(self):
        """POST inválido não deve redirecionar"""
        self.assertEqual(200,self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response,'subscriptions/subscription_form.html')

    def test_has_form(self):
        form = self.response.context['form']
        self.assertIsInstance(form,SubscriptionForm)

    def test_form_has_erros(self):
        form = self.response.context['form']
        self.assertTrue(form.errors)

class SubscribeSucessMessage(TestCase):
    def test_message(self):
        data = dict(name='Jucelino Alves',cpf='12345678901',email='jucelino@alves.net',phone='41-9854-4265')
        response = self.client.post('/inscricao/',data,follow=True)
        self.assertContains(response,'Inscrição realizada com sucesso!')
