# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 11:29:25 2020

@author: marszale
"""

import unittest
from datetime import date
testuj = 1

class recordsAnalyser:
    
    def printTransactionHistoryFunction(self, item, toPrint=1):
        if(toPrint == 1):
            print("##", "Date", item["date"], item["Symbol"], item["type"], "Amout", item["Amount"], "Quantity", item["Quantity"],"\n")
        
    def actionAnalyser(self,item, toPrint):
        balanceTransaction = 0
        balanceDividend = 0
        
        if(item["type"] == "BUY"):
            balanceTransaction = balanceTransaction - item["Amount"]
            self.printTransactionHistoryFunction(item,toPrint)
        elif(item["type"] == "SELL"):
            balanceTransaction = balanceTransaction + item["Amount"]
            self.printTransactionHistoryFunction(item,toPrint)
        elif(item["type"] == "DIV"):
            balanceDividend = balanceDividend + item["Amount"]
            self.printTransactionHistoryFunction(item,toPrint)
        elif(item["type"] == "DIVFT"):
            balanceDividend = balanceDividend - item["Amount"]
            self.printTransactionHistoryFunction(item,toPrint)
        elif(item["type"] == "DIVNRA"):
            balanceDividend = balanceDividend - item["Amount"]
            self.printTransactionHistoryFunction(item,toPrint)
            
        return {"balanceTransaction": balanceTransaction, "balanceDividend": balanceDividend}
        
        
    
    def analyseBalanceForTheCompany(self, recordBase, symbol, printSummary=0, printTransactionHistory=0 ,beginDate = date(2019, 1, 1), endDate = date(2030, 1, 1)):
        
        recordsForCompany = list()
        
        for element in recordBase:
            if(element["Symbol"] == symbol):
                recordsForCompany.append(element)
                
        balanceTransaction = 0
        balanceDividend = 0        
                
        for item in recordsForCompany:
            if(item["date"] >= beginDate and item["date"] <= endDate):
                resultBalance = self.actionAnalyser(item, printTransactionHistory)
                balanceTransaction = balanceTransaction + resultBalance["balanceTransaction"]
                balanceDividend = balanceDividend + resultBalance["balanceDividend"]
                                
        if(printSummary):
            print("Balance for company", symbol, "transaction balance", round(balanceTransaction,2), "dividend balance", round(balanceDividend,2), "total balance", round(balanceTransaction + balanceDividend,2))
            
        return balanceTransaction + balanceDividend
    
    def analizeCompleteBalanceForSpecificPeriod(self, recordBase, printSummary=0, printTransactionHistory=0 ,beginDate = date(2019, 1, 1), endDate = date(2030, 1, 1)):
        
        recordsForCompany = recordBase
                       
        balanceTransaction = 0
        balanceDividend = 0        
                
        for item in recordsForCompany:
            if(item["date"] >= beginDate and item["date"] <= endDate):
                resultBalance = self.actionAnalyser(item, printTransactionHistory)
                balanceTransaction = balanceTransaction + resultBalance["balanceTransaction"]
                balanceDividend = balanceDividend + resultBalance["balanceDividend"]
                                
        if(printSummary):
            print("From",beginDate, "to", endDate, "Transaction balance", round(balanceTransaction,2), "dividend balance", round(balanceDividend,2), "total balance", round(balanceTransaction + balanceDividend,2))
            
        return balanceTransaction + balanceDividend


class TestingClass(unittest.TestCase):
  

    def test_analyseBalanceForTheCompany1(self):
        base = [{'date': date(2019, 9, 24), 'type': 'BUY', 'Symbol': 'TM', 'Quantity': 1.0, 'Price': 137.33, 'Amount': 137.33}, {'date': date(2019, 10, 31), 'type': 'SELL', 'Symbol': 'TM', 'Quantity': -1.0, 'Price': 138.69, 'Amount': 138.68}, {'date': date(2019, 12, 9), 'type': 'DIV', 'Symbol': 'TM', 'Quantity': 0.0, 'Price': 0.0, 'Amount': 2.04}, {'date': date(2019, 12, 9), 'type': 'DIVFT', 'Symbol': 'TM', 'Quantity': 0.0, 'Price': 0.0, 'Amount': 0.51}]
        analyser = recordsAnalyser()
        balance = analyser.analyseBalanceForTheCompany(base, "TM", 0)
        self.assertEqual(round(balance, 1), round(2.88, 1))
        
    def test_analyseBalanceForTheCompany2(self):
        base = [{'date': date(2019, 9, 24), 'type': 'BUY', 'Symbol': 'TM', 'Quantity': 1.0, 'Price': 137.33, 'Amount': 137.33}, {'date': date(2019, 10, 31), 'type': 'SELL', 'Symbol': 'TM', 'Quantity': -1.0, 'Price': 138.69, 'Amount': 138.68}, {'date': date(2019, 12, 9), 'type': 'DIV', 'Symbol': 'TM', 'Quantity': 0.0, 'Price': 0.0, 'Amount': 2.04}, {'date': date(2019, 12, 9), 'type': 'DIVFT', 'Symbol': 'TM', 'Quantity': 0.0, 'Price': 0.0, 'Amount': 0.51}]
        analyser = recordsAnalyser()
        balance = analyser.analyseBalanceForTheCompany(base, "TM", 0, 0, date(2019, 9, 1), date(2019, 11, 1))
        self.assertEqual(round(balance, 1), round(1.34, 1))
        
    def test_analizeCompleteBalanceForSpecificPeriod1(self):
        base = [{'date': date(2019, 9, 24), 'type': 'BUY', 'Symbol': 'TM', 'Quantity': 1.0, 'Price': 137.33, 'Amount': 137.33}, {'date': date(2019, 10, 31), 'type': 'SELL', 'Symbol': 'TM', 'Quantity': -1.0, 'Price': 138.69, 'Amount': 138.68}, {'date': date(2019, 9, 24), 'type': 'BUY', 'Symbol': 'QCOM', 'Quantity': 1.0, 'Price': 137.33, 'Amount': 137.33}, {'date': date(2019, 10, 31), 'type': 'SELL', 'Symbol': 'QCOM', 'Quantity': -1.0, 'Price': 138.69, 'Amount': 138.68},{'date': date(2019, 12, 9), 'type': 'DIV', 'Symbol': 'TM', 'Quantity': 0.0, 'Price': 0.0, 'Amount': 2.04}, {'date': date(2019, 12, 9), 'type': 'DIVFT', 'Symbol': 'TM', 'Quantity': 0.0, 'Price': 0.0, 'Amount': 0.51}]
        analyser = recordsAnalyser()
        balance = analyser.analizeCompleteBalanceForSpecificPeriod(base, 1, 1, date(2019, 9, 1), date(2019, 11, 1))
        self.assertEqual(round(balance, 1), round(2.72, 1))
        

if(testuj):
    suite = unittest.TestLoader().loadTestsFromTestCase(TestingClass)
    unittest.TextTestRunner(verbosity=2).run(suite)