# Imports
from Admin import Admin
from Doctor import Doctor
from Patient import Patient

def main():
    """
    the main function to be ran when the program runs
    """

    # Initialising the actors
    admin = Admin() # username is 'admin', password is '123'

    # patients = admin.extract_data("patient_data")
    # doctors = [Doctor('John','Smith','Internal Med.'), Doctor('Jone','Smith','Pediatrics'), Doctor('Jone','Carlos','Cardiology')]
    # patients = [Patient('Sara','Smith', 20, '07012345678','B1 234',['Nausea']), Patient('Mike','Jones', 37,'07555551234','L2 2AB',['Vomiting']), Patient('Daivd','Smith', 15, '07123456789','C1 ABC',["Dizziness"])]
    # admin = Admin.extract_admin_data(Admin)
    patients = admin.extract_data("patient_data")
    # discharged_patients = Admin.extract_data(Admin,"dischargedpatient_data")

    # keep trying to login tell the login details are correct
    while True:
        if admin.login():
            running = True # allow the program to run
            break
        else:
            print('Incorrect username or password.')

    while running:
        # print the menu
        print('Choose the operation:')
        print(' 1- Register/view/update/delete doctor')
        print(' 2- Register/view/update patient')
        print(' 3- Assign doctor to a patient')
        print(' 4- Book an appointment')
        print(' 5- Relocating doctor to a patient')
        print(' 6- Patients Grouped by Family')
        print(' 7- Patients Grouped by Illness')
        print(' 8- Discharge patients')
        print(' 9- View discharged patient')
        print(' 10- Management Report')
        print(' 11- View Graphical Diagram of Management Report')
        print(' 12- Update admin details')
        print(' 13- Quit')

        # get the option
        op = input('Option: ')

        if op == '1':
            # 1- Register/view/update/delete doctor
         #ToDo1
          admin.doctor_management()

        elif op == '2':
            admin.patient_management()

        elif op == '3':
            # 4- Assign doctor to a patient
            admin.assign_doctor_to_patient()

        elif op == '4':
            admin.book_an_appointment()

        elif op == '5':
            admin.relocating_doctor()

        elif op == '6':
            admin.grouping_patients_based_on_familynames()

        elif op == '7':
            admin.display_grouped_patient_by_symptom()

        elif op == '8':
            # 7- View or discharge patients
            #ToDo2
            admin.view_patient(patients)

            while True:
                op = input('Do you want to discharge a patient(Y/N):').lower()
                
                if op == 'yes' or op == 'y':
                    #ToDo3
                    admin.discharge()
                    break

                elif op == 'no' or op == 'n':
                    break

                # unexpected entry
                else:
                    print('Please answer by yes or no.')
        
        elif op == '9':
            #  8- view discharged patients
            admin.view_discharge()

        elif op == '10':
            # 9-Management Reportadmin
            admin.management_report()

        elif op == '11':
            # 9-Management Reportadmin
            admin.display_graphical_diagram_of_maagement_report()

        elif op == '12':
            # 12- Update admin detais
            admin.update_details()

        elif op == '13':
            # 13 - Quit
            print("System is Closing for now")
            break
        
        else:
            # the user did not enter an option that exists in the menu
            print('Invalid option. Try again')

if __name__ == '__main__':
    main()
