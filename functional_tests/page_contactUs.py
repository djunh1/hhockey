from .base import FunctionalTest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class ContactUsPageTest(FunctionalTest):
    def test_can_open_contactUs_page(self):
        '''
        User has a question and navigates to the Contact Page.  They check the browser
        to verify that they landed on the right page.
        '''
        self.browser.get('http://heritage-hockey.com:8000/contact')
        self.assertIn('Hopewell Hockey | Contact', self.browser.title)

    def test_form_does_not_submit_with_no_information(self):
        '''
        The user accidentally submits the form with no data in the fields.  The web page
        shows this by displaying a graphic error message, and field errors.
        '''
        self.browser.get('http://heritage-hockey.com:8000/contact')
        self.browser.find_element_by_css_selector("button.small-btn").click()
        error = self.browser.find_element_by_css_selector("div.aui-message.aui-message-error")
        self.assertEqual(error.text, 'There was an error while submitting the form. Please check the errors and submit '
                                  'the form again.')
        field_error_name = self.browser.find_elements_by_css_selector("ul.errorlist")
        for i in range(0, 2):
            self.assertEqual(field_error_name[i].text, 'This field is required.')

    def test_user_submits_a_partial_form(self):
        '''
        After 5 hours of research, the user begins to understand how to fill out a form.  They fill out
        the name and content but forget the email.  They will once again see the graphic error and field errors

        '''
        self.browser.get('http://heritage-hockey.com:8000/contact')
        self.browser.find_element_by_id('id_contact_name').send_keys('Eric Seager')
        self.browser.find_element_by_id('id_content').send_keys('That goal was unassisted baby.  Send me a hockey '
                                                                'stick')
        self.browser.find_element_by_css_selector("button.small-btn").click()
        error = self.browser.find_element_by_css_selector("div.aui-message.aui-message-error")
        self.assertEqual(error.text, 'There was an error while submitting the form. Please check the errors and submit '
                                  'the form again.')
        field_error_name = self.browser.find_elements_by_css_selector("ul.errorlist")
        for i in range(0, 1):
            self.assertEqual(field_error_name[i].text, 'This field is required.')




