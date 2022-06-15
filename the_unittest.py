import unittest
from assessment2 import func,cal,middle2behind,cal_final,visualoutput_and_writeinfile,judgement,judgement2

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(middle2behind("(((2+3)*(4*5))+(1+(2+3)))"),str("23+45**123+++"))
        self.assertEqual(cal_final("23+45**123+++"),int(106))
        self.assertEqual(judgement("(((1+3)+3)"),False)#the program will print the sentence "Not a valid expression, bracket mismatched" on the terminal
        self.assertEqual(judgement("((1+2)3)"),False)#the terminal will show "Not a valid expression, operator missing."
        self.assertEqual(judgement("((3/4)*(3))"),False)#the terminal will show "Not a valid expression, wrong number of operands."
        self.assertEqual(judgement2("(1+1+1)"),False)#the terminal will show "Not a valid expression, wrong number of operands."
        self.assertEqual(judgement2("(3+2)/(1-4)"),False)#the terminal will show "Not a valid expression, brackets mismatched."


if __name__ == '__main__':
    unittest.main()
