'''
Created on Nov 21, 2016

@author: Arthur
'''
from examples.ex25_studentManagement.domain.Exceptions import StudentManagerException

class StudentNotFoundException(StudentManagerException):
    def __init__(self):
        pass