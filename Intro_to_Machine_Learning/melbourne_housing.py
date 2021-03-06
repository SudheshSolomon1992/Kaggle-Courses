import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor  
from sklearn.metrics import mean_absolute_error

melbourne_file_path = './input/melbourne_housing_snapshot/melb_data.csv'

def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return(mae)

# read the csv
melbourne_data = pd.read_csv(melbourne_file_path)
# print the summary
print (melbourne_data.describe())

# lists the columns of the dataset
print (melbourne_data.columns)

# dropna drops missing values
melbourne_data = melbourne_data.dropna(axis=0)

# select the targe column with dot notation
y = melbourne_data.Price

# selecting subset of columns. This is just a sample list of columns taken at random.
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
X = melbourne_data[melbourne_features]

print (X.describe())

# split data into training and validation data, for both features and target
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)

################### STEPS TO BUILDING AND USING MODEL ###################

# Define: What type of model will it be? A decision tree? Some other type of model? Some other parameters of the model type are specified too.
# Fit: Capture patterns from provided data. This is the heart of modeling.
# Predict: Just what it sounds like
# Evaluate: Determine how accurate the model's predictions are.

################### STEPS TO BUILDING AND USING MODEL ###################

# Define model. Specify a number for random_state to ensure same results each run
melbourne_model = DecisionTreeRegressor(random_state=1)

# Fit model
melbourne_model.fit(train_X, train_y)

# predict scores for validation set
val_predictions = melbourne_model.predict(val_X)

# find the MAE for the model
print (mean_absolute_error(val_y, val_predictions))

# compare MAE with differing values of max_leaf_nodes
for max_leaf_nodes in [5, 50, 500, 5000]:
    my_mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
    print("Max leaf nodes: %d  \t\t Mean Absolute Error:  %d" %(max_leaf_nodes, my_mae))

################### RANDOM FOREST ############################

forest_model = RandomForestRegressor(random_state=1)
forest_model.fit(train_X, train_y)
melb_preds = forest_model.predict(val_X)
print(mean_absolute_error(val_y, melb_preds))
