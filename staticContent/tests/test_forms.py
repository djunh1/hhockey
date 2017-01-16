from django.test import TestCase

from staticContent.forms import ContactForm

class ContactFormTest(TestCase):
    def test_form_renders_with_correct_fields(self):
        form = ContactForm()
        self.assertTrue(form.fields['contact_name'])
        self.assertTrue(form.fields['contact_email'])
        self.assertTrue(form.fields['content'])

    def test_form_validation_for_bad_email(self):
        form_data = {'contact_name': 'Dory', 'contact_email': 'bademail.com', 'content': ''}
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors,
            ["Please complete this field"]
        )