#pip install scikit-learn
from sklearn.linear_model import LinearRegression
# Training data
X = [[1], [2], [3], [4], [5]]
y = [35, 45, 55, 65, 75]
# Create and train the model
model = LinearRegression()
model.fit(X, y)
# Make a prediction
prediction = model.predict([[6]])
print("Study hours: 6")
print("Predicted marks:", prediction[0])
print("model traind successfully  ")
print("Running experimental model")
