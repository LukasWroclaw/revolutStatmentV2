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



analyser = recordsAnalyser()
balance = analyser.analyseBalanceForTheCompany(recordList, "TM", 1, 1)


print("Final gross balance", round(balance,2))
