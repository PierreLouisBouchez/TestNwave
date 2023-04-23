from abc import ABC, abstractmethod
import json
import csv

class Serializer:
    def serializer_json(self,obj, filename):
        with open(filename, 'w') as f:
            json.dump(obj, f)
            

    def serializer_csv(self,listobj, filename):
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for obj in listobj:
                writer.writerow(obj.csv_row())