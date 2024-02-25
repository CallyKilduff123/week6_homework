class Patient:
    def __init__(self, name, age, weight_kg, height_m):
        self.name = name
        self.age = age
        self.weight_kg = weight_kg
        self.height_m = height_m

    def calculate_bmi(self):

        # if self.height_m <= 0:
        #     raise ValueError("Height must be greater than zero.")
        # if self.weight_kg <= 0:
        #     raise ValueError("Weight must be greater than zero.")

        bmi = self.weight_kg / (self.height_m ** 2)
        return bmi

    def health_message(self):
        bmi = self.calculate_bmi()
        if bmi < 20:
            return f"{self.name} is underweight."
        elif bmi <= 25:
            return f"{self.name} has a healthy weight."
        elif bmi <= 30:
            return f"{self.name} is overweight."
        else:  # bmi > 30
            return f"{self.name} is obese."

if __name__ == "__main__":
    patient1 = Patient("Ursula", 30, 120, 1.65)
    bmi = patient1.calculate_bmi()
    print(f"{patient1.name}'s BMI: {bmi:.2f}")
    bmi_message = patient1.health_message()
    print(bmi_message)