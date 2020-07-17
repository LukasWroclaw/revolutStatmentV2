# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 15:14:36 2020

@author: marszale

"""
import os
import unittest
testuj = 0


class directoryHandler:
    
    def listFilesInDicectory(self, directory):
        return os.listdir( directory )
    
    
    def listFilesInDirectoryWithPrefix(self, directory):
        files = os.listdir( directory )
        filesWithPrefix = []
        
        for file in files:
            filesWithPrefix.append(directory + "/" + file)
            
        return filesWithPrefix
        
        
    
    
class TestingClass(unittest.TestCase):
  


 

    def test_filesInDirectory(self):
        handler = directoryHandler()
        files = handler.listFilesInDicectory("./testDataBase")
        self.assertEqual(files, ["test1.pdf", "test2.pdf"])
        
    def test_filesInDirectoryWithPrefix(self):
        handler = directoryHandler()
        files = handler.listFilesInDirectoryWithPrefix("./testDataBase")
        self.assertEqual(files, ["./testDataBase/test1.pdf", "./testDataBase/test2.pdf"])
        


if(testuj):
    suite = unittest.TestLoader().loadTestsFromTestCase(TestingClass)
    unittest.TextTestRunner(verbosity=2).run(suite)
    
    
    
    
    
    
    
