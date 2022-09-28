import numpy as np

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
        # clusters =[]
        # print(X[:,:1].dtype)
        # print(X[:,:2].dtype)
        clusters = np.empty((self.ncentroid,1,3))
        print(clusters.shape)
        print(clusters)
        for row in X:
            distances = ((self.centroids[:,:1] - row[:1])**2 + (self.centroids[:,1:2] - row[1:2])**2 + (self.centroids[:,2:3] - row[2:3])**2)**0.5
            index = np.where(distances == np.min(distances))[0]     
            # clusters = np.append(clusters[0,index],row)
            # print(row)


        # print(self.centroids)
        # print(X)

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

