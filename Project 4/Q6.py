import Testing
print("Running Testing")

# print(Testing.testPenData()[1])
myPenData = []
for j in range (0, 45, 5):
    intermediateContainer = []
    for i in range(5):
        intermediateContainer.append(Testing.testPenData([j])[1])
    myPenData.append(intermediateContainer)



myCarData = []
for j in range (0, 45, 5):
    intermediateContainer2 = []
    for i in range(5):
        intermediateContainer2.append(Testing.testCarData([j])[1])
    myCarData.append(intermediateContainer2)

# print(myCarData)

print("Raw Pen Data")
print(myPenData)
print("")
print("Raw Car Data")
print(myCarData)
print("----------------------------------------------------------------")
graphPenArr = []
graphCarArr = []
XAxis = []
for i in range (len(myPenData)):
    graphPenArr.append(Testing.average(myPenData[i]))
    XAxis.append(i * 5)
    print(i*5, " Average: ", Testing.average(myPenData[i]), " Standard Deviation: ", Testing.stDeviation(myPenData[i]), " MAX: ", max(myPenData[i]))
print("----------------------------------------------------------------")


for i in range (len(myCarData)):
    graphCarArr.append(Testing.average(myCarData[i]))
    print(i*5, " Average: ", Testing.average(myCarData[i]), " Standard Deviation: ", Testing.stDeviation(myCarData[i]), " MAX: ", max(myCarData[i]))
print("----------------------------------------------------------------")
print(graphPenArr)
print(graphCarArr)
print(XAxis)