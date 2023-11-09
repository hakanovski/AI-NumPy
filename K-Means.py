import numpy as np

def k_means_clustering(X, k, max_iters=100):
    centroids = X[np.random.choice(X.shape[0], k, replace=False)]
    for _ in range(max_iters):
        clusters = [np.argmin(np.linalg.norm(x - centroids, axis=1)) for x in X]
        new_centroids = np.array([X[np.array(clusters) == i].mean(axis=0) for i in range(k)])
        if np.all(centroids == new_centroids):
            break
        centroids = new_centroids
    return clusters, centroids

# Example usage with random data
X = np.random.rand(100, 2)
clusters, centroids = k_means_clustering(X, k=3)
