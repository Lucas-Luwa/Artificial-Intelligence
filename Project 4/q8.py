import Testing
print("Running Testing")

myExtraData = []
for i in range(5):
    myExtraData.append(Testing.testExtraData()[1])

print(myExtraData)
print("The average of the extra data is: ", Testing.average(myExtraData), " and the standard deviation of the data is ", Testing.stDeviation(myExtraData))
print("The max is: ", max(myExtraData))

# import Testing

# #No hidden Layer
# myXorData = []
# for j in range (60, 100, 5):
#     intermediateContainer = []
#     # for i in range(5):
#     intermediateContainer.append(Testing.testExtraData([j])[1])
#     myXorData.append(intermediateContainer)

# print("Raw Xor Data")
# print(myXorData)
# print("")

# for i in range (len(myXorData)):
#     print(i, " Average: ", Testing.average(myXorData[i]), " Standard Deviation: ", Testing.stDeviation(myXorData[i]), " MAX: ", max(myXorData[i]))
