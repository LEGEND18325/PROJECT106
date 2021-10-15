import plotly.express as px
import csv
import numpy as np

def getGraph(data):
    with open(data) as file:
        graph = csv.DictReader(file)
        figure = px.scatter(graph,x="sleep in hours", y="Coffee in ml")
        figure.show()

def getDataSource(data):
    hours= []
    coffee= []
    with open(data) as file:
        read = csv.DictReader(file)
        for row in read:
            hours.append(float(row["sleep in hours"]))
            coffee.append(float(row["Coffee in ml"]))

    return {"x" : hours, "y": coffee}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Marks in percentage and Days present :-",correlation[0,1])

def final():
    data  = "cups of coffee vs hours of sleep.csv"

    datasource = getDataSource(data)
    findCorrelation(datasource)
    getGraph(data)

final()
