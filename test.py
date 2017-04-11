# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from seleniumbase import BaseCase

class MyTestClass(BaseCase):

    def test_basic(self):
        self.open('http://xkcd.com/353/')            # Navigate to the web page
        self.assert_element('img[alt="Python"]')       # Assert element on page
        self.click('a[rel="license"]')                  # Click element on page
        self.assert_text('copy and reuse', 'div center')  # Assert element text
        self.open('http://xkcd.com/1481/')
        image_object = self.find_element('#comic img')    # Returns the element
        caption = image_object.get_attribute('title')   # Get element attribute
        self.assertTrue('connections to the server' in caption)
        self.click_link_text('Blag')              # Click on link with the text
        self.assert_text('xkcd', '#site-title')
        header_text = self.get_text('header h2')  # Grab text from page element
        self.assertTrue('The blag of the webcomic' in header_text)
        self.update_text('input#s', 'Robots!\n')  # Fill in field with the text
        self.assert_text('Hooray robots!', '#content')
        self.open('http://xkcd.com/1319/')
        self.assert_text('Automation', 'div#ctitle')