import csv
import json

class DataRecord:
    
    def __init__(self, mes, a_code, number, compensation, amount):
        self.message = mes
        self.airline_code = a_code
        self.number_of_fellow_passengers = number
        self.did_receive_compensation = compensation
        self.total_compensation_amount = amount

class CsvFileReader:
    data = []
    
    def __init__(self, filename):
        self.filename = filename

    def str2bool(self, value):
        return value.lower() == "true"
        
    def to_list(self):
        with open(self.filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for i, row in enumerate(reader):
                if i==0: continue
                self.data.append(DataRecord(row[0],row[1],int(row[2]),self.str2bool(row[3]), float(row[4])))
        return self.data

class JsonFileReader:
    data = []
    
    def __init__(self, filename):
        self.filename = filename
        
    def to_list(self):
        with open(self.filename, 'r') as jsonfile:
            reader = json.load(jsonfile)
            for row in reader:
                self.data.append(DataRecord(row["message"],row["airline_code"],row["number_of_fellow_passenger"],row["did_receive_compensation"],row["total_compensation_amount"]))
            return self.data


