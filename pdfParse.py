# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 12:32:50 2020

@author: marszale
"""

from pdfread import pdfRead
from stringToDataBaseElementsConverter import stringToDataBaseElementsConverter
import re
import unittest
testuj = 0

class pdfParser:
    
    def __init__(self, listOfRecords):
        self.converter = stringToDataBaseElementsConverter()
        self.listOfRecords = listOfRecords
    
    def extractActivityParagraph(self, text):
        buffor = text.split("ACTIVITY")
        buffor = buffor[1].split("SWEEP")
        buffor = buffor[0].split("Amount")
        
        self.activityParagraphData = buffor[1]

        
    def splitActivityParagraphIntoSeparateLines(self):
        linesSplitted = self.activityParagraphData.split("\n")
        linesSplitted = linesSplitted[1:-1]
        self.linesSplitted = linesSplitted
        
    def trimAdditionalFieldAndProcess(self, bufforForLines):
        if(len(bufforForLines[5]) > 1):
                buf = bufforForLines[:5] + bufforForLines[6:9]
                self.listOfRecords.append(self.converter.convertTransaction(buf))
                return bufforForLines[9:]
        else:
                self.listOfRecords.append(self.converter.convertTransaction(bufforForLines[:8]))
                return bufforForLines[8:]

        
    def splitLinesIntoSeparateReports(self):
        
        bufforForLines = self.linesSplitted
        
        pattern = re.compile("(\d{1,2})/(\d{1,2})/(\d{1,4})")
        
        
        while len(bufforForLines) > 0 and pattern.match(bufforForLines[0]) != None:
                        
            if(bufforForLines[3] == "BUY" or bufforForLines[3] == "SELL"):
                self.listOfRecords.append(self.converter.convertTransaction(bufforForLines[:8]))
                bufforForLines = bufforForLines[8:]
                
            elif(bufforForLines[3] == "CDEP" or bufforForLines[3] == "CSD"):
                self.listOfRecords.append(self.converter.convertWalletAction(bufforForLines[:6]))
                bufforForLines = bufforForLines[6:]
                
            elif(bufforForLines[3] == "DIV" or bufforForLines[3] == "DIVFT" or bufforForLines[3] == "DIVNRA"):
                bufforForLines = self.trimAdditionalFieldAndProcess(bufforForLines)
                
    def analyzeFile(self, fileName):
        readerInstance = pdfRead()
        readerInstance.createFileHandler(fileName)
        pages = readerInstance.getFileHandler().numPages
        text = ""
        for i in range(2, pages):
            text = text + readerInstance.getTextFromPage(i)
            
        self.extractActivityParagraph(text)        
        self.splitActivityParagraphIntoSeparateLines()
        self.splitLinesIntoSeparateReports()
            
        
        
                
            


        
        

readerInstance = pdfRead()
readerInstance.createFileHandler("Dec2019.pdf")
textPage3 = readerInstance.getTextFromPage(3)
textPage4 = readerInstance.getTextFromPage(4)
textPage5 = readerInstance.getTextFromPage(5)
text = textPage3 + textPage4 + textPage5




parserInstance = pdfParser(list())


#parserInstance.extractActivityParagraph(text)
        
#parserInstance.splitActivityParagraphIntoSeparateLines()

#parserInstance.splitLinesIntoSeparateReports()


class TestingClass(unittest.TestCase):
  

    def test_numberOfRecords1(self):
        inputString = "HOLDINGS\nACTIVITY\nTrade Date\nSettle Date\nCurrency\nActivity Type\nSymbol / Description\nQuantity\nPrice\nAmount\n01/02/2020\n01/02/2020\nUSD\nCSD\nCash Receipt - Wallet (USD)\n(2.04)\n01/06/2020\n01/08/2020\nUSD\nBUY\nVZ - VERIZON COMMUNICATIONS INC COM - TRD VZ B 3 at 60.45 Agency.\n3\n60.45\n(181.35)\n01/08/2020\n01/08/2020\nUSD\nCDEP\nCash Disbursement - Wallet (USD)\n181.35\nSWEEP"
        parserInstance = pdfParser(list())
        parserInstance.extractActivityParagraph(inputString)
        parserInstance.splitActivityParagraphIntoSeparateLines()
        parserInstance.splitLinesIntoSeparateReports()
        
        self.assertEqual(len(parserInstance.listOfRecords), 3)
        
    def test_numberOfRecords2(self):
        inputString = "Revolut Trading Ltd\nACTIVITY\nTrade Date\nSettle Date\nCurrency\nActivity Type\nSymbol / Description\nQuantity\nPrice\nAmount\n12/02/2019\n12/04/2019\nUSD\nBUY\nDUK - DUKE ENERGY CORP NEW   COM NEW - TRD DUK B 2 at 87.56 Agency.\n2\n87.56\n(175.12)\n12/09/2019\n12/09/2019\nUSD\nDIV\nTM - TOYOTA MOTOR CORP   SP ADR REP2COM - DIV:TM(2.0396/sh):TAXCD:\n0\n0.00\n2.04\n12/09/2019\n12/09/2019\nUSD\nDIVFT\nTM - TOYOTA MOTOR CORP   SP ADR REP2COM - DIVFT:TM(2.0396/sh):Withhold\n tax @ 0.2\n0\n0.00\n(0.51)\n12/16/2019\n12/16/2019\nUSD\nDIVNRA\nKO - COCA COLA CO    COM - DIVNRA:KO(0.4000/sh):NRA withholding @15.00%\n0\n0.00\n(0.30)\n12/31/2019\n12/31/2019\nUSD\nDIVNRA\nCCI - CROWN CASTLE INTL CORP NEW COM - DIVNRA:CCI(1.2000/sh):NRA \nwithholding @15.\n0\n0.00\n(0.36)\nSWEEP ACTIVITY"
        parserInstance = pdfParser(list())
        parserInstance.extractActivityParagraph(inputString)
        parserInstance.splitActivityParagraphIntoSeparateLines()
        parserInstance.splitLinesIntoSeparateReports()
        
        self.assertEqual(len(parserInstance.listOfRecords), 5)
        
    def test_completeScenario(self):
        inputFile = "Dec2019.pdf"
        parserInstance = pdfParser(list())
        parserInstance.analyzeFile(inputFile)
        self.assertEqual(len(parserInstance.listOfRecords), 14)
        

if(testuj):
    suite = unittest.TestLoader().loadTestsFromTestCase(TestingClass)
    unittest.TextTestRunner(verbosity=2).run(suite)


