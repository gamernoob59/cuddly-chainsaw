import csv
import numpy as np
def getDataSource(data_path):
    grade=[]
    attendance=[]
    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for i in csv_reader:
            grade.append(float(i["Marks In Percentage"]))
            attendance.append(float(i["Days Present"]))
        
    return{"x":grade,"y":attendance}
def findCorr(dataSource):
    corr=np.corrcoef(dataSource["x"],dataSource["y"])
    print("Correlation between attendance and grades :- \n--->",corr[0,1])
def setUp():
    data_path="grades-attendance.csv"
    dataSource=getDataSource(data_path)
    findCorr(dataSource)
setUp()