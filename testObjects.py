#! /usr/bin/python

class testPrototype:
    def __init__(self, args):
        print 'init not implemented'
    
    # update with the new value
    def update(self, newData, args):
        print 'update not implemented'

    # display the result of the test
    def display(self, args):
        print 'display not implemented'

    # Result = true for pass or false for failed
    def result(self, args):
        print 'result not implemented'
        return True

class test1(testPrototype):
    def __init__(self, args):
        self.counter = 0
	print args

    def update(self, newData, args):
        self.counter += 1

    def display(self, args):
        self.method1()
        print self.counter

    def method1(self):
        # another helper method can be defined if needed
        print 'method1'

    def method2(self):
        print 'method2'

    def result(self, args):
        return self.counter > 10


        
    
