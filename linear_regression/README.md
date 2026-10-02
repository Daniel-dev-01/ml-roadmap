# Linear Regression

## Project Overview

This project demonstrates the basic workflow of building a supervised machine learning regression model with Python and scikit-learn. Using the Telco Customer Churn dataset, I trained a Linear Regression model to predict `MonthlyCharges` from selected customer features, then evaluated its performance using MAE, MSE, RMSE, and R².

The main focus of the project is understanding the end-to-end ML workflow, from data cleaning and train/test splitting to model training, prediction, and evaluation.

# The Project

A beginner machine learning project where I trained a Linear Regression model using the Telco Customer Churn dataset to predict `MonthlyCharges`.

## Project Goal

The goal of this project was to understand the complete workflow of building and evaluating a regression model:

1. Load the dataset
2. Clean the data
3. Select features and target
4. Split the data into training and testing sets
5. Train a Linear Regression model
6. Make predictions
7. Evaluate the model using MAE, MSE, RMSE, and R²

## Dataset

The dataset contains information about 7,043 telecom customers.

The target I chose to predict is:

```text
MonthlyCharges
```

The features used by the model are:

```text
tenure
TotalCharges
SeniorCitizen
```

### Data Cleaning

`TotalCharges` was originally stored as text, so I converted it to a numeric data type.

There were 11 missing values after the conversion. These rows were removed because filling them with an artificial value such as 0 could introduce misleading information into the model.

After cleaning:

```text
Original rows: 7043
Rows after cleaning: 7032
```

## Features and Target

In machine learning, the features are the information we give the model to learn from.

I stored the features in `X`:

```python
X = df[["tenure", "TotalCharges", "SeniorCitizen"]]
```

The target is the value we want the model to predict, which I stored in `y`:

```python
y = df["MonthlyCharges"]
```

So:

```text
X = inputs/features
y = target/output
```

## Train/Test Split

I split the dataset into training and testing data using `train_test_split`.

```python
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
```

The data was split into:

```text
Training data: 80%
Testing data: 20%
```

The training data is used to teach the model.

The testing data is kept separate so that I can evaluate how the model performs on data it did not see during training.

### Why not evaluate on training data?

If I evaluate the model using the same data it learned from, the result may make the model look better than it really is.

The test set gives me a better idea of how the model performs on unseen data.

## Model Training

I used Linear Regression from scikit-learn:

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)
```

`LinearRegression()` creates the model.

`.fit()` trains the model using the training features and their corresponding target values.

The model learns the relationship between the features and `MonthlyCharges`.

## Making Predictions

After training, I used the test features to make predictions:

```python
y_pred = model.predict(X_test)
```

`X_test` contains data that the model did not use during training.

`y_pred` contains the model's predicted `MonthlyCharges` values.

## Model Evaluation

I evaluated the model using four metrics.

### MAE: Mean Absolute Error

MAE tells me the average size of the model's mistakes.

In simple terms:

> How far off are my predictions on average?

My result:

```text
MAE = 12.48
```

This means the predictions were, on average, about 12.48 charge units away from the actual values.

### MSE: Mean Squared Error

MSE calculates the average of the squared errors.

Squaring the errors means that larger errors have a much bigger effect on the final value.

In simple terms:

> How much do large prediction errors affect the model's error?

My result:

```text
MSE = 255.45
```

### RMSE: Root Mean Squared Error

RMSE is the square root of MSE.

Because the square root brings the result back to the original unit of the target, RMSE is easier to interpret than MSE.

It also gives larger errors more influence than MAE.

My result:

```text
RMSE = 15.98
```

This means the model's prediction errors are around 15.98 charge units on the RMSE scale.

### R²: R-squared

R² measures how much of the variation in the target can be explained by the model.

My result:

```text
R² = 0.711
```

This means the model explains approximately 71.1% of the variation in `MonthlyCharges` on the test set.

R² should not be interpreted as 71.1% accuracy.

## Results

| Metric | Result |
| ------ | -----: |
| MAE    |  12.48 |
| MSE    | 255.45 |
| RMSE   |  15.98 |
| R²     |  0.711 |

## What I Learned

Through this project, I learned the basic workflow of a supervised machine learning regression problem:

```text
Load data
    ↓
Clean data
    ↓
Choose features and target
    ↓
Split into training and testing data
    ↓
Choose a model
    ↓
Train with fit()
    ↓
Make predictions with predict()
    ↓
Evaluate predictions
```

I also learned that different evaluation metrics answer different questions. MAE focuses on the average size of errors, MSE and RMSE give more importance to larger errors, while R² describes how much variation in the target is explained by the model.

## Important Limitation

This is a learning project and the feature selection is intentionally simple.

`TotalCharges` is strongly related to `MonthlyCharges`, so using it to predict `MonthlyCharges` is not necessarily the best real-world feature design. A future version of this project should explore better feature selection and categorical variables such as `Contract`, `InternetService`, and other customer characteristics.

The purpose of this project was primarily to understand the end-to-end Linear Regression workflow and model evaluation.

## Files

```text
linear_regression/
├── data.csv
├── model.py
└── README.md
```

## Next Steps

* Improve feature selection
* Explore categorical features
* Compare Linear Regression with other regression models
* Perform more detailed model analysis
* Visualize predictions and residuals
* Continue building toward more advanced machine learning projects
