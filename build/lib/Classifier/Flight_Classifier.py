class AirlineClassifier:
    def __init__(self):
        self.Jet_Airways = 0
        self.Air_Asia = 0
        self.IndiGo = 0
        self.Air_India = 0
        self.Multiple_carriers = 0
        self.SpiceJet = 0
        self.Vistara = 0
        self.GoAir = 0
        self.Multiple_carriers_Premium_economy = 0
        self.Jet_Airways_Business = 0
        self.Vistara_Premium_economy = 0
        self.Trujet = 0

    def classify_Airline(self, airline):
        self.Jet_Airways = 1 if airline == 'Jet Airways' else 0
        self.Air_Asia = 1 if airline == "Air Asia" else 0
        self.IndiGo = 1 if airline == 'IndiGo' else 0
        self.Air_India = 1 if airline == 'Air India' else 0
        self.Multiple_carriers = 1 if airline == 'Multiple carriers' else 0
        self.SpiceJet = 1 if airline == 'SpiceJet' else 0
        self.Vistara = 1 if airline == 'Vistara' else 0
        self.GoAir = 1 if airline == 'GoAir' else 0
        self.Multiple_carriers_Premium_economy = 1 if airline == 'Multiple carriers Premium economy' else 0
        self.Jet_Airways_Business = 1 if airline == 'Jet Airways Business' else 0
        self.Vistara_Premium_economy = 1 if airline == 'Vistara Premium economy' else 0
        self.Trujet = 1 if airline == 'Trujet' else 0


class FlightClassifier:
    def __init__(self):
        self.Source_Banglore = 0
        self.Source_Delhi = 0
        self.Source_Kolkata = 0
        self.Source_Mumbai = 0
        self.Source_Chennai = 0
        self.Destination_Banglore = 0
        self.Destination_Delhi = 0
        self.Destination_Cochin = 0
        self.Destination_Hyderabad = 0
        self.Destination_Kolkata = 0
        self.Destination_New_Delhi = 0

    def classify_source(self, source):
        self.Source_Delhi = 1 if source == 'Delhi' else 0
        self.Source_Kolkata = 1 if source == 'Kolkata' else 0
        self.Source_Mumbai = 1 if source == 'Mumbai' else 0
        self.Source_Chennai = 1 if source == 'Chennai' else 0
        self.Source_Banglore = 1 if source == "Banglore" else 0

    def classify_destination(self, destination):
        self.Destination_Cochin = 1 if destination == 'Cochin' else 0
        self.Destination_Delhi = 1 if destination == 'Delhi' else 0
        self.Destination_New_Delhi = 1 if destination == 'New_Delhi' else 0
        self.Destination_Hyderabad = 1 if destination == 'Hyderabad' else 0
        self.Destination_Kolkata = 1 if destination == 'Kolkata' else 0
