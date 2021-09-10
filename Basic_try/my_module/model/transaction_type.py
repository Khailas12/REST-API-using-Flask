from enum import Enum

class TransactionType(Enum):
    INCOME = "INCOME"
    EXPENSE = "EXPENSE"
    
    
# It's a class in python for creating enumerations, which are a set of symbolic names (members) bound to unique, constant values. The enums are evaluatable string representation of an object also called repr(). The name of the enum is displayed using 'name' keyword. Using type() we can check the enum types
# Eg: Compass directions (values of NORTH, SOUTH, EAST, and WEST) and the days of the week