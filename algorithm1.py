import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression
def create_model():
    df=pd.read_excel("vehical.xlsx")
    #print(df)
    model_np=np.array(df["model"])
    km_np=np.array(df["km"])
    year_np=np.array(df["year"])
    power_np=np.array(df["power"])
    price_np=np.array(df["price"])
    #print(model_np)
    #print(km_np)
    #print(year_np)
    #print(power_np)
    #print(price_np)

    #linear regression....preprocessing "model"

    model_pp=preprocessing.LabelEncoder() #label encode use cheydhathu strng na num akki
    model_pp.fit(model_np)
    model_preprocessed=model_pp.transform(model_np)
    print(model_preprocessed)

    #model creation --first creat dictionary
    dictionary={'model':model_preprocessed,'km':km_np,'year':year_np,"power":power_np}
    df1=pd.DataFrame(dictionary)
    print(df1)

    #import linear regression , creat liner regess model

    lr=LinearRegression()               # model te obj create cheydh
    lr.fit(df1,price_np)          #labL PRICE ANN
    #print(lr)

    model=input("enter the model:")
    km=int(input("enter th km:"))
    year=int(input("enter the year:"))
    power=int(input("enter the power:"))

    model_entered_preprocessed=model_pp.transform([model])
    #print(model_entered_preprocessed)

    #getting prediction, creat numpy array of features

    for_prediction_np=np.array([[model_entered_preprocessed[0],km,year,power]])
    prediction=lr.predict(for_prediction_np)
    print(prediction)

    #output of the prediction
    #enter th km:45
    #enter the year:2016
    #enter the power:60
    #[463303.68867136]



create_model()
