# # OLD CODE  - iteration 2
# formatted the output for the class Patient
# left category out

class Patient:
    def __init__(self, firstname, lastname, age, condition):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.condition = condition



    def __str__(self):
        # Find the length of the longest label
        longest_label = max(len("Firstname"), len("Lastname"), len("Age"), len("Condition"))

        # Calculate padding for alignment
        padding = longest_label + 2  # +2 for the colon and space

        # Dynamically format each line
        firstname_line = f"Firstname:".ljust(padding) + f"{self.firstname}"
        lastname_line = f"Lastname:".ljust(padding) + f"{self.lastname}"
        age_line = f"Age:".ljust(padding) + f"{self.age} years"
        condition_line = f"Condition:".ljust(padding) + f"{self.condition}"



        # Combine all lines
        formatted_str = (f"------------------------------------"
                         f"\n{firstname_line}\n{lastname_line}"
                         f"\n{age_line}\n{condition_line}\n"
                         f"------------------------------------")
        return formatted_str



class List:
    def __init__(self):
        self.patients = []

    def add_patients(self, firstname, lastname, age, condition):
        new_patient = Patient(firstname, lastname, age, condition)
        self.patients.append(new_patient)
        print(f"{new_patient}")

    def get_patient_list(self):
        return self.patients

    # def __iter__(self):
    #     return iter(self.patients)



# if __name__ == "__main__":
#     clinic = List()
#     clinic.add_patients("Elsa", "Agnarrsdottir", 20, "Esotropia")
#     clinic.add_patients("Ana", "Agnarrsdottir", 18, "Esotropia")
#     clinic.add_patients("Olaf", "Snowsson", 3, "Optic nerve hypoplasia")
#     clinic.add_patients("Kristoff", "Hansson", 22, "Arc eye")
#     clinic.add_patients("Mirabel", "Madrigal", 14, "Myopia")
#
#     clinic.get_patient_list()

    # with open("patients_list.txt", "w") as file:
    #     title = file.write('CLINIC LIST:\n\n')
    #     for new_patient in clinic.patients:  # Directly iterate over clinic.patients
    #         file.write(str(new_patient) + "\n")


