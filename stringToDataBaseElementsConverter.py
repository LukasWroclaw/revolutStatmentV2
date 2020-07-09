# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 10:18:19 2020

@author: marszale
"""

import unittest
from datetime import date
testuj = 0

class stringToDataBaseElementsConverter:
    
    def convertDate(self, inputString):
        splitted = inputString.split("/")
        return date(int(splitted[2]), int(splitted[0]), int(splitted[1]))
    
    def extractSymbol(self, inputString):
        splitted = inputString.split(" - ")
        return splitted[0]
    
    def trimBrackets(self, inputString):
        
        if(inputString[0] == "("):
            inputString = inputString[1:-1]
            
        return float(inputString)
    
    def convertTransaction(self, inputList):
        record = {}
        record["date"] = self.convertDate(inputList[0])
        record["type"] = inputList[3]
        record["Symbol"] = self.extractSymbol(inputList[4])
        record["Quantity"] = float(inputList[5])
        record["Price"] = float(inputList[6])
        record["Amount"] = self.trimBrackets(inputList[7])
        return record
    
    def convertWalletAction(self, inputList):
        record = {}
        record["date"] = self.convertDate(inputList[0])
        record["type"] = inputList[3]
        record["Symbol"] = self.extractSymbol(inputList[4])
        record["Amount"] = self.trimBrackets(inputList[5])
        return record
        







class TestingClass(unittest.TestCase):
  

    def test_convertTransaction(self):
        inputList = ['01/06/2020', '01/08/2020', 'USD', 'BUY', 'VZ - VERIZON COMMUNICATIONS INC COM - TRD VZ B 3 at 60.45 Agency.', '3', '60.45', '(181.35)']
        converter = stringToDataBaseElementsConverter()
        record = converter.convertTransaction(inputList)
        expectedRecord = {"date": date(2020, 1, 6), "type": "BUY", "Symbol": "VZ", "Quantity": 3, "Price": 60.45, "Amount": 181.35}
        self.assertEqual(record, expectedRecord)
        
    def test_convertDivTransaction(self):
        inputList = ['12/09/2019', '12/09/2019', 'USD', 'DIV', 'TM - TOYOTA MOTOR CORP   SP ADR REP2COM - DIV:TM(2.0396/sh):TAXCD:', '0', '0.00', '2.04']
        converter = stringToDataBaseElementsConverter()
        record = converter.convertTransaction(inputList)
        expectedRecord = {"date": date(2019, 12, 9), "type": "DIV", "Symbol": "TM", "Quantity": 0, "Price": 0.00, "Amount": 2.04}
        self.assertEqual(record, expectedRecord)
        
    def test_convertWalletOperation(self):
        inputList = ['01/02/2020', '01/02/2020', 'USD', 'CSD', 'Cash Receipt - Wallet (USD)', '(2.04)']
        converter = stringToDataBaseElementsConverter()
        record = converter.convertWalletAction(inputList)
        expectedRecord = {"date": date(2020, 1, 2), "type": "CSD", "Symbol": "Cash Receipt", "Amount": 2.04}
        self.assertEqual(record, expectedRecord)
        


if(testuj):
    suite = unittest.TestLoader().loadTestsFromTestCase(TestingClass)
    unittest.TextTestRunner(verbosity=2).run(suite)