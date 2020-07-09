# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 13:14:30 2020

@author: marszale
"""


from pdfParse import pdfParser
from recordsAnalyser import recordsAnalyser

recordList = list()

parserInstance = pdfParser(recordList)
parserInstance.analyzeFile("Sep2019.pdf")
parserInstance.analyzeFile("Oct2019.pdf")
parserInstance.analyzeFile("Nov2019.pdf")
parserInstance.analyzeFile("Dec2019.pdf")
parserInstance.analyzeFile("Jan2020.pdf")
parserInstance.analyzeFile("Feb2020.pdf")
parserInstance.analyzeFile("Mar2020.pdf")

analyser = recordsAnalyser()
balance = analyser.analyseBalanceForTheCompany(recordList, "TM", 1)
#balance = balance + analyser.analyseBalanceForTheCompany(recordList, "VZ", 1)
balance = balance + analyser.analyseBalanceForTheCompany(recordList, "T", 1)
balance = balance + analyser.analyseBalanceForTheCompany(recordList, "KO", 1)
balance = balance + analyser.analyseBalanceForTheCompany(recordList, "CCI", 1)
balance = balance + analyser.analyseBalanceForTheCompany(recordList, "DUK", 1)
balance = balance + analyser.analyseBalanceForTheCompany(recordList, "ABBV", 1)
#balance = balance + analyser.analyseBalanceForTheCompany(recordList, "LMT", 1)
balance = balance + analyser.analyseBalanceForTheCompany(recordList, "STX", 1)

print("Final gross balance", round(balance,2))
