import csv
import numpy as np
def getDataSource(data_path):
    coffeeSize=[]
    averageTime=[]
    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for i in csv_reader:
            coffeeSize.append(float(i["Coffee in ml"]))
            averageTime.append(float(i["sleep in hours"]))
        
    return{"x":coffeeSize,"y":averageTime}
def findCorr(dataSource):
    corr=np.corrcoef(dataSource["x"],dataSource["y"])
    print("Correlation between coffee drunk and sleep :- \n--->",corr[0,1])
def setUp():
    data_path="coffee-sleep.csv"
    dataSource=getDataSource(data_path)
    findCorr(dataSource)
setUp()