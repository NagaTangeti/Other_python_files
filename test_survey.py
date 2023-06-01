#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 17:39:05 2023

@author: nagatangeti
"""

import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey"""
   
    def setUp(self):
        """
        Create a survey and a set of responses for use in all tests methods.
        """
        question = "What language did u first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['english', 'spanish', 'mandarin']

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
        
    def test_store_three_response(self):
        """Test that three responses is stored properly."""
        
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertEqual('english', self.my_survey.responses)
        
if __name__ == '__main__':
    unittest.main()
    