from flask import Flask, request, render_template
from Classifier.Flight_Classifier import AirlineClassifier, FlightClassifier
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd



app = Flask(__name__)
model = pickle.load(open("flight_rf.pkl", "rb"))

@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")


@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        # Date_of_Journey
        date_dep = request.form["Dep_Time"]
        Journey_date = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").day)
        Journey_month = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").month)
        print(date_dep)

        # Departure
        Dep_hour = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").hour)
        Dep_min = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").minute)
        # print("Departure : ",Dep_hour, Dep_min)

        # Arrival
        date_arr = request.form["Arrival_Time"]
        Arrival_hour = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").hour)
        Arrival_min = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").minute)
        # print("Arrival : ", Arrival_hour, Arrival_min)
        print(date_arr)


        # Duration
        dur_hour = abs(Arrival_hour - Dep_hour)
        dur_min = abs(Arrival_min - Dep_min)
        Duration = (dur_hour*60) + dur_min
        # print("Duration : ", dur_hour, dur_min)

        # Total Stops
        Total_stops = int(request.form["stops"])
        # print(Total_stops)


        # Airline
        airline_classifier = AirlineClassifier()
        flight_classifier = FlightClassifier()

        airline = request.form["airline"]
        airline_classifier.classify_Airline(airline)

        Air_Asia = airline_classifier.Air_Asia
        Jet_Airways = airline_classifier.Jet_Airways
        IndiGo = airline_classifier.IndiGo
        Air_India = airline_classifier.Air_India
        Multiple_carriers = airline_classifier.Multiple_carriers
        SpiceJet = airline_classifier.SpiceJet
        Vistara = airline_classifier.Vistara
        GoAir = airline_classifier.GoAir
        Multiple_carriers_Premium_economy = airline_classifier.Multiple_carriers_Premium_economy
        Jet_Airways_Business = airline_classifier.Jet_Airways_Business
        Vistara_Premium_economy = airline_classifier.Vistara_Premium_economy
        Trujet = airline_classifier.Trujet

        # flight
        flight_classifier = FlightClassifier()
        Source = request.form["Source"]
        flight_classifier.classify_source(Source)

        Source_Delhi = flight_classifier.Source_Delhi
        Source_Kolkata = flight_classifier.Source_Kolkata
        Source_Mumbai = flight_classifier.Source_Mumbai
        Source_Chennai = flight_classifier.Source_Chennai
        Source_Banglore = flight_classifier.Source_Banglore


        destination = request.form["Destination"]
        flight_classifier.classify_destination(destination)

        Destination_Delhi = flight_classifier.Destination_Delhi
        Destination_New_Delhi = flight_classifier.Destination_New_Delhi
        Destination_Kolkata = flight_classifier.Destination_Kolkata
        Destination_Hyderabad = flight_classifier.Destination_Hyderabad
        Destination_Cochin = flight_classifier.Destination_Cochin
        Destination_Banglore = flight_classifier.Destination_Banglore



        prediction=model.predict([[Duration, Total_stops, Journey_date, Journey_month, Arrival_hour, Arrival_min, Dep_hour,
        Dep_min, 
        Air_Asia,
        Air_India,                           
        GoAir,
        IndiGo,
        Jet_Airways,
        Jet_Airways_Business,
        Multiple_carriers,
        Multiple_carriers_Premium_economy,
        Trujet,
        SpiceJet,
        Vistara,
        Vistara_Premium_economy,
        Destination_Banglore,
        Destination_Cochin,
        Destination_Delhi,
        Destination_Hyderabad,
        Destination_Kolkata,
        Destination_New_Delhi,
        Source_Banglore,
        Source_Chennai,  
        Source_Delhi,
        Source_Kolkata,
        Source_Mumbai]])


        output=round(prediction[0],2)

        return render_template('home.html',prediction_text="Your flight price will be Rs. {}".format(output))


    return render_template("home.html")




if __name__ == "__main__":
    app.run(debug=True)

