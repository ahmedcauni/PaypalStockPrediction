
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras import Sequential,utils
from tensorflow.keras.layers import Flatten, Dense, Conv1D, MaxPool1D, Dropout

df=pd.read_csv('PYPL.csv') #loading my data

print(df.head()) #checking what does the data look like

X = df.drop(['Date','Close','Adj Close','Volume'], axis=1) #Featur data
y = df['Close'] #label data

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X = pd.DataFrame(scaler.fit_transform(X), columns=X.columns) # scaling the features
X.head()

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, shuffle=False) # splitting the data 80% training and 20% testing

#reshaping the features so that it can be applied to my model
X_train = np.array(X_train).reshape(X_train.shape[0], X_train.shape[1], 1)
X_test = np.array(X_test).reshape(X_test.shape[0], X_test.shape[1], 1)

#creating my model
model = Sequential()
model.add(Conv1D(32, kernel_size=(3,), padding='same', activation='relu', input_shape = (X_train.shape[1],1)))
model.add(Conv1D(64, kernel_size=(5,), padding='same', activation='relu'))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(units = 1))
#compiling my model
model.compile(loss='mean_squared_error', optimizer='adam')

#training the model
model.fit(X_train, y_train, epochs=150, validation_split=0.2)

#trying to predict the value of close price using the x_test features
pred_val = model.predict(X_test)

#Looking at the values my model preicted and the values of the already there from actual data
pred_df = pd.DataFrame({'Actual Value': y_test, 'Predicted Value': pred_val.flatten()})
pred_df.head()

#plotting the predicted value and the actual value to evaluate how did my model do with prediction
plt.figure(figsize=(8,8))
plt.ylabel('Close', fontsize=16)
plt.plot(pred_df)
plt.legend(['Actual Value', 'Prediction Value'])
plt.show()
