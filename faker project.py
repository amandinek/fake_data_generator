import pandas as pd
import csv
import random
from time import time
from decimal import Decimal
from faker import Faker
import numpy as np
import pandas as pd
from numpy.random import randn

RECORD_COUNT=100
fake = Faker()

def create_csv_file():
    with open('../fake data/lawyers.csv', 'w', newline='') as csvfile:
        fieldnames = ['id','name','rating', 'rate($/hour)', 'averageResponseTime(days)','experience(years)','specialisation']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for i in range(RECORD_COUNT):
            writer.writerow(
                {   
                    'name':fake.name(),               
                    'rating':fake.random_int(min=7,max=9),
                    'rate($/hour)': fake.random_int(min=500,max=2000),
                    'averageResponseTime(days)': fake.random_int(min=1, max=30),
                    'experience(years)': fake.random_int(min=1, max=15),
                    'specialisation': fake.random_int(min=1, max=15)                
                                   
                    
                }
            )
if __name__ == '__main__':
    start = time()
    create_csv_file()
    elapsed = time() - start
    print('created csv file time: {}'.format(elapsed))

    #get total emails




df= pd.read_csv("../fake data/lawyers.csv")
  
data= ['criminal','insurance','agriculture','security','theft','medical','disaster','accidents']
df['specialisation']=df.specialisation.map(lambda x: data[x%8])        

print(df)


df.to_csv("lawyers.csv")