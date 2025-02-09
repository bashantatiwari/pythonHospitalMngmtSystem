from Person import Person
class Patient(Person):
    """Patient class"""

    def __init__(self, first_name, surname, age, mobile, address, symptoms,doctor = "Doctor Not Assigned",):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            age (int): Age
            mobile (string): the mobile number
            address (string): address
        """

        #ToDo1
        super().__init__(first_name,surname,age,mobile,address) # use of Inheritance 
        self.__symptom = symptoms.strip().split(",") # use of split method
        self.__doctor = doctor

    def get_doctor(self) :
        #ToDo3
        return self.__doctor
    

    def link(self, doctor):
        """Args: doctor(string): the doctor full name"""
        self.__doctor = doctor

    def add_symptom(self,symptom):
        self.__symptom.append(symptom)
        

    def get_symptoms(self):
        return self.__symptom

    def print_symptoms(self):
        """prints all the symptoms"""
        # return self.__symptom
        value = []
        for val in self.__symptom:
            value.append(val.strip())
        return ", ".join(value)
    
    def get_doctor_list(self):
        return self.__doctor


    
    
    @classmethod
    def set_symptoms(cls,new_symptom):
        cls.__symptom = new_symptom

########################### Handling Patient Data ############################      

  
    def write_patient_data_in_file(self):
         with open("./Database/patient_data.txt",'a') as file:
            file.write(f"{self.get_firstname()}|{self.get_surname()}|{self.get_age()}|{self.get_mobile()}|{self.get_address()}|{self.print_symptoms()}|{self.get_doctor()}\n")
            

    @classmethod
    def write_in_dischargedfile(cls,discharge_patient_list):
        try:
            with open("./Database/dischargedpatient_data.txt",'a') as file:
                for discharged_patient in discharge_patient_list:
                    file.write(f"{discharged_patient.get_firstname()}|{discharged_patient.get_surname()}|{discharged_patient.get_age()}|{discharged_patient.get_mobile()}|{discharged_patient.get_address()}|{discharged_patient.print_symptoms()}|{discharged_patient.get_doctor()}\n")

        except FileNotFoundError:
            print("Discharged Patient File not Found") 

    @classmethod
    def after_discharge_data(cls,patients):
        try:
            with open('./Database/patient_data.txt','w') as file:
                for patient in patients:
                    file.write(f"{patient.get_firstname()}|{patient.get_surname()}|{patient.get_age()}|{patient.get_mobile()}|{patient.get_address()}|{patient.print_symptoms()}|{patient.get_doctor()}\n")
                                    
        except FileNotFoundError:
            print("Patient Data Not Found")


    def __str__(self):
        return f'{self.full_name():^30}|{self.__doctor:^30}|{self.get_age():^5}|{self.get_mobile():^15}|{self.get_address():^15}|{self.print_symptoms():^15}|'


