import plotly.express as px
import csv
import numpy as np

def getGraph(data):
    with open(data) as file:
        graph = csv.DictReader(file)
        figure = px.scatter(graph,x="Days Present", y="Marks In Percentage")
        figure.show()

def getDataSource(data):
    marks= []
    days= []
    with open(data) as file:
        read = csv.DictReader(file)
        for row in read:
            marks.append(float(row["Marks In Percentage"]))
            days.append(float(row["Days Present"]))

    return {"x" : days, "y": marks}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Marks in percentage and Days present :-",correlation[0,1])

def final():
    data  = "Student Marks vs Days Present.csv"

    datasource = getDataSource(data)
    findCorrelation(datasource)
    getGraph(data)

final()
