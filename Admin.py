from Doctor import Doctor
from Patient import Patient
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import numpy as np
class Admin:
    """A class that deals with the Admin operations"""
    def __init__(self, username = '', password = '', address = ''):
        """
        Args:
            username (string): Username
            password (string): Password
            address (string, optional): Address Defaults to ''
        """

        self.__username = username
        self.__password = password
        self.__address =  address

    def write_admin_data_in_file(self):
        try:
            with open("./Database/admin_data.txt",'w') as file:
                file.write(f'{self.__username}|{self.__password}|{self.__address}\n')

        except FileNotFoundError:
            print("Database Not Found")

    def extract_admin_data(self):
        try:
            with open("./Database/admin_data.txt",'r') as file:
                data_in_lines = file.readlines()
                for line in data_in_lines:
                    values = line.strip().split('|')
                    if len(values) == 3:
                        username, password, address = values
                        return username, password, address
        except FileNotFoundError:
            print("Admin data not found")

    def update_values_in_file(cls,index,updated_value,file_address,element_index=0):
            try:
                with open(f"./Database/{file_address}.txt", "r") as file:
                    data_in_lines = file.readlines()

                if index >= len(data_in_lines):
                    print("Invalid Index")
                    return

                data = data_in_lines[index].strip().split("|")
                data[element_index] = updated_value
                data_in_lines[index] = "|".join(data) + '\n'

                with open(f"./Database/{file_address}.txt", "w") as file:
                    file.writelines(data_in_lines)

            except FileNotFoundError:
                print(f"{file_address} file not found.")

    def view(self,a_list):
        """
        print a list
        Args:
            a_list (list): a list of printables
        """
        for index, item in enumerate(a_list):
            print(f'{index+1:3}|{item}')

    def login(self) :
        self.__username,self.__password,self.__address = self.extract_admin_data()
        """
        A method that deals with the login
        Raises:
            Exception: returned when the username and the password ...
                    ... don`t match the data registered
        Returns:
            string: the username
        """
    
        print("-----Login-----")
        #Get the details of the admin

        username = input('Enter the username: ')
        password = input('Enter the password: ')

        # check if the username and password match the registered ones
        #ToDo1
        if username == self.__username and password == self.__password:
            print("Login Successful")
            return True

    def find_index(self,index,doctors):
        
            # check that the doctor id exists          
        if index in range(0,len(doctors)):
            
            return True

        # if the id is not in the list of doctors
        else:
            return False
            
    def get_doctor_details(self) :
        """
        Get the details needed to add a doctor
        Returns:
            first name, surname and ...
                            ... the speciality of the doctor in that order.
        """
        #ToDo2
        first_name = input("Enter Doctor's First Name: ")
        surname = input("Enter Doctor's Surname: ")
        speciality = input("Enter Doctor's Speciality: ")

        return first_name,surname,speciality
    
    def get_patient_details(self):
        """
        this method here is to take inputs from the patient
        for adding details into the patient data
        """
        first_name = input("Enter Patient's First Name: ")
        surname = input("Enter Patient's Surname: ")
        age = int(input("Enter Patient's age: "))
        mobile = input("Enter Patients MobileNumber: ")
        address = input("Enter Patient's Address: ")
        symptoms = (input("Enter Patient's Symptoms separated with commas: "))
        symptom = symptoms.strip()
        
        return first_name,surname,age,mobile,address,symptom
    

    def extract_data(self,file_address):
        data_list = []
        try:
            with open(f"./Database/{file_address}.txt",'r') as file:
                 for line in file:
                      if line.strip(): #this line of code is helping to skip any blank lines in the file 
                        values = line.strip().split('|') #this line of code is to store values in a list at first removing white spaces from line and then creating list on the basis of comma as a separator
                        if len(values) == 3:
                            first_name, surname, speciality = values
                            data_list.append(Doctor(first_name,surname,speciality))
                    

                        elif len(values) >= 6:
                            first_name,surname,age,mobile,address,symptoms,doctor = values
                            data_list.append(Patient(first_name,surname,age,mobile,address,symptoms,doctor))

                        else:
                            return
            return data_list
        except FileNotFoundError:
             print("Doctor data not found")


    def view_patient(self,iterable_list):
        
        """
        print a list of patients
        Args:
            patients (list<Patients>): list of all the active patients
        """
        print("-----View Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     |    Postcode   |    Symptoms   | ')
        #ToDo10
        self.view(iterable_list)

    def doctor_management(self):
        doctors = self.extract_data("doctor_data")

        
        """
        A method that deals with registering, viewing, updating, deleting doctors
        Args:
            doctors (list<Doctor>): the list of all the doctors names
        """

        print("-----Doctor Management-----")

        # menu
        print('Choose the operation:')
        print(' 1 - Register')
        print(' 2 - View')
        print(' 3 - Update')
        print(' 4 - Delete')

        #ToDo3
        op = input('Enter the task to perform: ')


        # register
        if op == '1':
            print("-----Register-----")

            # get the doctor details
            print('Enter the doctor\'s details:')
            #ToDo4
            first_name,surname,speciality = self.get_doctor_details()
            # check if the name is already registered
            name_exists = False
            for doctor in doctors:
                if first_name == doctor.get_firstname() and surname == doctor.get_surname():
                    print('Name already exists.')
                    #ToDo5
                    break # save time and end the loop

            #ToDo6
            else:
                newdoctor = Doctor(first_name,surname,speciality)
                newdoctor.write_doctor_data_in_file()
                # doctors.append(newdoctor)
                                             # ... to the list of doctors
                print('Doctor registered.')

        # View
        elif op == '2':
            print("-----List of Doctors-----")
            #ToDo7
            self.view(doctors)

        # Update
        elif op == '3':

            file_address = "doctor_data"
             
            while True:
                print("-----Update Doctor`s Details-----")
                print('ID |          Full name           |  Speciality')
                self.view(doctors)
                try:
                    index = int(input('Enter the ID of the doctor: ')) - 1
                    doctor_index=self.find_index(index,doctors)
                    if doctor_index!=False:
                        break
                    else:
                        print("Doctor not found")
                        # doctor_index is the ID mines one (-1)
                    
                except ValueError: # the entered id could not be changed into an int
                    print('The ID entered is incorrect')

            # menu
            print('Choose the field to be updated:')
            print(' 1 First name')
            print(' 2 Surname')
            print(' 3 Speciality')
            op = input('Input: ') 

            #ToDo8   
            if op == '1':
                updated_first_name = input("Enter the Doctor's First name to update: ")
                Doctor.update_values_in_file(index,updated_first_name,file_address,element_index=0)
 
            elif op == '2':    
                updated_surname = input("Enter the Doctor's Surname to update: ")
                Doctor.update_values_in_file(index,updated_surname,file_address,element_index=1)
                

            elif op == '3':
                updated_speciality = input("Enter the Doctor's speciality to update: ")
                Doctor.update_values_in_file(index,updated_speciality,file_address,element_index=2)

            else:
                print("Your Choose of field is invalid")
                    
        # Delete
        elif op == '4':
            print("-----Delete Doctor-----")
            print('ID |          Full Name           |  Speciality')
            self.view(doctors)

            doctor_index = int(input('Enter the ID of the doctor to be deleted: '))-1
            #ToDo9
            val = self.find_index(doctor_index,doctors)
            if val:
                doctors.pop(doctor_index)
                Doctor.delete_doctor_data(doctors)
                print("Doctor's detail is deleted from the system")
            else:
                print('The id entered is incorrect')

        # if the id is not in the list of patients
        else:
            print('Invalid operation choosen. Check your spelling!')

    def patient_management(self):
        patients = self.extract_data("patient_data")

        print("-----Patient Management-----")

        # menu
        print('Choose the operation:')
        print(' 1 - Register')
        print(' 2 - View')
        print(' 3 - Update')

        op = input("Enter the choice: ")

        if op == '1':
            print("----Register Patient----")

            print('Enter the Patient\'s details:')
            first_name,surname,age,mobile,address,symptoms = self.get_patient_details()
            # check if the name is already registered
            name_exists = False
            for patient in patients:
                if first_name == patient.get_firstname() and surname == patient.get_surname() and age == patient.get_age() and mobile == patient.get_mobile() and address == patient.get_address() and symptoms == patient.print_symptoms():
                    print('Patient Data already exists in the system.')
                    #ToDo5
                    break # save time and end the loop

            #ToDo6
            else:
                newpatient = Patient(first_name,surname,age,mobile,address,symptoms,doctor="Doctor Not Assigned")
                newpatient.write_patient_data_in_file()
                # patients.append(newpatient)
                                             # ... to the list of doctors
                print('patient registered.')
        
        elif op == '2':

            self.view_patient(patients)

        elif op == '3':
            file_address = "patient_data"
            while True:
                print("-----Update Patient`s Details-----")
                self.view_patient(patients)
                try:
                    index = int(input('Enter the ID of the Patient: '))- 1
                    patient_index=self.find_index(index,patients)
                    if patient_index!=False:
                        break
                    else:
                        print("Doctor not found")
                        # doctor_index is the ID mines one (-1)
                    
                except ValueError: # the entered id could not be changed into an int
                    print('The ID entered is incorrect')

            # menu
            print('Choose the field to be updated:')
            print(' 1 First name')
            print(' 2 Surname')
            print(' 3 Age')
            print(' 4 Mobile')
            print(' 5 Address')
            print(' 6 Symptoms')
            
            op = input('Input: ') 

            #ToDo8   
            if op == '1':
                updated_first_name = input("Enter the Patient's First name to update: ")
                Patient.update_values_in_file(index,updated_first_name,file_address,element_index=0)
                
            elif op == '2':    
                updated_surname = input("Enter the Patient's Surname to update: ")
                Patient.update_values_in_file(index,updated_surname,file_address,element_index=1)
                

            elif op == '3':
                updated_age = input("Enter the Patient's age to update: ")
                Patient.update_values_in_file(index,updated_age,file_address,element_index=2)

            elif op == '4':
                updated_mobile = input("Enter the Patient's mobile to update: ")
                Patient.update_values_in_file(index,updated_mobile,file_address,element_index=3)

            elif op == '5':
                updated_address = input("Enter the Patient's Address to update: ")
                Patient.update_values_in_file(index,updated_address,file_address,element_index=4)

            elif op == '6':
                updated_symptoms = input("Enter the Patient's Symptoms to update: ")
                updated_symptom = updated_symptoms.strip()
                Patient.update_values_in_file(index,updated_symptom,file_address,element_index=5)

            else:
                print(f"{op}:this Choose of field is invalid")

        else:
            print("Invalid operation Choosen")




    def assign_doctor_to_patient(self):
        doctors = self.extract_data("doctor_data")
        patients = self.extract_data("patient_data")

        """
        Allow the admin to assign a doctor to a patient
        Args:
            patients (list<Patients>): the list of all the active patients
            doctors (list<Doctor>): the list of all the doctors
        """
        print("-----Assign-----")

        self.view_patient(patients)

        patient_index = input('Please enter the patient ID: ')

        try:
            # patient_index is the patient ID mines one (-1)
            patient_index = int(patient_index) -1

            # check if the id is not in the list of patients
            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return # stop the procedures

        except ValueError: # the entered id could not be changed into an int
            print('The id entered is incorrect')
            return # stop the procedures

        print("-----Doctors Select-----")
        print('Select the doctor that fits these symptoms:')
        print(patients[patient_index].print_symptoms()) # print the patient symptoms

        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)
        doctor_index = input('Please enter the doctor ID: ')

        try:
            # doctor_index is the patient ID mines one (-1)
            doctor_index = int(doctor_index) -1
            # check if the id is in the list of doctors
            if self.find_index(doctor_index,doctors)!=False:
                
                    
                # link the patients to the doctor and vice versa
                #ToDo11
                
                doctor_full_name = doctors[doctor_index].full_name()
                patients[patient_index].link(doctor_full_name)
                doctors[doctor_index].add_patient(patients[patient_index])
                Patient.update_values_in_file(patient_index,doctor_full_name,"patient_data",6)

                print('The patient is now assign to the doctor.')

            # if the id is not in the list of doctors
            else:
                print('The id entered was not found.')

        except ValueError: # the entered id could not be changed into an in
            print('The id entered is incorrect')


    def relocating_doctor(self):
        doctors = self.extract_data("doctor_data")
        patients = self.extract_data("patient_data")
        """
        Reassigning doctor to a patient
        """

        print("-----Re-Assigning Doctor to Patient-----")

        self.view_patient(patients)
        try:
            patient_index = int(input('Please enter the patient ID: '))-1
            # check if the id is not in the list of patients
            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return # stop the procedures

        except ValueError:
            print('The id entered is incorrect')
            return # stop the procedures
        
        old_doctor = patients[patient_index].get_doctor()

        if old_doctor == "Doctor Not Assigned":
            print("Doctor has not been assigned.")
            val = input("Do you want to assign doctor yes or no (y/n): ")
            if val.lower() == 'yes' or val.lower() == 'y':
                self.assign_doctor_to_patient()
            else:
                return
            
        print(f'Current Doctor: Dr.{old_doctor}')
        print("----- Select New Doctor -----")
        print('Select the doctor that fits these symptoms:')
        print(patients[patient_index].print_symptoms()) # print the patient symptoms

        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)

        try:
            # check if the id is in the list of doctor
            doctor_index = int(input('Please enter the patient ID: '))-1
            # check if the id is not in the list of patients
            if doctor_index not in range(len(doctors)):
                print('The id entered was not found.')
                return # stop the procedures

        except ValueError:
            print('The id entered is incorrect')
            return # stop the procedures
                # link the patients to the doctor and vice versa
                #ToDo11
            
        new_doctor = doctors[doctor_index].full_name()

        if new_doctor == old_doctor:
            print("Doctor is already assigned !!!")
            return
        
        for doctor in doctors:
            if doctor.full_name() == old_doctor:
                doctors[doctor_index].remove_patient(patient_index)

        patients[patient_index].link(new_doctor)
        doctors[doctor_index].add_patient(patients[patient_index])
        Patient.update_values_in_file(patient_index,new_doctor,"patient_data",6)

        print(f'The patient has been reassigned to Dr. {new_doctor}')
    



    def grouping_patients_based_on_familynames(self):
        """
        Admin can call for viewing patients based on Family Name 
        Print the list of patients based on Family Names
        """
        patients = self.extract_data("patient_data")
        patientDict = {}
        for patient in patients:
            family_name = patient.get_surname()
            if family_name in patientDict:
                patientDict[family_name].append(patient)
            else:
                patientDict[family_name] = [patient]         
        print("-------Patient Grouped on Family Name-------")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     |    Postcode   |    Symptoms   | ')
        for family_name, members in patientDict.items():
            print(f"Family Name: {family_name}")
            for index,patient in enumerate(members):
                print(f'{index+1:>3}){patient.full_name():^30}|{patient.get_doctor():^30}|{patient.get_age():^5}|{patient.get_mobile():^15}|{patient.get_address():^15}|{patient.print_symptoms():^15}|')
                print()

    def group_patient_by_symptom(self):

        patients = self.extract_data("patient_data")
        Dictionary_for_illness = {}
        for patient in patients:
            for symptom in patient.print_symptoms().split(', '):
                symptom = symptom.lower()
                if symptom in Dictionary_for_illness:
                    Dictionary_for_illness[symptom].append(patient)
                else:
                    Dictionary_for_illness[symptom] = [patient]

        return Dictionary_for_illness


