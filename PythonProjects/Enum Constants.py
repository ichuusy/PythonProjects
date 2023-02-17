from enum import Enum # Importing modules for Enumeration

days = Enum("Days",["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]) # Enum Constant and included items in list are set the enum.
print(f"First day of week : {days.Sunday.name} and {days.Monday.value} days is {days.Monday.name}") # Written the first day of week and second day of week.