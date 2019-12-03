import os
import pickle
import random
#from sklearn.externals import joblib

import numpy as np
import pandas as pd
import sklearn.model_selection as ms
#from os import open
#from matplotlib.artist import get
#from joblib import load

class Predictor:
    '''Predictor serves as a class for generating predictions'''

    def __init__(self):
        curr_dir = os.path.dirname(os.path.realpath(__file__))
        self.model = pickle.load(open(os.path.join(curr_dir, 'finalized_model_rf.pkl'), 'rb'))

    def predict_prob(self, data: pd.DataFrame):
        return self.model.predict(data)

    def predict(self, **kwargs):
        data = {
            "bedrooms": [kwargs['bed']],
            "bathrooms": [kwargs['bath']],
            "floors": [kwargs['floor']],
            "waterfront": [kwargs['wf']],
            "view": [kwargs['view']],
            "condition": [kwargs['cond']],
            "grade": [kwargs['grade']],
            "sqft_above": [kwargs['sabv']],
            "sqft_basement": [kwargs['sbst']],
            "yr_built": [kwargs['yblt']],
            "yr_renovated": [kwargs['yrnv']],
            "zipcode": [kwargs['zipc']],
            "lat": [kwargs['lat']],
            "long": [kwargs['lng']],
            "sqft_living15": [kwargs['sliv15']],
            "sqft_lot15": [kwargs['slot15']]
        }
        data = pd.DataFrame(data)
        
        #result = self.predict_prob(data)[:,0].tolist()[0]*100
        result = self.predict_prob(data)

        return result