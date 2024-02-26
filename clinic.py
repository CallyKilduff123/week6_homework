# OLD CODE  - iteration 1
# created the class patient
# tried to use input to assign category to each patient but i had to enter the category before the patient populated
# could try user inputting all of the patient details including category

# created List class
# had method to add patients

class Patient:
    def __init__(self, firstname, lastname, age, condition):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.condition = condition

    def __str__(self):
        return (f"-------------------------------------"
                f"\nFirstname: {self.firstname}\nLastname: {self.lastname}\n"
                f"Age: {self.age} years\nCondition: {self.condition}\n-------------------------------------")


class Category:
    def assign_category(self):
        category_code = input('S for strabismus, R for refractive error, '
                              'A for anterior segment, P for posterior segment').upper()
        if category_code == 'S':
            print('Strabismus patient. Investigations: VA--Orthoptics--Dilate--Refraction--Doctor')
        elif category_code == 'R':
            print('Refractive patient. Investigations: VA--Orthoptics--Refraction')
        elif category_code == 'A':
            print('Anterior segment patient. Investigations: VA--Doctor')
        elif category_code == 'P':
           print('Posterior segment patient. Investigations: VA--Orthoptics--Dilate--OCT--OPTOS--Doctor')
        else:
            print('Other - clinical team to assign investigations')
        return category_code


class List:
    def __init__(self):
        self.patients = []

    # def index_patient(self, index):
    #     index = self.patients.index(Patient)

    def add_patients(self, firstname, lastname, age, condition):
        new_patient = Patient(firstname, lastname, age, condition)
        self.patients.append(new_patient)
        print(f"{new_patient}")


    def get_patient_list(self):
        return self.patients





# if __name__ == "__main__":
