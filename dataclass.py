"""
    A dataclass is a class that is designed to only hold data values.They are typically used to 
    store information that will be passed between different parts of a program or a system.
"""
from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int
    grade: str
    marks: int

studentOne = Student('Jabari Maina', 7, 'Grade 5', 470)
