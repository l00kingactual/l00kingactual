import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.cluster import KMeans, MiniBatchKMeans
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis as QDA
from sklearn.linear_model import SGDClassifier
import logging
import os
import glob
import json

# Import value spaces
from k_value_space import k_value_space
from q_value_space import q_value_space
from epsilon_value_space import epsilon_value_space
from epsilon_greedy_vaule_space import create_epsilon_greedy_space

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_all_json_files(directory):
    """
    Load JSON files from a specified directory and its subdirectories, then combine them into a single DataFrame.

    Args:
        directory (str): The root directory containing the JSON files.

    Returns:
        pd.DataFrame: Combined DataFrame from all JSON files.
    """
    # Recursively search for all JSON files in the specified directory and its subdirectories
    json_files = glob.glob(os.path.join(directory, '**', '*.json'), recursive=True)
    
    if not json_files:
        logging.warning(f"No JSON files found in the directory: {directory}")
        return pd.DataFrame()  # Return an empty DataFrame if no files are found

    df_list = []

    for file in json_files:
        try:
            # Check if the file can be accessed
            if not os.access(file, os.R_OK):
                logging.warning(f"Skipping file due to permission issues: {file}")
                continue

            # Load the JSON data manually
            with open(file, 'r') as f:
                content = f.read()
                try:
                    # Attempt to load the entire content as a single JSON object
                    data = json.loads(content)
                    df = pd.json_normalize(data)
                except json.JSONDecodeError:
                    # If there's an error, attempt to load it as multiple JSON objects
                    lines = content.splitlines()
                    for line in lines:
                        data = json.loads(line)
                        df = pd.json_normalize(data)
                        df.fillna(0, inplace=True)
                        df_list.append(df)
                    continue

            # Reset the index to avoid any issues with index uniqueness
            df.reset_index(drop=True, inplace=True)
            
            # Handle any potential NaN values by filling them with a default value
            df.fillna(0, inplace=True)
            
            # Append the DataFrame to the list
            df_list.append(df)

            logging.info(f"Successfully processed {file}")
        
        except PermissionError as e:
            logging.error(f"PermissionError for {file}: {e}")
        except json.JSONDecodeError as e:
            logging.error(f"Failed to decode JSON in {file}: {e}")
        except Exception as e:
            logging.error(f"Failed to process {file}: {e}")

    if df_list:
        # Concatenate all DataFrames in the list
        combined_df = pd.concat(df_list, ignore_index=True)
        
        # Ensure all NaN values are filled with 0 in the final DataFrame
        combined_df.fillna(0, inplace=True)

        # Infer objects' data types in the final DataFrame
        combined_df = combined_df.infer_objects(copy=False)

        logging.info("Successfully combined all DataFrames.")
        return combined_df
    else:
        logging.warning("No valid DataFrames were loaded; returning an empty DataFrame.")
        return pd.DataFrame()  # Return an empty DataFrame if no data was loaded


# Usage example
directory = r"E:\tetra_ai_ml\19_08_2024_Start\analysis"
combined_df = load_all_json_files(directory)

if not combined_df.empty:
    print("Combined DataFrame:")
    print(combined_df.head())
else:
    print("No data to display.")

# Initialize 'k', 'q', and 'epsilon' with values from their respective spaces if they don't exist
additional_columns = {}
if 'k' not in combined_df.columns:
    additional_columns['k'] = np.random.choice(k_value_space, size=len(combined_df))

if 'q' not in combined_df.columns:
    additional_columns['q'] = np.random.choice(q_value_space, size=len(combined_df))

if 'epsilon' not in combined_df.columns:
    additional_columns['epsilon'] = np.random.choice(epsilon_value_space, size=len(combined_df))

if additional_columns:
    combined_df = pd.concat([combined_df, pd.DataFrame(additional_columns)], axis=1)

# Replace any NaN or Null values in the DataFrame with 0
combined_df.fillna(0, inplace=True)

# Feature Engineering for k, q, and epsilon
if {'k', 'q', 'epsilon'}.issubset(combined_df.columns):
    features = combined_df[['k', 'q', 'epsilon']]

    # Scale the features
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)

    # Replace the original columns with their scaled values
    combined_df[['k', 'q', 'epsilon']] = scaled_features

    # Replace any NaN or Null values in the DataFrame with 0
    combined_df.fillna(0, inplace=True)

    print("Scaled features replaced in the DataFrame:")
    print(combined_df[['k', 'q', 'epsilon']].head())

    # Example ML Task: Classification using k, q, and epsilon as features
    if 'target' in combined_df.columns:  # Replace 'target' with the actual target column name
        X = combined_df[['k', 'q', 'epsilon']]
        y = combined_df['target']

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Initialize a simple model (e.g., RandomForest)
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        # Make predictions
        y_pred = model.predict(X_test)

        # Evaluate the model
        accuracy = accuracy_score(y_test, y_pred)
        print(f"Model accuracy: {accuracy:.2f}")

        # K-means clustering
        kmeans = KMeans(n_clusters=3, random_state=42)
        kmeans_labels = kmeans.fit_predict(X_train)
        combined_df['kmeans_cluster'] = kmeans.predict(X_train)

        # Dynamic K-means (MiniBatchKMeans)
        dynamic_kmeans = MiniBatchKMeans(n_clusters=3, random_state=42)
        dynamic_kmeans_labels = dynamic_kmeans.fit_predict(X_train)
        combined_df['dynamic_kmeans_cluster'] = dynamic_kmeans.predict(X_train)

        # Q-Learning with Quadratic Discriminant Analysis (QDA)
        qda = QDA()
        qda.fit(X_train, y_train)
        qda_accuracy = qda.score(X_test, y_test)
        print(f"QDA accuracy: {qda_accuracy:.2f}")

        # Epsilon-Greedy Optimization with Stochastic Gradient Descent (SGDClassifier)
        epsilon_greedy = SGDClassifier(max_iter=1000, tol=1e-3, random_state=42)
        epsilon_greedy.fit(X_train, y_train)
        sgd_accuracy = epsilon_greedy.score(X_test, y_test)
        print(f"SGD (Epsilon-Greedy) accuracy: {sgd_accuracy:.2f}")

else:
    print("The DataFrame does not contain the required 'k', 'q', and 'epsilon' columns.")