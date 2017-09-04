from sklearn.datasets import fetch_mldata
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import normalize
from sklearn.model_selection import train_test_split

#Get MNIST Dataset
print('Getting MNIST Data...')
mnist = fetch_mldata('MNIST original')
print('MNIST Data downloaded!')

images = mnist.data 
labels = mnist.target 

#Preprocess the images 
images = normalize(images, norm='l2') #You can use l1 norm too

#Split the data into training set and test set
images_train, images_test, labels_train, labels_test = train_test_split(images, labels, test_size=0.25, random_state=17)

#Setup the neural network that we want to train on 
nn = MLPClassifier(hidden_layer_sizes=(200), max_iter=20, solver='sgd', learning_rate_init=0.001, verbose=True)

#Start training the network 
print('NN Training started...')
nn.fit(images_train, labels_train)
print('NN Training completed!')

#Evaluate the performance of the neural network on test data 
print('Network Performance: %f' % nn.score(images_test, labels_test))
