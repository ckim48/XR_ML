import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import plotly.express as px

data = pd.read_csv("static/data/consulting_data_content_logic.csv")

print(data)

# Drop username column as it's not relevant for clustering
data.drop(columns=['username'], inplace = True)
print(data)
# Convert categorical variables to numerical/boolean
data = pd.get_dummies(data)
print(data)

# students
# 93 92 95 93 97 100 99 95 97 99
# Convert the data into 0~1

# Data normalization
scaler = StandardScaler()
df_sacled = scaler.fit_transform(data)

# Clustering
kmeans = KMeans(n_clusters = 3, random_state=42)
kmeans.fit(df_sacled)
data['cluster'] = kmeans.labels_
print(data['cluster'])

# Machine Learning
# Machine Learning is a field of AI that focuses on developing algorithm/technique
# that enable computers to learn from and make predictions or decision based on data.
    # Supervised Learning  --> Classficiation
        # the algorithm learns from labeled data, where each example in the
        # training data is associated with a correspoding label.
    # Unsupervised Learning --> Clustering
        # the algorithm learns from unlabeld data, where algorithm tries to find
        # hidden structures or patterns in the data.
    # Reinforcement Learning
        # the model learns to interact with an enviornment by taking actions and receiving
        # reaward.
# Clustering
# techniquuee used in unsupervised learning to group similar data based on their
# characterics or features.



