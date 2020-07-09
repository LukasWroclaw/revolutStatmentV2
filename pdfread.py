# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 09:44:57 2020

@author: marszale
"""
import unittest
import PyPDF2

testuj = 0

class pdfRead:


    def createFileHandler(self, fileName):
        file = open(fileName, 'rb')
        self.fileHandler = PyPDF2.PdfFileReader(file)
    
    def getFileHandler(self):
        return self.fileHandler
    
    def getTextFromPage(self, pageNumber):
        page = self.fileHandler.getPage(pageNumber)
        return page.extractText()



class TestingClass(unittest.TestCase):
  
    @classmethod
    def setUpClass(cls):
        readInstance = pdfRead()
        readInstance.createFileHandler('test1.pdf')
        cls._readInstance = readInstance
 

    def test_numberOfPages(self):
        self.assertEqual(self._readInstance.getFileHandler().numPages, 1)
        
    def test_extractFirstPageText(self):
        extractedText = self._readInstance.getTextFromPage(0)
        self.assertEqual(extractedText, "Ala Ma Kota\n \n")

if(testuj):
    suite = unittest.TestLoader().loadTestsFromTestCase(TestingClass)
    unittest.TextTestRunner(verbosity=2).run(suite)