import unittest

def pipe(var, *args):
    for function in args:
        try:
            var = function(var)
        except:
            print("An exception occurred")
            return None
    return var

class pipeFunctionTest(unittest.TestCase):
    def testValueWithNumber(self):
        def increment(value):
            return value + 1 

        self.assertEqual(pipe(1234, increment, increment, increment), 1237)
        self.assertEqual(pipe(1, "increment", increment), None)
        self.assertEqual(pipe("abc", increment, increment), None)
    
    def testValueWithString(self):
        def addString(value):
            return value + "abc"

        self.assertEqual(pipe("aa", addString, addString), "aaabcabc")
        self.assertEqual(pipe(123, addString), None)

    def testPower(self):
        def power(value):
            return value*value

        self.assertEqual(pipe(2, power, power), 16)
        self.assertEqual(pipe("a", power, power), None)

    def testList(self):
        def appendList(value):
            return value + [1]

        self.assertEqual(pipe([1, 1], appendList, appendList), [1, 1, 1, 1])
if __name__ == '__main__':
    unittest.main()