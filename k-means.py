import numpy as np

class KMeans:
    def __init__(self, k, max_iter=100, tol=1e-4, random_state=None):
        self.k = k
        self.max_iter = max_iter
        self.tol = tol
        self.random_state = random_state
        self.centroids = None

    def fit(self, X):
        rng = np.random.default_rng(self.random_state)
        # Randomly initialize centroids
        self.centroids = X[rng.choice(len(X), self.k, replace=False)]

        for _ in range(self.max_iter):
            # Compute distances and assign clusters
            labels = self.predict(X)
            # Update centroids
            new_centroids = np.array([X[labels == i].mean(axis=0) for i in range(self.k)])
            # Check convergence
            if np.allclose(self.centroids, new_centroids, atol=self.tol):
                break
            self.centroids = new_centroids

    def predict(self, X):
        # Assign each point to the nearest centroid
        dists = np.linalg.norm(X[:, None] - self.centroids, axis=2)
        return np.argmin(dists, axis=1)
