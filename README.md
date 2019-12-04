# House-Price-Prediction
by : Licyawati Dewi, Gabriella, Eric Jahja

This repository is a documentation of our frontier technology project on predicting house prices. 
Given a data of some features that could possibly predict a price of a house, we generate a model, train it using the training data, and use the model to predict new sets of inputs of the corresponding features. All coding was done using Python.

## Data Source
All of the data was obtained from https://www.kaggle.com/c/house-prices-prediction-2/data

## Prerequisite
1. Python3
2. Dash library
3. Pip
4. Jupyter Notebook
5. Visual Studio Code

## Installation
1. Download this repository.<br>
2. There are a few packages needed to be installed, which is:<br>
    i.  <code>dash</code> with the command <code>pip install dash</code>.<br>
    ii. <code>plotly</code> with the command <code>pip install plotly</code>.<br>
note : run these codes in the command prompt instead of a regular python notebook cell.<br>
3. Run Visual Studio Code.<br>
4. Run <code>components.py</code>.<br>
5. The following code should be present in the VSCode terminal:<br>
Running on http://127.0.0.1:8050/ <br>
Debugger PIN: 569-451-627<br>
 * Serving Flask app "component" (lazy loading)<br>
 * Environment: production<br>
   WARNING: This is a development server. Do not use it in a production deployment.<br>
   Use a production WSGI server instead.<br>
 * Debug mode: on<br>
6. Click on the local link, and the web will start.<br>

## Development Flow
### 1. Model Development
There are a total of 6 processes in our model development, stated as follows:<br>
* Data Acquisition
* Train-Test Split
* Feature Selection
* Model Training
* Model Evaluation

### 2. Front-End Development
Front-end was developed using Dash. The app focused all the scripts to one single file <code>components.py</code>.
### 3. Integration
The fitted model is saved as <code>.pkl</code> extension. The predictor is to be ran along with <code>components.py</code> as it is also inside the Dash script.
### 4. Production
After the succesful integration, the app is ready to be used.

## Procedures
To be able to give a prediction on the price of a house with certain features, we need to [generate a model](https://github.com/gabyiman99/House-Price-Prediction/blob/master/HousePrice.ipynb) that fits well. To be able to do so, we need to get some training and validation data to help train our model so we can get a model than can make accurate predictions. We used both random forest and linear regression to compare the results. It turns out that linear regression produced higher errors, so we decided to use the random forest algorithm as our predictor.

Next, we create an app using Dash to visualize the result by letting users input the value of each features and the predicted price will be shown. To create a Dash app, we use Visual Studio Code as our IDE and use the help of sklearn's pickle module to save our previously trained model. As a way to  improve our GUI, we have also made some CSS codes for a better look at the results.

First, we create our predictor which is a module that can be called whenever users want to predict a house price. The code can be seen [here](https://github.com/gabyiman99/House-Price-Prediction/blob/master/model_predictor.py) 

Then, we create the layout of the app, including input boxes for users to input the value of each features of the hosue they want to predict. The code can be seen [here](https://github.com/gabyiman99/House-Price-Prediction/blob/master/component.py)

## Development Suggestions
- There are other variables that can be dropped, as the final prediction will be altered by these seemingly unimportant features.
- Broader data is recommended for these predictions.

## Disclaimer
- The data are used for a previous Kaggle InClass competition and therefore are no longer suitable for modelling. We are using these data merely for academic purposes.
- This repository is made by Licyawati Dewi, Gabriella, and Eric Jahja to fulfill course assignments of <i>Frontier Technology</i> in Informatics study program of Pelita Harapan University.
