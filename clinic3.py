
class Patient:
    def __init__(self, firstname, lastname, age, condition):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.condition = condition
        # self.category = category

    # def update_category(self):
    #     category_descriptions = {
    #         'S': 'Strabismus patient. Investigations: VA--Orthoptics--Dilate--Refraction--Doctor',
    #         'R': 'Refractive patient. Investigations: VA--Orthoptics--Refraction',
    #         'A': 'Anterior segment patient. Investigations: VA--Doctor',
    #         'P': 'Posterior segment patient. Investigations: VA--Orthoptics--Dilate--OCT--OPTOS--Doctor'
    #     }
    #
    # # Prompt for category key
    #     category_key = input(
    #         'Enter S for strabismus, R for refractive error, A for anterior segment, P for posterior segment: ').upper()
    # # Auto-populate the category description based on the entered key
    #
    #     self.category = category_descriptions.get(category_key)


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
        # category_line = f"Category: {self.category}"


        # Combine all lines
        formatted_entry = (f"------------------------------------"
                         f"\n{firstname_line}\n{lastname_line}"
                         f"\n{age_line}\n{condition_line}\n"
                         f"------------------------------------")
        return formatted_entry

# class Investigations:
#     def __init__(self):
#         self.category_descriptions = {
#                 'S': 'Strabismus patient. Investigations: VA--Orthoptics--Dilate--Refraction--Doctor',
#                 'R': 'Refractive patient. Investigations: VA--Orthoptics--Refraction',
#                 'A': 'Anterior segment patient. Investigations: VA--Doctor',
#                 'P': 'Posterior segment patient. Investigations: VA--Orthoptics--Dilate--OCT--OPTOS--Doctor'
#             }
#
#         # Prompt for category key
#         category_key = input(
#             'Enter S for strabismus, R for refractive error, A for anterior segment, P for posterior segment: ').upper()
#         # Auto-populate the category description based on the entered key
#
#         self.category = self.category_descriptions.get(category_key)

class Investigations:
    def __init__(self):
        # This dictionary is defined as an instance attribute
        self.categories = {
            'S': 'Strabismus patient. Investigations: VA--Orthoptics--Dilate--Refraction--Doctor',
            'R': 'Refractive patient. Investigations: VA--Orthoptics--Refraction',
            'A': 'Anterior segment patient. Investigations: VA--Doctor',
            'P': 'Posterior segment patient. Investigations: VA--Orthoptics--Dilate--OCT--OPTOS--Doctor'
        }

    def print_category(self, key):
        # Check if the key exists in the dictionary
        if key in self.categories:
            print(self.categories[key])
        else:
            print("Other. Clinical team to decide on investigations")

class List:
    def __init__(self):
        self.patients = []

    def add_patients(self, firstname, lastname, age, condition):
        new_patient = Patient(firstname, lastname, age, condition)
        self.patients.append(new_patient)
        print(f"{new_patient}")

    def remove_patients(self, firstname, lastname):
        for patient in self.patients:
            if patient.firstname == firstname and patient.lastname == lastname:
                self.patients.remove(patient)
                print(f"DNA {patient.firstname} {patient.lastname}: "
                      "unable to attend appointment.\n"
                      "------------------------------------")
                break


    def get_patient_list(self):
        return self.patients

    # def __iter__(self):
    #     return iter(self.patients)




# if __name__ == "__main__":
#     clinic = List()
#     investigation = Investigations()
#     clinic.add_patients("Elsa", "Agnarrsdottir", 20, "Esotropia")
#     print(investigation.print_category('S'))
#     clinic.add_patients("Ana", "Agnarrsdottir", 18, "Esotropia")
#     print(investigation.print_category('S'))
#     clinic.add_patients("Olaf", "Snowsson", 3, "Optic nerve hypoplasia")
#     print(investigation.print_category('P'))
#     clinic.add_patients("Kristoff", "Hansson", 22, "Arc eye")
#     print(investigation.print_category('A'))
#     clinic.add_patients("Mirabel", "Madrigal", 14, "Myopia")
#     print(investigation.print_category('R'))
#     clinic.add_patients("Dory", "Fisherton", 47,"Exotropia")
#     clinic.remove_patients("Dory", "Fisherton")
#     clinic.get_patient_list()
#
#     with open("patients_list.txt", "w") as file:
#         title = file.write('CLINIC LIST:\n\n')
#         for new_patient in clinic.patients:  # Directly iterate over clinic.patients
#             file.write(str(new_patient) + "\n")
#             file.write(str(investigation.print_category) + "\n")
