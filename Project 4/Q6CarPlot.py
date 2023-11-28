import matplotlib.pyplot as plt

penArr = [0.0, 0.8439679817038307, 0.891538021726701, 0.9016580903373356, 0.9071469411092054, 0.9058319039451115, 0.9002287021154946, 0.9034305317324186, 0.9002858776443683]   
carArr = [0.71, 0.967, 0.985, 0.9850000000000001, 0.9759999999999998, 0.978, 0.9869999999999999, 0.9800000000000001, 0.974]
Xaxis = [0, 5, 10, 15, 20, 25, 30, 35, 40]

plt.plot(Xaxis, carArr, label='Line 1', marker='o')

plt.xlabel('Number of Hidden Layers')
plt.ylabel('Average Accuracy (CarData)')
plt.title('Average Accuracy (CarData) vs Number of Hidden Layers')


plt.show()