# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 11:29:25 2020

@author: marszale
"""

import unittest
from datetime import date
testuj = 0

class recordsAnalyser:
    
    def analyseBalanceForTheCompany(self, recordBase, symbol, printSummary):
        
        recordsForCompany = list()
        
        for element in recordBase:
            if(element["Symbol"] == symbol):
                recordsForCompany.append(element)
                
        balanceTransaction = 0
        balanceDividend = 0        
                
        for item in recordsForCompany:
            if(item["type"] == "BUY"):
                balanceTransaction = balanceTransaction - item["Amount"]
            elif(item["type"] == "SELL"):
                balanceTransaction = balanceTransaction + item["Amount"]
            elif(item["type"] == "DIV"):
                balanceDividend = balanceDividend + item["Amount"]
            elif(item["type"] == "DIVFT"):
                balanceDividend = balanceDividend - item["Amount"]
            elif(item["type"] == "DIVNRA"):
                balanceDividend = balanceDividend - item["Amount"]
                
        if(printSummary):
            print("Balance for company", symbol, "transaction balance", round(balanceTransaction,2), "dividend balance", round(balanceDividend,2), "total balance", round(balanceTransaction + balanceDividend,2))
            
        return balanceTransaction + balanceDividend


class TestingClass(unittest.TestCase):
  

    def test_numberOfRecords1(self):
        base = [{'date': date(2019, 9, 24), 'type': 'BUY', 'Symbol': 'TM', 'Quantity': 1.0, 'Price': 137.33, 'Amount': 137.33}, {'date': date(2019, 10, 31), 'type': 'SELL', 'Symbol': 'TM', 'Quantity': -1.0, 'Price': 138.69, 'Amount': 138.68}, {'date': date(2019, 12, 9), 'type': 'DIV', 'Symbol': 'TM', 'Quantity': 0.0, 'Price': 0.0, 'Amount': 2.04}, {'date': date(2019, 12, 9), 'type': 'DIVFT', 'Symbol': 'TM', 'Quantity': 0.0, 'Price': 0.0, 'Amount': 0.51}]
        analyser = recordsAnalyser()
        balance = analyser.analyseBalanceForTheCompany(base, "TM", 1)
        self.assertEqual(round(balance, 1), round(2.88, 1))
        

        

if(testuj):
    suite = unittest.TestLoader().loadTestsFromTestCase(TestingClass)
    unittest.TextTestRunner(verbosity=2).run(suite)