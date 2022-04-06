#!/usr/bin/env python3

from audioop import add


class Student(object):
    """ A python obj for retrieving student in school"""
    def __init__(self, name, address, age):
        self.name = name
        self.address = address
        self.age = age
    def returnName(self):
        """ return name of student"""
        return self.name
    def returnAddress(self) -> str:
        """ return address of student"""
        return self.address
    def returnAge(self):
        """ return age of student"""
        return self.age
    def updateAddress(self, address):
        """ update address of student"""
        self.address = address
        return self.address
    


student1 = Student("xman", "BirdmingHarm", 40)

print(student1.returnAddress())

student1.updateAddress("WickedShit")

print(student1.returnAddress())