#################### Method to Display Patients on the basis of Same Family Group ###############################
    def display_grouped_patient_by_symptom(self):
        Dictionary_for_illness = self.group_patient_by_symptom()

        print("-------Patient Grouped on Illness-------")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     |    Postcode   |    Symptoms   | ')
        for symptoms, patient_data in Dictionary_for_illness.items():
            print(f"Illness: {symptoms}")
            count = 0
            for index,patient in enumerate(patient_data):
                print(f'{index+1:>3}){patient.full_name():^30}|{patient.get_doctor():^30}|{patient.get_age():^5}|{patient.get_mobile():^15}|{patient.get_address():^15}|{symptoms:^15}|')
                print()
    
#################### Method to Return Dictionary for key:Symptom Value: Number of Patients ###############################
    def patient_symptom_count(self):
        Dictionary_for_illness = self.group_patient_by_symptom()
        Dictionary_for_count = {}
        for symptom,patient in Dictionary_for_illness.items():
            Dictionary_for_count[symptom] = len(patient)

        return Dictionary_for_count

#################### Method For Discharging Patients ###############################
    def discharge(self):
        discharged_patients = self.extract_data("dischargedpatient_data")
        """
        Allow the admin to discharge a patient when treatment is done
        Args:
            patients (list<Patients>): the list of all the active patients
            discharge_patients (list<Patients>): the list of all the non-active patients
        """
        patients = self.extract_data("patient_data")
        print("-----Discharge Patient-----")

        patient_index = int(input('Please enter the patient ID: '))-1

        index_to_check = self.find_index(patient_index,patients)
        if index_to_check == True:
            discharged_patients.append(patients[patient_index])
            Patient.write_in_dischargedfile(discharged_patients)
            del patients[patient_index]
            Patient.after_discharge_data(patients)
        else:
            print("Given Index is not a valid")
        

