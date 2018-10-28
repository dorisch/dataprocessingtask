import sys
from deserialization import *
from file_handler import FileHandler
from data_processing import Calculator


file_info = FileHandler(sys.argv[1])

file = None

if file_info.file_ext() == ".csv":
    file = CsvFileReader(file_info.filename)
elif file_info.file_ext() == ".json":
    file = JsonFileReader(file_info.filename)
else:
    print ("Unsupported data format!")

if file == None:
    sys.exit("Unsupported data format!")

data = file.to_list()
calc = Calculator(data)
print ("Distribution of number of fellow passengers per user: {}".format(calc.distribution()))
print ("Average compensation per passenger: {}".format(calc.average_compensation()))
print ("Most popular airline is: {}".format(calc.most_popular_airline()))
print ("Percentage of users who got compensation: {}".format(calc.percet_of_passengers_with_compensation()))

