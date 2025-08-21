import numpy as np

def kmeans(X, k, max_iter=100):
    # Randomly choose k initial centroids from data
    centroids = X[np.random.choice(len(X), k, replace=False)]
    
    for _ in range(max_iter):
        # Assign points to nearest centroid
        labels = np.argmin(((X[:, None] - centroids)**2).sum(axis=2), axis=1)
        # Compute new centroids
        new_centroids = np.array([X[labels == i].mean(axis=0) for i in range(k)])
        # Stop if converged
        if np.allclose(centroids, new_centroids): break
        centroids = new_centroids
    
    return centroids, labels

X = np.random.rand(100, 2)  # 100 2D points
centroids, labels = kmeans(X, k=3)
print(X)
print(centroids)
print(labels)
