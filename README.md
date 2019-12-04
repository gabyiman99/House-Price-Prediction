# House-Price-Prediction
by : Licyawati Dewi, Gabriella, Eric Jahja

This repository is a documentation of our Frontier Technology project on predicting house prices. 
Given data of some features that could possibly predict a price of a house, we generate a model, train it using the training data, and use the model to predict new sets of input of the corresponding features. All coding was done using Python.

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
* Data Acquisition <br>
We get all data to train our model from the Kaggle website https://www.kaggle.com/c/house-prices-prediction-2/data and use the train.csv file. Then, separate the features from the target variable which is <code>price</code>. <br>
* Train-Test Split <br>
To split the data for training and validation, we use the module <code> train_test_split</code> from <code>sklearn.model_selection</code>
```bash
from sklearn.model_selection import train_test_split
```
and set the <code>test_size</code> to 0.33. This means that 33% of data from the train.csv file will be selected randomly and used as validation data. We also set the <code>random_state</code> value to 1 so that each run can give us the same random data split. Using the <code>.shape</code> property, it can be seen that our data currently has 18 features that will be used to predict the target variable.<br>
* Feature Selection<br>
To select the features that we actually want to include in the model, we use the correlation approach. That is, we remove features that have high correlation with other features (in this case if the correlation coefficient is larger than 0.72). In the notebook, we use heatmap to visualize the correlations between each feature. In a heatmap, the correlation coefficient are visualized as blocks of colors ranging from light (low correlation) to dark (high correlation). Below is the picture of the data's heatmap.<br>
[ HEAT MAP PIC ]<br>
As can be seen, some features have high correlation with other features so we drop them from the data. The purpose of removing these features is to avoid multicollienearity which can result in a skewed or biased prediction. It can be seen that our final data has a total of 16 features. <br>
Next, we need to see if there are any missing values in our data using
```python
    cols_miss = [col for col in X_train_drop.columns if X_train_drop[col].isnull().any()]</code>
```
It turns out that there isn't any so we can proceed to the next step. <br>
The final step is to check for categorical features, and our data has none of it. So our training data is ready to be used to train the model. <br>
* Model Training <br>
We chose 2 models, random forest and linear regression, and will later compare them to choose which one can predict with better accuracy. <br>
    * Random Forest <br>
        ```python
        from sklearn.ensemble import RandomForestRegressor
        from sklearn.metrics import mean_squared_error
        ```
    We use the <code>RandomForestRegressor</code> model from <code>sklearn</code> and set the n_estimators to 10 to avoid overfitting. Then we train the model on our training data using the <code>.fit</code> feature. We then use the model to predict the house prices on the validation data using the <code>.predict</code> feature and calculate the mean squared error using <code>mean_squared_error</code> function. <br>
    * Linear Regression <br>
        ```python
        from sklearn.linear_model import LinearRegression
        ```
    We use the <code>LinearRegression</code> model from <code>sklearn</code>. Then we train the model on our training data using the <code>.fit</code> feature. We then use the model to predict the house prices on the validation data using the <code>.predict</code> feature and calculate the mean squared error using <code>mean_squared_error</code> function. <br> 
* Model Evaluation<br>
It can be seen clearly that the random forest model has a better accuracy because the mean squared error value is only half the value of the linear regression model. Thus, we choose random forest as our model.<br> 
Finally we need to save our trained model so whenever we want to predict a house price, we can just call the trained model and calculate the predicted price without having to train the model over and over again. In this case, we used pickle. 
    ```bash
    import pickle
    ```
To save the model, simply use <code>pickle.dump()</code> and put it into a file called <code>'finalized_model_rf.pkl'</code><br>
All code regarding the model development can be seen [here](https://github.com/gabyiman99/House-Price-Prediction/blob/master/HousePrice.ipynb)<br>
### 2. Front-End Development
Front-end was developed using Dash. The main code for the dash app is in the [component.py](component.py). Before starting, there are some libraries and modules that need to be downloaded
```bash
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
```
* Layout<br>
To make the layout of the app, we use html and bootstrap components in dash as well as a little bit of css external stylesheet. First we define the app's body using <code>dbc.Container</code> and every thing visible in the app screen is put inside this container. To display it, use
    ```python
    app.layout = html.Div(body)
    ```
* Callbacks<br>
Callbacks are basically functions that is available in Dash to make the app dynamic. To get input values from user, we use
    ```python
    @app.callback(Output('output-state', 'children'),
                  [Input(component_id='submit-button', component_property='n_clicks')],
                  [State('input-1-state', 'value')
    ```
To update the output value, we use
    ```python
    def update_output(n_clicks: int,
                             var_name: dtype):
            if n_clicks is None:
                raise PreventUpdate
            else:
                data1 = model_predictor.predict(
                    var_name = var_name
                )
                data = {
                    'prediction': data1
                }
                return u
                The house predicted price is USD {},
                .format(data["prediction"])
    ```
### 3. Integration
To get an output, we need to use our model to predict the price of a house depending on the user's input. First, make a file where we define the predictor class, for example, [model_predictor.py](model_predictor.py). Remember that the trained model has been saved, and now we can load it using pickle.
```python
    pickle.load(open('finalized_model_rf.pkl', 'rb'))
```
After that, we need to make a predict function 
```python
def predict(self, **kwargs):
        data = {
            "features": [kwargs['var_name']]
        }
        data = pd.DataFrame(data)
        result = self.predict_prob(data)

        return result
```
```python
predict(data)
```

Make sure that the feature name ("features") is correct for each feature as it will determine in which column the input data of a certain variable name (var_name) will be put. If the input data is put in the wrong column/feature, the prediction result will not be accurate.<br>
Back in the component.py file, call the predictor
```bash
model_predictor = Predictor()
```
So, when <code>model_predictor.predict()</code> is called, the input data gets transformed into a data frame with each corresponding feature, and the model will predict the price.  
### 4. Production
To run the app, open a terminal or cmd, change the directory to your project's directory, and run the python file
```bash
python appname.py
```

## Procedures
To be able to give a prediction on the price of a house with certain features, we need to [generate a model](https://github.com/gabyiman99/House-Price-Prediction/blob/master/HousePrice.ipynb) that fits well. To be able to do so, we need to get some training and validation data to help train our model so we can get a model than can make accurate predictions. We used both random forest and linear regression to compare the results. Linear regression produced greater errors, so we decided to use the random forest algorithm as our predictor.

Next, we create an app using Dash to visualize the result by letting users input the value of each features and the predicted price will be shown. To create a Dash app, we use Visual Studio Code as our IDE and use the help of sklearn's pickle module to save our previously trained model. As a way to improve our GUI, we have also made some CSS codes for a better look at the results.

First, we create our predictor which is a module that can be called whenever users want to predict a house price. The code can be seen [here](https://github.com/gabyiman99/House-Price-Prediction/blob/master/model_predictor.py) 

Then, we create the layout of the app, including input boxes for users to input the value of each features of the hosue they want to predict. The code can be seen [here](https://github.com/gabyiman99/House-Price-Prediction/blob/master/component.py)

## Development Suggestions
- Broader data is recommended for these predictions.
- The GUI can be improved to show the data.

## Disclaimer
- We are using these data merely for academic purposes.
- This repository is made by Licyawati Dewi, Gabriella, and Eric Jahja to fulfill course assignments of <i>Frontier Technology</i> in Informatics Study Program of Pelita Harapan University.
