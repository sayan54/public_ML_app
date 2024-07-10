# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 20:34:15 2024

@author: User
"""

import numpy as np
import pickle
import streamlit as st

# loading the saved model
loaded_model = pickle.load(open('E:/ML projects/model.sav', 'rb'))

# creating a function for Prediction

def fraud_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 'Fraud'):
      return ' Fraud'
    else:
      return 'Not Fraud'
  
    
def main():
    
    
    # giving a title
    st.title('Transaction Fraud Detection App')
    
    
    # getting the input data from the user
    
    
    step = st.number_input('Number of step',step=1.,format="%.2f")
    type = st.number_input('Transaction Type',step=1.,format="%.2f")
    amount = st.number_input('Enter Amount',step=1.,format="%.2f")
    oldbalanceOrg = st.number_input('Enter oldbalanceOrg',step=1.,format="%.2f")
    newbalanceOrig = st.number_input('Enter newbalanceOrig',step=1.,format="%.2f")
    oldbalanceDest	= st.number_input('oldbalanceDest value',step=1.,format="%.2f")
    newbalanceDest = st.number_input('newbalanceDest value',step=1.,format="%.2f")
    
    
    
    # code for Prediction
    detection = ''
    
    # creating a button for Prediction
    
    if st.button('Result'):
        detection = fraud_prediction([step, type, amount, oldbalanceOrg, newbalanceOrig, oldbalanceDest, newbalanceDest])
        
        
    st.success(detection)
    
    
    
    
    
if __name__ == '__main__':
    main()
  