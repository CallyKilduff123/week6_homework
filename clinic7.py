# iteration 7 - current iteration
# did not inherit patient to list - kept seperate


# TODO - create a clinic list

# create a clinic list
# add patients
# have a template for each patient to be added
# assign a category to each patient based on condition
# autopopulate investigations required for each category
# write the list to a txt file
# delete a patient off the list

# create class

# new class called Patient created - this encapsulates all of the patient attributes)
# initialised Patient object - setting up the initial state of the object (as above)
# this class has 5 parameters
# category key - is because category is a dictionary -
# its the hint in the variable name is to enter the key e.g. S for strabismus
class Patient:
    def __init__(self, firstname, lastname, age, condition, category_key):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.condition = condition
        self.category_key = category_key
    #     category key is to store the category

        self.category = {
            'S': 'Strabismus patient. Investigations: VA--Orthoptics--Dilate--Refraction--Doctor',
            'R': 'Refractive patient. Investigations: VA--Orthoptics--Refraction',
            'A': 'Anterior segment patient. Investigations: VA--Doctor',
            'P': 'Posterior segment patient. Investigations: VA--Orthoptics--Dilate--OCT--OPTOS--Doctor'}

    # the __str__ method returns a string representation of the Patient object.
    # It's called automatically when you print the object or convert it to a string.
    # in the first iteration it just returned a string of patient details sep by lines
    # later iterations were formatted so that the patient details all started from the same place:
    def __str__(self):
        # Find the length of the longest label
        longest_label = max(len("Firstname"), len("Lastname"), len("Age"), len("Condition"), len("Investigations") + 2)
        # Calculate padding for alignment
        padding = longest_label + 2
        # +2 for the colon and space

        # Format each line: create variable for each line and make an F string
        # including the detail heading e.g. firstname and then left adjusting the padding (len of the longest label+2)
        # so that all  the responses start at the same point
        # 2 ways of doing it: either using ljust or :< - both left adjust
        firstname_line = f"Firstname:".ljust(padding) + f"{self.firstname}"
        lastname_line = f"Lastname:".ljust(padding) + f"{self.lastname}"
        age_line = f"Age:".ljust(padding) + f"{self.age} years"
        condition_line = f"Condition:".ljust(padding) + f"{self.condition}"
        # The get() method returns the value of the item with the specified key in a dictionary
        # dictionary.get(keyname, value) -keyname is compulsory and value is optional - default is None if no key
        investigation_line = self.category.get(self.category_key)

        # Combine all lines
        formatted_entry = (f"------------------------------------"
                           f"\n{firstname_line}\n{lastname_line}"
                           f"\n{age_line}\n{condition_line}\n"
                           f"------------------------------------\n"
                           f"{investigation_line}\n"
                           f"------------------------------------")
        # return = used within a function to exit the function and pass back a value to the caller.
        # terminates funciton immediately
        # and the value in the return statement is sent back to the function's caller.
        return formatted_entry


# create final class called list - this inherits from the Patient class
# acts as a container for storing patient information.
# designed to hold multiple patient records
# initialise and don't pass any variables because creating a list - this list will be used to store the patient records

# dont inherit Patient class in List class
# a list of patients (a collection) doesn't have an "is-a" relationship with a single patient but rather has patients..
# Instead of inheriting from Patient, create a separate class to manage the collection of patients.
# This class will use composition by containing a list of Patient instances
# they now have individual responsibilities—Patient for storing individual patient data
# List for managing the collection of patients.
class List:
    def __init__(self):
        self.patients = []

    def add_patients(self, firstname, lastname, age, condition, category_key):
        new_patient = Patient(firstname, lastname, age, condition, category_key)
        self.patients.append(new_patient)
        print(f"{new_patient}")

    def get_patients(self):
        for person in self.patients:
            print(person)

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

    # method to get the patient list and return the list of patients
    # i don't actually use this in this example
    def get_patient_list(self):
        return self.patients


# the main trick:
if __name__ == "__main__":
    # import List and investigations classes

    clinic = List()
    patient = Patient(firstname=(), lastname=(), age=(), condition=(), category_key=())

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
    with open("patients_list.txt", "a") as file:
        file.write('CLINIC LIST:\n\n')
        for patient in clinic.patients:
            # Write patient details as a string (so they aren't printed as a list with brackets)
            # to the file with a line in between
            file.write(str(patient) + "\n")
#             if I append it brings through the removed message but it writes the whole file again
