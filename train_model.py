import  pandas as pd  
df = pd.read_csv('car_cleaned_data_NEW.csv')
 
X=df[['Present_Price', 'Kms_Driven',
       'Car_Age', 'Fuel_Type_CNG', 'Fuel_Type_Diesel',
       'Fuel_Type_Petrol', 'Transmission_Automatic', 'Transmission_Manual']]
y=df['Selling_Price']
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X, y)
import pickle
with open('lr_model_New.pkl', 'wb') as model_file:#wb: write binary
    pickle.dump(model, model_file)