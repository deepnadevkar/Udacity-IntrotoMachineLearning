#!/usr/bin/python

""" 
    starter code for exploring the Enron dataset (emails + finances) 
    loads up the dataset (pickled dict of dicts)

    the dataset has the form
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person
    you should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""
import pandas as pd
import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
df = pd.DataFrame(enron_data)
df1 = df.T
print df1.shape
print(df1.loc[df1['poi'] == True])


print enron_data["PRENTICE JAMES"]["total_stock_value"]
print enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]
print enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]
print enron_data["SKILLING JEFFREY K"]["total_payments"]
print enron_data["LAY KENNETH L"]["total_payments"]
print enron_data["FASTOW ANDREW S"]["total_payments"]

print(df1.loc[df1['salary'] != 'NaN'])
print(df1.loc[df1['email_address'] != 'NaN'])
print(df1.loc[df1['total_payments'] == 'NaN'])
poi = (df1.loc[df1['poi'] == True])
total_payments_poi = poi.loc[df1['total_payments'] == 'NaN']
print total_payments_poi
