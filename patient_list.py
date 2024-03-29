from clinic7 import List
from clinic7 import Patient

clinic = List()
patient = Patient(firstname=(), lastname=(), age=(), condition=(), category_key=())

# add patients to the list with a category key for their investigations
clinic.add_patients("Elsa", "Agnarrsdottir", 20, "Esotropia", 'S')
clinic.add_patients("Ana", "Agnarrsdottir", 18, "Esotropia", "S")
clinic.add_patients("Olaf", "Snowsson", 1, "Optic nerve hypoplasia", "P")
clinic.add_patients("Kristoff", "Hansson", 22, "Arc eye", "A")
clinic.add_patients("Mirabel", "Madrigal", 14, "Myopia", "R")
clinic.add_patients("Dory", "Fisherton", 47, "Exotropia", "S")

# remove a patient from the list using their name only
clinic.remove_patients("Dory", "Fisherton")
clinic.get_patients()

# Continue adding patients as before, including the category_key in the arguments

with open("patients_list.txt", "w") as file:
    file.write('CLINIC LIST:\n\n')
    for patient in clinic.patients:
        # Write patient details
        file.write(str(patient) + "\n")


#
