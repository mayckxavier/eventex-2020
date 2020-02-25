from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Mayck Xavier', cpf='12345678901',
                    email='contato@mayckxavier.com', phone='21-9-8657-5108')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmacao de inscricao'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'contato@mayckxavier.com']
        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = ['Mayck Xavier', '12345678901', 'contato@mayckxavier.com', '21-9-8657-5108']

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
