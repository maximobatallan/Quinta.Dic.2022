import pandas as pd
import csv 
from datetime import datetime

lista = ['mica', 'simik', 'pablo']

df= pd.read_csv('Quinta.csv',sep=',')




# Sample class with init method
class Person:
 
    # init method or constructor
    def __init__(self, name, descripcion, precio):
        self.name = name
        self.descripcion = descripcion
        self.precio = precio
    # Sample Method
    def say_hi(self):
        now = datetime.now()
        now = now.date()
        list = [now,self.name, self.descripcion, self.precio]
        #print(list)
#        df.to_csv("Quinta.csv")
        
        with open('Quinta.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(list)








