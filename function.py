import plotly.figure_factory as ff 
import plotly.graph_objects as go 
import pandas as pd 
import csv
import random
import statistics
df = pd.read_csv("data.csv")
poplist = df["id"].to_list()
fig = ff.create_distplot([poplist],["Population"])
#fig.show()
popmean = statistics.mean(poplist)
print("Population Mean {}".format(popmean))
def randomSetOfMean(counter):
    dataSet = []
    for i in range(0,counter):
        randomIndex = random.randint(0,len(poplist)-1)
        value = poplist[randomIndex]
        dataSet.append(value)
    mean = statistics.mean(dataSet)
    return mean
def showFig(meanlist):
    df = meanlist
    mean = statistics.mean(df)
    fig = ff.create_distplot([poplist],["Population"], show_hist = False)
    fig.add_trace(go.Scatter(x = [mean,mean], y = [0,1], mode = "lines", name = "Mean"))
    fig.show()
def setUp():
    mean_list = []
    for i in range(0,100):
        SetOfMean = randomSetOfMean(30)
        mean_list.append(SetOfMean)
    showFig(mean_list)
    mean = statistics.mean(mean_list)
    print("Population Sampling: ", mean)

setUp()


    