#################### Method For Viewing Discharged Patients ###############################
    def view_discharge(self):
        """
        Prints the list of all discharged patients
        Args:
            discharge_patients (list<Patients>): the list of all the non-active patients
        """
        discharged_patients = self.extract_data("dischargedpatient_data")
        print("-----Discharged Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     |    Postcode   |    Symptoms   | ')
        #ToDo13
        self.view(discharged_patients)


    def book_an_appointment(self):
        # Get patient data
        patients = self.extract_data("patient_data")
        self.view_patient(patients)
        
        try:
            patient = patients[int(input('Enter Patient ID: ')) - 1]
        except (ValueError, IndexError):
            print("Invalid Patient ID")
            return

        # Check doctor assignment
        doctor = patient.get_doctor()
        if doctor == "Doctor Not Assigned":
            print("Doctor not assigned. Assign a doctor first.")
            return
        
        print(f"\nPatient is assigned to Dr. {doctor}")

        # Generate available dates (excluding weekends)
        today = datetime.today()
        available_dates = [
            today + timedelta(days=day) for day in range(1, 31)
            if (today + timedelta(days=day)).weekday() < 5
        ]

        # Display available dates
        print("\nAvailable Dates:")
        for idx, date in enumerate(available_dates, 1):
            print(f"{idx}. {date.strftime('%Y-%m-%d (%A)')}")
        
        try:
            selected_date = available_dates[int(input("\nChoose a date (number): ")) - 1]
        except (ValueError, IndexError):
            print("Invalid selection")
            return

        # Read existing appointments
        booked_slots = set()
        try:
            with open('./Database/appointment_data.txt', 'r') as file:
                booked_slots = {
                    parts[3] for parts in (line.strip().split('|') for line in file)
                    if parts[0] == doctor and parts[2] == selected_date.strftime('%Y-%m-%d')
                }
        except FileNotFoundError:
            pass

        # Determine available slots
        all_slots = ["9-10", "10-11", "13-14", "14-15"]
        available_slots = [slot for slot in all_slots if slot not in booked_slots]

        if not available_slots:
            print("No available slots for this date.")
            return

        # Display available slots
        print(f"\nAvailable Slots for {selected_date.strftime('%Y-%m-%d')}:")
        for idx, slot in enumerate(available_slots, 1):
            print(f"{idx}. {slot}")

        try:
            selected_slot = available_slots[int(input("\nChoose a slot (number): ")) - 1]
        except (ValueError, IndexError):
            print("Invalid selection")
            return

        # Confirm booking
        if input(f"Confirm appointment on {selected_date.strftime('%Y-%m-%d')} at {selected_slot}? (y/n): ").lower() == 'y':
            with open('./Database/appointment_data.txt', 'a') as file:
                file.write(f"{doctor}|{patient.full_name()}|{selected_date.strftime('%Y-%m-%d')}|{selected_slot}|Booked\n")
            print("Appointment booked successfully!")
        else:
            print("Booking cancelled")


    def made_dictionary_to_store_doctor_as_key_and_month_as_value(self):

        doctor_dict = {}
        empty_list = []
        try:
            with open("./Database/appointment_data.txt",'r') as file:
                data_in_lines = file.readlines()
                counter = 0
                for line in data_in_lines:
                   empty_list.append(line.strip().split('|'))
                for data in empty_list:
                    doctor_name = data[0]
                    date = data[2]
                    date = date.strip().split('-')
                    month = date[1]
                    if doctor_name in doctor_dict:
                        doctor_dict[doctor_name].append(month)
                    else:
                        doctor_dict[doctor_name] = [month]

                return doctor_dict

        except FileNotFoundError:
            print("Appointment Data Not Found")
            return
        

    def made_dictionary_to_store_doctor_as_key_and_number_of_patient_as_value(self):
        patients = self.extract_data("patient_data")
        empty_dict = {}
        for patient in patients:
            doctor_name = patient.get_doctor()
            if doctor_name == "Doctor Not Assigned":
                continue
            else:
                if doctor_name in empty_dict:
                    empty_dict[doctor_name] += 1
                else:
                    empty_dict[doctor_name] = 1
        return empty_dict


    def data_representation_of_doctor_and_month(self):
        appointment_data = self.made_dictionary_to_store_doctor_as_key_and_month_as_value()
        appointment_month_count_dict = {}
        for key,value in appointment_data.items():
            appointment_month_count_dict[key] = {}
            for month in value:
                if month in appointment_month_count_dict[key]:
                    appointment_month_count_dict[key][month] += 1
                else:
                    appointment_month_count_dict[key][month] = 1
                    
        return appointment_month_count_dict

    
#################### Method For Printing Management Report Request By Admin ###############################
    def management_report(self):

        """
        this function is to display the management report
        it will display the following:
        Total number of doctors in the system
        Total number of patients per doctor
        Total number of appointments per month per doctor
        Total number of patients based on the illness type
        """
        doctors = self.extract_data("doctor_data")
        number_of_doctor = len(doctors)
        dictionary_of_count = self.patient_symptom_count()
        appointment_data = self.data_representation_of_doctor_and_month()
        dictionary_of_doctor_and_patient = self.made_dictionary_to_store_doctor_as_key_and_number_of_patient_as_value()
        print('\n')
        print("{:-^70}".format("Management Report")) 
        print("{:_^70}".format(""))
        print("|     Total Numbers of Doctors        |{:^30}|".format(number_of_doctor))
        print("{:-^70}".format(""))
        print("{:_^70}".format(""))
        print("|           Name of Doctor            |     Number of Patients       |")
        print("{:-^70}".format(""))
        for doctor in doctors:
            for key,value in dictionary_of_doctor_and_patient.items():
                if doctor.full_name() == key:
                    print(f"|  Dr.{doctor.full_name():<32}|{value:^30}|")

            if doctor.full_name() not in dictionary_of_doctor_and_patient:
                print(f"|  Dr.{doctor.full_name():<32}|{'0':^30}|")
        print("{:-^70}".format(""))
        print("{:_^70}".format(""))
        print("|     Name of Doctor      |     Month    |   Number of Appointments  |")
        print("{:-^70}".format(""))
        for key,value in appointment_data.items():
            for month,count in value.items():
                if month == '01':
                    month = 'January'
                elif month == '02':
                    month = 'February'
                elif month == '03':
                    month = 'March'
                elif month == '04':
                    month = 'April'
                elif month == '05':
                    month = 'May'
                elif month == '06':
                    month = 'June'
                elif month == '07':
                    month = 'July'
                elif month == '08':
                    month = 'August'
                elif month == '09':
                    month = 'September'
                elif month == '10':
                    month = 'October'
                elif month == '11':
                    month = 'November'
                elif month == '12':
                    month = 'December'
                else:
                    month = 'Invalid Month'
                
                print(f"| Dr.{key:<21}|{month:^14}|{count:^27}|")
            print("{:-^70}".format(""))     
        print("{:_^70}".format(""))
        print("|           Symptoms             |          Number of Patients       |")
        print("{:-^70}".format(""))
        for key,value in dictionary_of_count.items():
            if key is not None:
                print(f"|{key.capitalize():^32}|{value:^35}|")
        print("{:-^70}".format(""))

        


#################### Method For Updatin Admin Details ###############################
    def update_details(self):
        """
        Allows the user to update and change username, password and address
        """
        print('Choose the field to be updated:')
        print(' 1 Username')
        print(' 2 Password')
        print(' 3 Address')
        op = int(input('Input: '))

        if op == 1:
            #ToDo14
            while True:
                updated_username = input('Enter the new username: ')
                if updated_username == self.__username:
                    print("Username is already taken")
                elif updated_username != self.__username:
                    self.update_values_in_file(0,updated_username,"admin_data",element_index=0) 
                    break
                else:
                    print("Invalid input is given")
                
        elif op == 2:
            while True:
                updated_password = input('Enter the new password: ')
                if updated_password == self.__password:
                    print("Password is already in used")
                elif updated_password!= self.__password:
                    self.update_values_in_file(0,updated_password,"admin_data",element_index=1)    
                    break
                else:
                    print("Invalid input is given")

        elif op == 3:
            #ToDo15
            doctor_address = input('Enter your address: ')
            self.update_values_in_file(0,doctor_address,"admin_data",element_index=2)

        else:
            #ToDo16
            print("Invalid Input")



    def display_graphical_diagram_of_maagement_report(self):

        """
            To Display Graphical Data using Matplotlib using class: Pyplot
            Use of arrange function of numpy to create a range of values for x-axis
            Usual range function with list comprehension shows TypeError
            To display the data the data needs to be in the <list> format
            Due to this lots of empty lists are created at first to store the data
        """
        doctors = self.extract_data("doctor_data")
        dictionary_of_doctor_and_patient = self.made_dictionary_to_store_doctor_as_key_and_number_of_patient_as_value()
        appointment_Data = self.data_representation_of_doctor_and_month()
        dictionary_of_count = self.patient_symptom_count() # a dictionary where key is a symptom and value is count of patient with that symptom
        name_of_doctors = [] #an empty list to store the name of doctors
        patients_per_doctor = [] #an empty list to store the number of patients per doctor
        name_of_symptoms = [] #an empty list to store the type of symptoms
        number_of_patients_per_Symptoms = [] #an empty list to store number of patients per symptoms
        months = ['February','March'] # the month here is only two cause user can only choose between feb to march date for appointment

        # This block of code is to store the name of doctors in the list(<name_of_doctors>)
        for doctor in doctors:
            name_of_doctors.append(doctor.full_name())

        # This block of code is to store the number of patients per doctor in the list(<patients_per_doctor>)
        for i in range(0,len(name_of_doctors)):
            for key,value in dictionary_of_doctor_and_patient.items():
                if name_of_doctors[i] == key:
                    patients_per_doctor.append(value)
            if name_of_doctors[i] not in dictionary_of_doctor_and_patient:
                patients_per_doctor.append(0)
        
        # This block of code is to store the number of appointments per month per doctor in the list(<appointments>)
        appointments = [[0 for i in range(0,len(months))] for index in range(0,len(name_of_doctors))] # a 2D list to store the number of appointments per month per doctor
        for doctor in doctors:
            for key,value in appointment_Data.items():
                if doctor.full_name() == key:
                    for month,count in value.items():
                        if month == '02':
                            appointments[name_of_doctors.index(key)][0] = count
                        if month == '03':
                            appointments[name_of_doctors.index(key)][1] = count

        # This block of code is to store the type of symptoms in the list(<name_of_symptoms>)
        for key,value in dictionary_of_count.items():
            if key is not None:
                name_of_symptoms.append(key.capitalize())
                number_of_patients_per_Symptoms.append(value)

        # this block of code here is to diplay piechart showing total number of doctors in the hospital
        total_doctors = len(doctors)
        sizes = [total_doctors]
        colors = ['skyblue']
        plt.pie(sizes, colors=colors, startangle=90)
        plt.title('Total Number of Doctors in the Hospital',fontsize=18)
        plt.text(0, 0, f'{total_doctors}', ha='center', va='center', fontsize=40, color='black')
        plt.axis('equal')
        plt.show()

        # this block of code here is to display bar graph showing number of patients per doctor
        p = np.arange(len(name_of_doctors))
        width = 0.2
        plt.title('Number of Patients per Doctor',fontsize=18) 
        plt.bar(name_of_doctors,patients_per_doctor,color='#0066CC',edgecolor='black',width=0.4,linewidth=2)
        plt.xlabel('Name of Doctors',fontsize=14)
        plt.ylabel('Number of Patients',fontsize=14)
        plt.xticks(p+width/2,name_of_doctors,rotation=15)
        plt.tight_layout()
        plt.show()

        # this block of code here is to display group-bardiagram showing apointments for month feb and march per doctor 
        x = np.arange(len(name_of_doctors))
        bar_width = 0.35
        fig, ax = plt.subplots(figsize=(10, 6))
        for i, month in enumerate(months):
            offset = i * bar_width
            ax.bar(x + offset, [row[i] for row in appointments], bar_width, label=month,edgecolor='black',linewidth=2)
        ax.set_xlabel('Name of Doctors', fontsize=14)
        ax.set_ylabel('Number of Appointments', fontsize=14)
        ax.set_title('Appointments per Month per Doctor', fontsize=18)
        ax.set_xticks(x + bar_width / 2)  # Center labels under grouped bars
        ax.set_xticklabels(name_of_doctors, rotation=0, ha='center')
        ax.legend(title="Months")
        ax.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()  

        # this block of code here is to display bar diagram showing number of patients per symptoms
        max_value = max(number_of_patients_per_Symptoms)
        colors = ['red' if value == max_value else "#0066CC" for value in number_of_patients_per_Symptoms]
        plt.title('Number of Patients per Illness',fontsize=18)
        plt.bar(name_of_symptoms,number_of_patients_per_Symptoms,color=colors,edgecolor='black',width=0.5,linewidth=2)
        plt.xlabel('Name of Illness',fontsize=14)
        plt.ylabel('Number of Patients Per Symptoms',fontsize=14)
        plt.legend()
        plt.show()
        

