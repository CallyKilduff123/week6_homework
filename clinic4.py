# TODO - create a clinic list

# create a clinic list
# add patients
# have a template for each patient to be added
# assign a category to each patient based on condition
# autopopulate investigations required for each category
# write the list to a txt file
# delete a patient off the list

# create a class called investigations first
# the next class Patient will use the output from this class
# the final class List will use the output from patient

# Investigations class encapsulates all the attributes that are the 4 categories
# then a method is created to assign investigations to the categories

# create class
class Investigations:
    # The __init__ method is a special function in Python.
    # It's run automatically whenever a new instance of the class (in this case, an Investigations object) is created.
    # This method sets up the initial state of the object.
    def __init__(self):
        #  self parameter refers to the instance being created.
        #  It allows you to set and access the instance's attributes and methods.
        self.category = {
            'S': 'Strabismus patient. Investigations: VA--Orthoptics--Dilate--Refraction--Doctor',
            'R': 'Refractive patient. Investigations: VA--Orthoptics--Refraction',
            'A': 'Anterior segment patient. Investigations: VA--Doctor',
            'P': 'Posterior segment patient. Investigations: VA--Orthoptics--Dilate--OCT--OPTOS--Doctor'
        }
    #         Inside the __init__ method, a dictionary named category is created as an attribute of the instance.
    #         This dictionary maps single-letter keys to strings that describe different investigation categories

    # get_category method is designed to retrieve the details of a specific investigation category based on a key.
    # It takes one parameter, key, which is expected to be one of the letters 'S', 'R', 'A', or 'P'.
    # Inside the method, self.category.get(key) is called.
    # This is a way to fetch the value from the category dictionary using the provided key.
    # the value is returned
    def get_category(self, key):
        return self.category.get(key)


# new class called Patient created - this encapsulates all of the patient attributes)
# initialised Patient object - setting up the initial state of the object (as above)
# this class has 4 parameters that are required and one optional parameter (category_key)
# category is set to return an empty string unless filled.
# the hint in the variable name is to enter the key e.g. S for strabismus
class Patient:
    def __init__(self, firstname, lastname, age, condition, category_key=''):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.condition = condition
        self.category_key = category_key  # Store the category key


    # the __str__ method returns a string representation of the Patient object.
    # It's called automatically when you print the object or convert it to a string.
    # in the first iteration it just returned a string of patient details sep by lines
    # later iterations were formatted so that the patient details all started from the same place:
    def __str__(self):
        # Find the length of the longest label
        longest_label = max(len("Firstname"), len("Lastname"), len("Age"), len("Condition"))
        # Calculate padding for alignment
        padding = longest_label + 2
        # +2 for the colon and space

        # Format each line: create variable for each line and make an F string
        # including the detail heading e.g. firstname and then left adjusting the padding (len of the longest label+2)
        # so that all  the responses start at the same point
        # 2 ways of doing it: either using ljust or :< - both left adjust
        # firstname_line = f"Firstname:".ljust(padding) + f"{self.firstname}"
        firstname_line = f"Firstname: {self.firstname:<{padding}}"
        lastname_line = f"Lastname:".ljust(padding) + f"{self.lastname}"
        age_line = f"Age:".ljust(padding) + f"{self.age} years"
        condition_line = f"Condition:".ljust(padding) + f"{self.condition}"
        # category_line = f"Category: {self.category_key}"

        # Combine all lines
        formatted_entry = (f"------------------------------------"
                           f"\n{firstname_line}\n{lastname_line}"
                           f"\n{age_line}\n{condition_line}\n"
                           f"------------------------------------")
        # used within a function to exit the function and pass back a value to the caller.
        # When a return statement is executed, the function terminates immediately,
        # and the value specified in the return statement is sent back to the function's caller.
        return formatted_entry


# create final class called list -
# initialise and don't pass any variables because creating a list
class List:
    def __init__(self):
        self.patients = []

    # def add_patients(self, firstname, lastname, age, condition, category_key):
    #     new_patient = Patient(firstname, lastname, age, condition, category_key)
    #     self.patients.append(new_patient)
    def add_patients(self, firstname, lastname, age, condition, category_key):
        new_patient = Patient(firstname, lastname, age, condition, category_key)
        self.patients.append(new_patient)
        print(f"{new_patient}")

    def remove_patients(self, firstname, lastname):
        for person in self.patients[:]:
            if person.firstname == firstname and person.lastname == lastname:
                self.patients.remove(person)
            return person
                # print(f"DNA {person.firstname} {person.lastname}: unable to attend appointment.")
            # else:
            #     print("Patient not found")

    def get_patient_list(self):
        return self.patients


if __name__ == "__main__":
    clinic = List()
    investigation = Investigations()

    # Example of adding a patient with a category key
    clinic.add_patients("Elsa", "Agnarrsdottir", 20, "Esotropia", 'S')
    clinic.add_patients("Ana", "Agnarrsdottir", 18, "Esotropia", "S")
    clinic.add_patients("Olaf", "Snowsson", 3, "Optic nerve hypoplasia", "P")
    clinic.add_patients("Kristoff", "Hansson", 22, "Arc eye", "A")
    clinic.add_patients("Mirabel", "Madrigal", 14, "Myopia", "R")
    clinic.add_patients("Dory", "Fisherton", 47, "Exotropia", "S")
    clinic.remove_patients("Dory", "Fisherton")
    clinic.get_patient_list()

    # Continue adding patients as before, including the category_key in the arguments

    with open("patients_list.txt", "w") as file:
        file.write('CLINIC LIST:\n\n')
        for patient in clinic.patients:
            # Write patient details
            file.write(str(patient) + "\n")
            # Write investigation details for the patient's category
            investigation_details = investigation.get_category(patient.category_key)
            file.write(investigation_details + "\n------------------------------------\n")


