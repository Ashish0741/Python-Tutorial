
# Assert :

# Code 1 :

def test_min():
    assert min([1, 2, 3, 5]) == 1, "It should be 1"


if __name__ == "__main__":
    test_min()
    print("Everything Passed !!")


# Code 2 :

# Using assert program gets terminated if any test case fails then further test cases will not run

def test_min():
    assert min([1, 2, 3, 5]) == 1, "It should be 1"


def test_sum():
    assert sum([1, 2, 3, 5]) == 11, "It should be 11"


if __name__ == "__main__":
    test_min()
    test_sum()
    print("Everything Passed !!")

# -----------------------------------------------------------------------------------------------

# To overcome above issue we use unittest

# using unittest peforming unit testing in python :

# step 1 : import unittest module

# step 2 : define a function to be tested. In the following example, sub() function is to be subjected to test.

# step 3 : create a testcase by inheriting unittest. (TestCase)

# step 4 : define a test as a method inside the class. Name of the method must start with 'test'.

# step 5 : Each test calls assert function of TestCase class.
#          There are many types of asserts :
#                Following example calls assertEquals() function.

# step 6 : assertEquals() function compares result of sub() function with args2 argument and throws assertionError if comparison fails.

# step 7 : finally, call main() method from the unittest module.

# -----------------------------------------------------------------------

# Code 1 :

import unittest

# def sub(num1, num2):
#     return num1 - num2

# class CheckSubFunction(unittest.TestCase):
#     def test_add(self):
#         self.assertEquals(sub(10,2),8)

# if __name__ == "__main__":
#     unittest.main()

# ----------------------------------------------------------------------

# Code 2:

# class TestingSum(unittest.TestCase):
#     def test_sum(self):
#         self.assertEquals(sum([10,3,5,2]),20,"It should be 20")

#     def test_sum_tuple(self):
#         self.assertEquals(sum((10,30)),40,"It should be 40")


# if __name__ == "__main__":
#     unittest.main()


# -------------------------------------------------------------------------

# Code 3 :

# importing cube func 

# from test_cube import cube

# class TestCube(unittest.TestCase):
#     def test_cube(self):
#         num = 3
#         result = cube(num)
#         self.assertEquals(result,27,"It should be 27")

# if __name__ == "__main__":
#     unittest.main()

# -------------------------------------------------------------------------

# Code 4 :

# Skipping test cases :

# class SkippingTest(unittest.TestCase):

#     @unittest.skip("skipping method")    # Skipping decorator
#     def test_add(self):
#         self.assertEquals(10+20,30,"It should be 30")


# if __name__ == "__main__":
#     unittest.main()

# ---------------------------------------------------------------------------

# step 9 : The following three could be the possible outcomes of a test -

# OK --> test passes. 'A' is displayed on console.

# FAIL --> test does not pass, and raises an AssertionError exception. 'F' is displayed on console.

# ERROR --> test raises an exception other than AssertionError. 'E' is displayed on console.

# skipped --> test case will be skipped. 'S' is displayed on console.

# --------------------------------------------------------------------------

# TestSuite in unittest module :

# STEPS TO CREATE TESTSUIT :

# The following steps are involved in creating and running a test suite :

# 1. Create an instance of TestSuite class

# suite = unittest.TestSuite()

# 2. Add tests inside a TestCase class in the suite.

# suite.addTest(testcase class)

# 3. You can also use makeSuite() method to add tests from a class.

# suite = unittest.makeSuite(test case class)

# 4. Individual tests can also be added in the suite.

# suite.addTest(testcaseclass("testmethod"))

# 5. Create an object of the TextTestRunner class.

# runner = unittest.TextTestRunner()

# 6. Call the run() method to run all the tests in the suite.

# runner.run(suite)

# -----------------------------------------------------------------------------

# class ConfigTestCase(unittest.TestCase):
#     def setUp(self) -> None:
#         self.a = 10
#         self.b = 20

#     def test_add(self):
#         """Add"""
#         result = self.a + self.b
#         self.assertTrue(result == 30)

#     def test_sub(self):
#         """sub"""
#         result = self.a - self.b
#         self.assertTrue(result == -10)

# def suite():
#     """
#         Gather all the tests from this module in a test suite.
#     """
#     test_suite = unittest.TestSuite()
#     test_suite.addTest(unittest.makeSuite(ConfigTestCase))
#     return test_suite

# my_suite = suite()

# runner = unittest.TextTestRunner()
# runner.run(my_suite)

