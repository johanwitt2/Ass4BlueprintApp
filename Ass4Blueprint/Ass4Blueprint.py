import pyodbc
from Ass4Class import *

print("What do you want to do? (A, B, C OR D)")
print("A- diplay all, B- display growth, C- display by date or D- range of dates")

choice = input()

def connect_to_db():
    pass



if (choice == 'A'):

    print_all_records()

elif (choice == 'B'):

    print_positive_growth()

elif (choice == 'C'):

    record_by_date()

else: count_companies_between_dates()



