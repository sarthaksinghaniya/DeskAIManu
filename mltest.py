# Kaggle Run Test in jarvis file
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

# Load the data
iowa_file_path = '../input/home-data-for-ml-course/train.csv'
home_data = pd.read_csv(iowa_file_path)

y = home_data.SalePrice
feature_columns = [
    'LotArea',
    'YearBuilt',
    '1stFlrSF',
    '2ndFlrSF',
    'FullBath',
    'BedroomAbvGr',
    'TotRmsAbvGrd'
]
X = home_data[feature_columns]

train_X, val_X, train_y, val_y = train_test_split(
    X, y, random_state=1
)

# Specify and train the model
iowa_model = DecisionTreeRegressor(random_state=1)
iowa_model.fit(train_X, train_y)


val_predictions = iowa_model.predict(val_X)

print(val_predictions[:5])
print(val_y[:5].tolist())

val_mae = mean_absolute_error(val_y, val_predictions)
print("Validation MAE:", val_mae)
