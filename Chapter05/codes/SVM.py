from sklearn import datasets, metrics, svm

mnist = datasets.load_digits()

images = mnist.images

data_size = len(images)

#Preprocessing images
images = images.reshape(len(images), -1)
labels = mnist.target

#Initialize Logistic Regression
SVM_classifier = svm.SVC(gamma=0.001)
#Training the data on only 75% of the dataset. Rest of the 25% will be used in testing the Logistic Regression
SVM_classifier.fit(images[:int((data_size / 4) * 3)], labels[:int((data_size / 4) * 3)])

#Testing the data
predictions = SVM_classifier.predict(images[int((data_size / 4)):])
target = labels[int((data_size/4)):]

#Print the performance report of the Logistic Regression model that we learnt
print("Performance Report: \n %s \n" % (metrics.classification_report(target, predictions)))
