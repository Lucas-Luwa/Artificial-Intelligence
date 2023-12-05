import Testing

#No hidden Layer
myXorData = []
for j in range (0, 60, 1):
    intermediateContainer = []
    for i in range(5):
        intermediateContainer.append(Testing.testXorData([j])[1])
    myXorData.append(intermediateContainer)

print("Raw Xor Data")
print(myXorData)
print("")

for i in range (len(myXorData)):
    print(i, " Average: ", Testing.average(myXorData[i]), " Standard Deviation: ", Testing.stDeviation(myXorData[i]), " MAX: ", max(myXorData[i]))