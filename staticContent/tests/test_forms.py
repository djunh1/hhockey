from django.test import TestCase
from django.core.urlresolvers import reverse
from django.utils.html import escape

from staticContent.forms import ContactForm

class ContactFormTest(TestCase):
    def post_invalid_input(self):
        pass

    def test_form_renders_with_correct_fields(self):
        form = ContactForm()
        self.assertTrue(form.fields['contact_name'])
        self.assertTrue(form.fields['contact_email'])
        self.assertTrue(form.fields['content'])

    def test_display_contactform(self):
        response = self.client.get(reverse('contact_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['form'] == ContactForm) #hacky.  IsInstance did not work

    def test_form_validation_for_bad_submission(self):
        form_data = {'contact_name': 'Dory', 'contact_email': '', 'content': ''}
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_error_message_for_bad_submission(self):
        form_data = {'contact_name': 'Dory', 'contact_email': '', 'content': ''}
        response = self.client.post(reverse('contact_page'), data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'site/contact.html')
        html = response.content.decode('utf8')
        expected_error_html = '<div class="aui-message aui-message-error">'
        self.assertIn( expected_error_html, html)

    def test_success_message_for_sat_submission(self):
        form_data = {'contact_name': 'test', 'contact_email': 'test1235@gmail.com', 'content': 'Simple test message.'}
        response = self.client.post(reverse('contact_page'), data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'site/contact.html')
        html = response.content.decode('utf8')
        expected_html = '<div class="aui-message success">'
        self.assertIn( expected_html, html)