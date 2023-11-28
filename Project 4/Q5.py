import Testing
print("Running Testing")

# print(Testing.testPenData()[1])
myPenData = []
for i in range(5):
    myPenData.append(Testing.testPenData()[1])

myCarData = []
for i in range(5):
    myCarData.append(Testing.testCarData()[1])

print(myPenData)
print("The average of the pen data is: ", Testing.average(myPenData), " and the standard deviation of the data is ", Testing.stDeviation(myPenData))
print("The max is: ", max(myPenData))
print("------------------------------------")
print(myCarData)
print("The average of the car data is: ", Testing.average(myCarData), " and the standard deviation of the data is ", Testing.stDeviation(myCarData))
print("The max is: ", max(myCarData))

