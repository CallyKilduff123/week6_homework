# iteration 5 - current iteration


# TODO - create a clinic list

# create a clinic list
# add patients
# have a template for each patient to be added
# assign a category to each patient based on condition
# autopopulate investigations required for each category
# write the list to a txt file
# delete a patient off the list

# create a class called investigations first = base class
# the next class Patient will use (inherit) the output from this class = derived class to investigations
# but is base class to List
# the final class List will use (inherit) the output from patient

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
    #         Inside the __init__ method, i created a dictionary named category as an attribute of the instance.
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
# category is set to return an empty string unless filled. - otherwise you have to enter a value
# the hint in the variable name is to enter the key e.g. S for strabismus
class Patient:
    def __init__(self, firstname, lastname, age, condition, category_key):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.condition = condition
        self.category_key = category_key
    #     category key is to store the category


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
        lastname_line = f"Lastname: {self.lastname:<{padding}}"
        age_line = f"Age:".ljust(padding) + f"{self.age} years"
        condition_line = f"Condition: {self.condition:<{padding}}"

        # Combine all lines
        formatted_entry = (f"------------------------------------"
                           f"\n{firstname_line}\n{lastname_line}"
                           f"\n{age_line}\n{condition_line}\n"
                           f"------------------------------------")
        # return = used within a function to exit the function and pass back a value to the caller.
        # terminates funciton immediately
        # and the value in the return statement is sent back to the function's caller.
        return formatted_entry


# create final class called list - this inherits from the Patient class
# acts as a container for storing patient information.
# designed to hold multiple patient records
# initialise and don't pass any variables because creating a list - this list will be used to store the patient records.
class List:
    def __init__(self):
        self.patients = []

    # add patients method - used to add new patient records to the list.
    # The parameters represent the details of a patient that need to be provided
    # pass the data required for entry into the parameters
    def add_patients(self, firstname, lastname, age, condition, category_key):
        # new_patient... line creates a new instance of the Patient class, using the provided patient details.
        # This Patient instance represents one patient's record.
        new_patient = Patient(firstname, lastname, age, condition, category_key)
        # append adds the newly created Patient instance to the self.patients list,
        #  storing the patient's record in the list managed by the List class instance.
        self.patients.append(new_patient)
        print(f"{new_patient}")

    # The method's purpose is to remove a patient based on their first name and last name
    # (not entering all the other fields)
    # and then record this by appending a message in the clinic list txt file to say the patient did not attend
    def remove_patients(self, firstname, lastname):
        # found was added in this iteration as not previously working: A Boolean set to False.
        # aim is  to track whether the  patient was found to then be removed
        found = False
        # for loop to look through each record for patient matching the name
        # self.patients is the list containing all the patient records.
        # Each patient record is an object
        # person is the current patient object being examined in the loop.
        for person in self.patients:
            # if the firstname and lastname match the patient entered to be removed
            # found boolean switches to true - indicating a match
            if person.firstname == firstname and person.lastname == lastname:
                found = True
                # once found remove method applied to the person in the patient list
                self.patients.remove(person)
                # open the patient list and remove and write a message to say they DNA'd appointment
                # i didnt have this here before but it wouldn't work when i called the class
                # currently only half working - it removes the patient but doesnt write the message
                # i think this is because i open the file to write/overwrite later so the text is wiped
                # but i don't know how to change it
                with open("patients_list.txt", "a") as file:
                    file.write(f"DNA {person.firstname} {person.lastname}: unable to attend appointment.\n")
                #     break out of the loop
                break
        #         if the paient name is not in the list, print an error message
        if not found:
            with open("patients_list.txt", "a") as file:
                file.write(f"{firstname} {lastname} not found in the patient list.\n")

    # previous attempt: without the found boolean:
    # def remove_patients(self, firstname, lastname):
    #     for person in self.patients:
    #         if person.firstname == firstname and person.lastname == lastname:
    #             self.patients.remove(person)
    #             with open("patients_list.txt", "a") as file:
    #                 file.write(f"DNA {person.firstname} {person.lastname}: unable to attend appointment.\n")
    #             break

    # method to get the patient list and return the list of patients
    # i don't actually use this in this example
    def get_patient_list(self):
        return self.patients


# the main trick:
if __name__ == "__main__":
    # import List and investigations classes - i don't need to import the patient class
    # because it is used in the List class - not sure if that is right
    # i would need to import it if i updated patient details
    clinic = List()
    investigation = Investigations()

    # add patients to the list with a category key for their investigations
    # use add patients method in List class to add patients to the patient list (stored in clinic variable)
    clinic.add_patients("Elsa", "Agnarrsdottir", 20, "Esotropia", 'S')
    clinic.add_patients("Ana", "Agnarrsdottir", 18, "Esotropia", "S")
    clinic.add_patients("Olaf", "Snowsson", 3, "Optic nerve hypoplasia", "P")
    clinic.add_patients("Dory", "Fisherton", 47, "Exotropia", "S")
    clinic.add_patients("Kristoff", "Hansson", 22, "Arc eye", "A")
    clinic.add_patients("Mirabel", "Madrigal", 14, "Myopia", "R")

    # remove a patient from the list using their name only
    # use remove patient method in List class
    clinic.remove_patients("Dory", "Fisherton")
    # clinic.get_patient_list()

    # write the list to the txt file
    # 'with' scoops everything up and closes file at the end
    # open the file to write or overwrite - if i open to append to include the remove patient text - it duplicates the
    # list everytime i run the programme
    # write the title for the clinic
    # iterate over each patient in the clinic list
    # write their details as a string separated as a line
    # add the investigation details based on the key provided
    with open("patients_list.txt", "w") as file:
        file.write('CLINIC LIST:\n\n')
        for patient in clinic.patients:
            # Write patient details as a string (so they aren't printed as a list with brackets)
            # to the file with a line in between
            file.write(str(patient) + "\n")
            # Write investigations required for the patient's category
            # for each patient use the category key to fetch the matching investigation value
            # then write to the file
            investigation_details = investigation.get_category(patient.category_key)
            file.write(investigation_details + "\n------------------------------------\n")



