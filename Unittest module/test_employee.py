from employee import Employee
import unittest

class TestEmployee(unittest.TestCase):
    
    def test_mail(self):
        emp_1 = Employee('Corey', 'Schafer', 50000)
        emp_2 = Employee('Sue', 'Smith', 60000)
        