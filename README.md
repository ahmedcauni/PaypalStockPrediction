# Overview
This Python script is designed to predict stock prices using Convolutional Neural Networks (Conv1D) for one-dimensional data. The script imports stock market data from a CSV file, preprocesses the data, splits it into training and testing sets, and then uses the Conv1D model for prediction.

# Dataset
Paypal Holdings Inc. from Yahoo.finance

#Data Preprocessing
-Drop irrelevant columns like Date, Close, Adj Close, and Volume.
-Scale the feature data using Min-Max scaling.
-Split the data into 80% training and 20% testing sets.
$Model Architecture
The model uses a Conv1D neural network architecture with the following layers:
  -Conv1D layer with 32 filters and kernel size 3
  -Conv1D layer with 64 filters and kernel size 5
  -Flatten layer
  -Dense layer with 128 neurons
  -Dense layer with 1 neuron for output
  -The model uses mean_squared_error as the loss function and adam as the optimizer.

# Evaluation
The model is trained for 150 epochs. The predicted stock prices are plotted against the actual stock prices for visual evaluation.

