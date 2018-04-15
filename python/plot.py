import pylab  
  
def loadData(flieName):  
    inFile = open(flieName, 'r')  
  
    X = []  
    y = []  
  
    for line in inFile:  
        trainingSet = line.split(',')  
        X.append(trainingSet[0])   
        y.append(trainingSet[1])   
  
    return (X, y) 

def plotData(X, y):  
    length = len(y)  
              
    pylab.figure(1)  
  
    pylab.plot(X, y, 'rx')  
    pylab.xlabel('Population of City in 10,000s')  
    pylab.ylabel('Profit in $10,000s')  
  
    pylab.show()


(X,y) = loadData('data.txt')  
  
plotData(X,y)  
