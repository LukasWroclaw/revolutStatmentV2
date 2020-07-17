# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 13:14:30 2020

@author: marszale
"""

from datetime import date
from pdfParse import pdfParser
from directoryHandler import directoryHandler
from recordsAnalyser import recordsAnalyser

recordList = list()

parserInstance = pdfParser(recordList)

directoryHandler = directoryHandler()

files = directoryHandler.listFilesInDirectoryWithPrefix("./dataBase")


for file in files:
    parserInstance.analyzeFile(file)

#parserInstance.analyzeFile("./dataBase/Sep2019.pdf")
#parserInstance.analyzeFile("./dataBase/Oct2019.pdf")
#parserInstance.analyzeFile("./dataBase/Nov2019.pdf")
#parserInstance.analyzeFile("./dataBase/Dec2019.pdf")
#parserInstance.analyzeFile("./dataBase/Jan2020.pdf")
#parserInstance.analyzeFile("./dataBase/Feb2020.pdf")
#parserInstance.analyzeFile("./dataBase/Mar2020.pdf")

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
