import numpy as np
from csvreader import CsvReader
import matplotlib.pyplot as plt
import math
import sys
import random

class KmeansClustering:
	def __init__(self, max_iter=20, ncentroid=5):
		self.ncentroid = ncentroid # number of centroids
		self.max_iter = max_iter # number of max iterations to update the centroids
		self.centroids = [] # values of the centroids

	def fit(self, X):
		"""
		Run the K-means clustering algorithm.
		For the location of the initial centroids, random pick ncentroids from the dataset.
		Args:
		-----
			X: has to be an numpy.ndarray, a matrice of dimension m * n.
		Return:
		-------
			None.
		Raises:
		-------
			This function should not raise any Exception.
		"""
		X = np.array(X, dtype=float)
		self.centroids = X[np.random.randint(0,X.shape[0],self.ncentroid)]
		for i in range(self.max_iter):		
			clusters = []
			for i in range(self.ncentroid):
				clusters.append([])
			for row in X:
				distances = ((self.centroids[:,:1] - row[:1])**2 + (self.centroids[:,1:2] - row[1:2])**2 + (self.centroids[:,2:3] - row[2:3])**2)**0.5
				indices = np.where(distances == np.min(distances))
				if indices[0].shape[0] <= 1:
					index = int(indices[0])
				else:
					index = int(indices[0][1])
				clusters[index].append(list(row))
			for centroid in range(self.ncentroid):
				m = np.mean(np.array(clusters[centroid]), axis=0)
				try:
					if not math.isnan(sum(m)):
						self.centroids[centroid] = m
				except:
					if not math.isnan(m):						
						self.centroids[centroid] = m
		self.clusters = clusters

	def predict(self, X):
		"""
		Predict from wich cluster each datapoint belongs to.
		Args:
		-----
			X: has to be an numpy.ndarray, a matrice of dimension m * n.
		Return:
		-------
			the prediction has a numpy.ndarray, a vector of dimension m * 1.
		Raises:
		-------
		This function should not raise any Exception.
		"""
		# clusters = []
		# 	for i in range(self.ncentroid):
		# 		clusters.append([])
		# for row in X:
		# 	distances = ((self.centroids[:,:1] - row[:1])**2 + (self.centroids[:,1:2] - row[1:2])**2 + (self.centroids[:,2:3] - row[2:3])**2)**0.5
		# 	indices = np.where(distances == np.min(distances))
		# 	if indices[0].shape[0] <= 1:
		# 		index = int(indices[0])
		# 	else:
		# 		index = int(indices[0][1])
		# 	clusters[index].append(list(row))
		self.clusters = clusters


def	get_colors(n):
	colors = []
	for count in range(n) :
		color = [0,0,0]
		if count < 3:
			color[count] = 1
		elif count < 6:
			color[count % 3] = 1
			color[(count + 1) % 3] = 1
		else:
			for i in range(3):
				color[i] = random.random()
		colors.append(color)

	return (colors)

def plot(km):
	fig = plt.figure()
	ax = fig.add_subplot(projection='3d')
	colors = get_colors(km.ncentroid)
	ax.scatter([float(i) for i in km.centroids[:,0]],[float(i) for i in km.centroids[:,1]],[float(i) for i in km.centroids[:,2]], c = colors, marker='x' )
	for index, cluster in enumerate(km.clusters):
		xs = [float(i) for i in np.array(cluster)[:,0]]
		ys = [float(i) for i in np.array(cluster)[:,1]]
		zs = [float(i) for i in np.array(cluster)[:,2]]
		ax.scatter(xs, ys, zs, color = colors[index])
	plt.show()


if __name__=='__main__':
	ncentroid = 5
	max_iter = 20
	filename = None
	for arg in sys.argv[1:]:
		kwarg = arg.split("=")
		if kwarg[0] not in ["ncentroid", "max_iter","filename"]:
			print("Error: bad argument name.\nValid arguments are:\n\t-ncentroid: number of centroids desired\n\t-max_iter: maximum amount of iterations allowed in order to find the kmeans cluster")
			exit()
		elif len(kwarg) != 2:
			print("Error: '",kwarg[0],"' bad usage. e.g. ",kwarg[0],"=",5,sep='')
			exit()
		elif kwarg[0] == "ncentroid":
			ncentroid = int(kwarg[1])
		elif kwarg[0] == "max_iter":
			ncentroid = int(kwarg[1])
		elif kwarg[0] == "filename":
			filename = kwarg[1]
	km = KmeansClustering(max_iter,ncentroid)
	with CsvReader(filename, skip_top=1) as file:
		if file == None:
			print("Error: File nonexistant or corrupted")
		else:
			x = np.array(file.getdata())[:,1:]
			km.fit(x)
			km.predict(x)
			plot(km)
