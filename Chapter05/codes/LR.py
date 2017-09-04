from sklearn import datasets, metrics
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

mnist = datasets.load_digits()

img_tuple = list(zip(mnist.images, mnist.target))

images = mnist.images

data_size = len(images)

#Preprocessing images
images = images.reshape(len(images), -1)
labels = mnist.target

#Initialize Logistic Regression
LR_classifier = LogisticRegression(C=0.01, penalty='l1', tol=0.01)
#Training the data on only 75% of the dataset. Rest of the 25% will be used in testing the Logistic Regression
LR_classifier.fit(images[:int((data_size / 4) * 3)], labels[:int((data_size / 4) * 3)])

#Testing the data
predictions = LR_classifier.predict(images[int((data_size / 4)):])
target = labels[int((data_size/4)):]

#Print the performance report of the Logistic Regression model that we learnt
print("Performance Report: \n %s \n" % (metrics.classification_report(target, predictions)))
