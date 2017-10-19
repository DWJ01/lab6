#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 18:15:39 2017

@author: duanwujie
"""

class Employee:
    def __init__(self, name, idnumber, department, jobtitle):
        self.Name = name
        self.IDNumber = idnumber
        self.Department = department
        self.JobTitle = jobtitle

emp_1 = Employee('Susan Meyers',47899,'Accounting','Vice President')
emp_2 = Employee('Mark Jones',39119,'IT','Programmer')
emp_3 = Employee('Joy Rogers',81774,'Manufacturing','Engineer')

print(emp_1.__dict__, emp_2.__dict__, emp_3.__dict__)
