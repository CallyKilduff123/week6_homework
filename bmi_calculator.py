# create class called Patient and enter details including height in m and weight in kg
# initialise bmi but don't pass in parameters as not entered manually

class Patient:
    def __init__(self, name, age, condition, weight_kg, height_m):
        self.name = name
        self.age = age
        self.condition = condition
        self.weight_kg = weight_kg
        self.height_m = height_m
        self.bmi = self.calculate_bmi()

    # create calculation for bmi as method and return response
    # return allows the response to be passed into the formatted string later
    def calculate_bmi(self):
        bmi = self.weight_kg / (self.height_m ** 2)
        return bmi

    # create health message based on bmi, with actions for the GP
    # use if else statements
    # return the response - this allows it to be passed into the formatted string later
    def health_message(self):
        bmi = self.calculate_bmi()
        if bmi < 20:
            return f"{self.name} is underweight. Offer health visitor appointment"
        elif bmi <= 25:
            return f"{self.name} has a healthy weight."
        elif bmi <= 30:
            return f"{self.name} is overweight. Send leaflet on healthy eating and exercise"
        else:  # bmi > 30
            return f"{self.name} is obese. Offer telephone appointment"

    # formatted string - this contains the above information and returns it as a string, allowing you to format it
    def __str__(self):
        return (f"Name: {self.name}\nAge: {self.age} years\nCondition: {self.condition}\nBMI: {self.bmi:.0f}\n"
                "************************************************************\n"
                f"Health alert: {self.health_message()}\n"
                "************************************************************\n")

# main trick
# create patients and pass in patient class - prompts to enter correct information in the correct positions
# the bmi calculation is done and returned as the formatted string
if __name__ == "__main__":

    patient1 = Patient("Ursula", 30, 'diabetes', 120, 1.5)
    print(patient1)
    patient2 = Patient("Ariel", 16, 'amenorrhoea', 45, 1.7)
    print(patient2)
