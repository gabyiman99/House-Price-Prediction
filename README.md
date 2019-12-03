# House-Price-Prediction

This repository is a documentation of our frontier technology project on predicting house prices. 
Given a data of some features that could possibly predict a price of a house, we generate a model, train it using the training data, and use the model to predict new sets of inputs of the corresponding features. All coding was done using Python.

## Data Source
All of the data was obtained from https://www.kaggle.com/c/house-prices-prediction-2/data

## Prerequisite
1. Python
2. Dash library
3. Pip
4. Jupyter Notebook

## Procedures
To be able to give a prediction on the price of a house with certain features, we need to [generate a model](https://github.com/gabyiman99/House-Price-Prediction/blob/master/HousePrice.ipynb) that fits well. To be able to do so, we need to get some training and validation data to help train our model so we can get a model than can make accurate predictions. 

Next, we create an app using Dash to visualize the result by letting users input the value of each features and the predicted price will be shown. To create a Dash app, we use Visual Studio Code as our IDE and use the help of sklearn's pickle module to save our previously trained model. 

First, we create our predictor which is a module that can be called whenever users want to predict a house price. The code can be seen [here](https://github.com/gabyiman99/House-Price-Prediction/blob/master/model_predictor.py) 

Then, we create the layout of the app, including input boxes for users to input the value of each features of the hosue they want to predict. The code can be seen [here](https://github.com/gabyiman99/House-Price-Prediction/blob/master/component.py)
