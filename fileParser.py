#! /usr/bin/python

"""
This Program is a file parser using regex
Create a test object in testObjects.py and xml code in the tests.xml
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""

import testObjects
from testObjects import *
import re
from xml.etree import ElementTree as ET

class testInfo:
    def __init__(self, name, function, regex, argsList):
        self.name = name
        self.function = function
        self.regex = regex
        self.argsList = argsList

class FileParser:
    def __init__(self, dataInputFile, parserTestFile = 'tests.xml'):
        self.testList = [];
        # read in all tests
        tree = ET.parse(parserTestFile)
        tests = tree.getroot()
        for test in tests:
            name = test.attrib.pop('name')
            function = test.find('function').text.strip()
            regex = test.find('regex').text.strip()
            argsList = test.find('arguments').text
            argsList = argsList.split('\n')
            newList = []
            for argument in argsList:
                argument = argument.strip()
                if(len(argument) > 0):
                    newList.append(argument)
            newTest = testInfo(name, function, regex, newList)
            self.testList.append(newTest)
        # open data file
        self.fileHandle = open(dataInputFile)

    def runTest(self, testInfoObj):
        print 'Running test ' + testInfoObj.name
        testClass = getattr(testObjects, testInfoObj.function)
        test = testClass(testInfoObj.argsList)
        # go to start of file
        self.fileHandle.seek(0,0)
        data = self.fileHandle.readlines()
        regex = re.compile(testInfoObj.regex)
        # read in data from dataInputFile and apply regex
        for line in data:
            matches = regex.findall(line)
            if matches:
                test.update(matches, testInfoObj.argsList)
        # when no more data to input
        test.display(testInfoObj.argsList)
        return test.result(testInfoObj.argsList)
    
    def runAllTests(self):
        # for all test names
        for test in self.testList:
            if not self.runTest(test):
                print 'Test \'' + test.name + '\' Failed'
                return False
            else:
                print 'Test \'' + test.name + '\' Passed'                
        return True


def test():
    myParser = FileParser('vp680_fmc168_test_PDWs.out')
    myParser.runAllTests()

if __name__ == '__main__':
    test()
