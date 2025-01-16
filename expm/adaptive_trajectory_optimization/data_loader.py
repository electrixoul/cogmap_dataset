import matplotlib.pyplot as plt
import numpy as np

# centroids_feature_space_transformed = np.load('./data/centroids_feature_space_transformed.npy')
# centroids_feature_space_transformed = np.load('./data/rnn_states_early_stable.npy')
centroids_feature_space_transformed = np.load('./data/rnn_states_early_stable_feature_space_transformed.npy')
# centroids_feature_space_transformed = np.load('./data/centroids.npy')
landscapes_np = np.load('./data/landscapes.npy')

print("centroids_feature_space_transformed.shape", centroids_feature_space_transformed.shape)
print("landscapes_np.shape", landscapes_np.shape)

def visualize(landscape_144, centroid_feature_space_transformed):

    landscape_12x12 = landscape_144.reshape(12, 12)
    # 在左边以图像的形式展示landscape_12x12，右边以曲线的形式展示centroid_feature_space_transformed
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(landscape_12x12, cmap='hot', interpolation='nearest')
    plt.colorbar()
    plt.subplot(1, 2, 2)
    plt.plot(centroid_feature_space_transformed)
    plt.show()

for i in range(landscapes_np.shape[0]):
    visualize(landscapes_np[i], centroids_feature_space_transformed[i])
    print("landscapes_np[i]", landscapes_np[i])
    print("centroids_feature_space_transformed[i]", centroids_feature_space_transformed[i])
    


