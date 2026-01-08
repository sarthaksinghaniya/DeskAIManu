import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.tree import DecisionTreeRegressor

# -------------------------------
# Load data
# -------------------------------
data_path = "../input/home-data-for-ml-course/train.csv"
data = pd.read_csv(data_path)

y = data.SalePrice

features = [
    'LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF',
    'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd'
]

X = data[features]

# -------------------------------
# Train-validation split
# -------------------------------
X_train, X_valid, y_train, y_valid = train_test_split(
    X, y, train_size=0.8, random_state=0
)

# -------------------------------
# Model evaluation function
# -------------------------------
def score_model(model):
    model.fit(X_train, y_train)
    preds = model.predict(X_valid)
    return mean_absolute_error(y_valid, preds)

# -------------------------------
# Define models
# -------------------------------
models = [
    DecisionTreeRegressor(max_leaf_nodes=5, random_state=0),
    DecisionTreeRegressor(max_leaf_nodes=25, random_state=0),
    DecisionTreeRegressor(max_leaf_nodes=50, random_state=0),
    DecisionTreeRegressor(max_leaf_nodes=100, random_state=0),
    DecisionTreeRegressor(max_leaf_nodes=500, random_state=0)
]

# -------------------------------
# Compare models
# -------------------------------
for i, model in enumerate(models, start=1):
    mae = score_model(model)
    print(f"Model {i} MAE: {int(mae)}")

# -------------------------------
# Select best model (from results)
# -------------------------------
best_model = models[2]

# -------------------------------
# Define final model
# -------------------------------
my_model = best_model

# -------------------------------
# Train final model on full data
# -------------------------------
my_model.fit(X, y)

# -------------------------------
# (Optional) Make predictions
# -------------------------------
test_data = pd.read_csv("../input/home-data-for-ml-course/test.csv")
X_test = test_data[features]

predictions = my_model.predict(X_test)

output = pd.DataFrame({
    'Id': test_data.Id,
    'SalePrice': predictions
})

output.to_csv("submission.csv", index=False)
print("submission.csv created successfully")
