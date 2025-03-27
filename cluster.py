import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Step 1: Load the dataset (Use the correct filename)
data = pd.read_csv("plant_breeding_data.csv")

# Step 2: Remove non-numeric columns
data_numeric = data.drop(columns=["Genotype"])  # Exclude Genotype

# Step 3: Apply KMeans Clustering
kmeans = KMeans(n_clusters=3, random_state=42)  # Set random_state for reproducibility
data["Cluster"] = kmeans.fit_predict(data_numeric)  # Assign clusters

# Step 4: Visualize Clusters (Choose two features for plotting)
plt.scatter(data_numeric["Height_cm"], data_numeric["Yield_kg"], c=data["Cluster"], cmap="viridis")
plt.xlabel("Height (cm)")
plt.ylabel("Yield (kg)")
plt.title("K-Means Clustering of Plant Genotypes")
plt.colorbar(label="Cluster")
plt.show()

# Step 5: Display clustered data
print(data)
