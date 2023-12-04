

# Logging : It is used for saving logs of servers

# logging levels : by default it is set for WARNING

# importing module
import logging

# create and configure logger

# logging.basicConfig(filename="DAY_23/newfile.log",format="%(asctime)s : %(message)s",filemode="w")

# # creating ana object

# logger = logging.getLogger()

# # setting the threshold of logger to DEBUG
# logger.setLevel(logging.DEBUG)

# # test messages
# logger.debug("Debug message")
# logger.info("Just an information")
# logger.warning("Remove white spaces")
# logger.error("Divide by zero")
# logger.critical("Server down")


# --------------------------------------------------------------------------------------------------

# DEBUG : Detailed information, typically of interest only when diagnosing problems.

# INFO : Confirmation that things are working as expected.

# WARNING : An indication that something unexpected happened or indicative of some problem in the near future (e.g. 'disk space low')
# The software is still working as expected.

# ERROR : Due to a more serious problem, the software has not been able to perform some function.

# CRITICAL : A serious error, indicating that the program itself may be unable to continue running.

# ------------------------------------------------------------------------------------------------------

# Program 1 :

# we can setlevel in basicConfig too.

# by default filemode is in append mode
# logging.basicConfig(filename="DAY_23/newfile.log",level=logging.DEBUG,format="%(asctime)s : %(levelname)s : %(message)s",filemode="w")

# def add(x,y):
#     """Add function"""
#     return x + y

# def sub(x,y):
#     """Subtract function"""
#     return x - y

# def mul(x,y):
#     """Multiplication function"""
#     return x * y

# def div(x,y):
#     """Division function"""
#     return x // y

# num1 = 10
# num2 = 2

# add_result = add(num1,num2)
# logging.debug('Addition: {} + {} = {}'.format(num1,num2,add_result))

# sub_result = sub(num1,num2)
# logging.debug('Subtraction: {} - {} = {}'.format(num1,num2,sub_result))

# mul_result = mul(num1,num2)
# logging.debug('Multiplication: {} * {} = {}'.format(num1,num2,mul_result))

# div_result = div(num1,num2)
# logging.debug('Division: {} / {} = {}'.format(num1,num2,div_result))

# -----------------------------------------------------------------------------------------------

# Program 2 :

logging.basicConfig(filename="DAY_23/newfile.log", level=logging.INFO,
                    format="%(asctime)s : %(levelname)s : %(message)s", filemode="w")


class Employee:

    """
    A sample employee class
    """

    def __init__(self, first, last) -> None:
        self.first = first
        self.last = last

        logging.info('Created Employee : {} - {}'.format(self.fullname,(self.email).lower()))

    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first,self.last)

    def logged_in(self):
        logging.info('Logged In : {} - {}'.format(self.fullname,(self.email).lower()))

    def logged_off(self):
        logging.info('Logged Off : {} - {}'.format(self.fullname,(self.email).lower()))


emp1 = Employee("Ashish","Khedekar")
emp1.logged_in()
emp2 = Employee("Shivani","Kale")
emp2.logged_in()
emp2.logged_off()
emp1.logged_off()

