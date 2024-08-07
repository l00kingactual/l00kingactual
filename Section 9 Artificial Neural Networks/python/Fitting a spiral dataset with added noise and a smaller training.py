import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.optimizers import Adam
import logging

# Configure logging for detailed console output
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_spiral_dataset(n_samples, noise=0.5):
    """
    Generate a noisy spiral dataset.
    
    Args:
        n_samples (int): Number of samples in each class.
        noise (float): Amount of noise to add to the data.
        
    Returns:
        X (ndarray): Features.
        y (ndarray): Labels.
    """
    np.random.seed(42)
    n = np.sqrt(np.random.rand(n_samples, 1)) * 780 * (2 * np.pi) / 360
    d1 = -np.cos(n) * n + np.random.rand(n_samples, 1) * noise
    d2 = np.sin(n) * n + np.random.rand(n_samples, 1) * noise
    X = np.vstack((np.hstack((d1, d2)), np.hstack((-d1, -d2))))
    y = np.hstack((np.zeros(n_samples), np.ones(n_samples)))
    return X, y

def create_spiral_model(input_shape):
    """
    Create a neural network model for the spiral dataset.
    
    Args:
        input_shape (tuple): Shape of the input data.
        
    Returns:
        model (Sequential): Compiled neural network model.
    """
    model = Sequential([
        Input(shape=input_shape),
        Dense(64, activation='relu'),
        Dense(64, activation='relu'),
        Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer=Adam(learning_rate=0.01), loss='binary_crossentropy', metrics=['accuracy'])
    return model

def plot_decision_boundary(model, X, y):
    """
    Plot the decision boundary of the trained model.
    
    Args:
        model (Sequential): Trained neural network model.
        X (ndarray): Features.
        y (ndarray): Labels.
    """
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, y[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01), np.arange(y_min, y_max, 0.01))
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    
    plt.contourf(xx, yy, Z, alpha=0.8, cmap=plt.cm.Spectral)
    plt.scatter(X[:, 0], X[:, 1], c=y, s=20, edgecolor='k')
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.title('Decision Boundary')
    plt.show()

def main():
    try:
        logging.info("Generating spiral dataset")
        X, y = generate_spiral_dataset(100, noise=0.1)
        
        plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Spectral)
        plt.title('Spiral Dataset')
        plt.show()
        
        logging.info("Creating and training the model with Gradient Descent")
        model_gd = create_spiral_model(X.shape[1:])
        history_gd = model_gd.fit(X, y, epochs=100, batch_size=16, verbose=0)
        
        logging.info("Model training completed")
        
        y_pred_gd = model_gd.predict(X)
        
        plt.figure(figsize=(18, 6))
        
        plt.subplot(1, 2, 1)
        plt.plot(X, y, 'b.', label='Data')
        plt.plot(X, y_pred_gd, 'r-', label='GD Prediction')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Gradient Descent Optimization')
        plt.legend()
        
        plot_decision_boundary(model_gd, X, y)
        
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
