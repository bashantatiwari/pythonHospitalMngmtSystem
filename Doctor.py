from Person import Person

class Doctor(Person):
    """A class that deals with the Doctor operations"""
    """ Being a Doctor age mobile and address need to be added for connectivity"""

    __doctor_count = 0

    def __init__(self, first_name, surname,speciality, age="", mobile="", address="" ):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            speciality (string): Doctor`s speciality
        """
        super().__init__(first_name,surname,age,mobile,address)
        self.__speciality = speciality
        self.__patients = []
        self.__appointments = []
        self.__doctors = []

    def get_speciality(self) :
        return self.__speciality

    def set_speciality(self, new_speciality):
        self.__speciality = new_speciality

    
    def add_patient(self, patient):
        self.__patients.append(patient)

    def number_patient(self):
        return len(self.__patients)
    
    def remove_patient(self,patient):
        if self.__patients:
            self.__patients.remove(patient)
        else:
            print("Patients are not stored")

    def print_patinets(self):
        for patient in self.__patients:
            print(patient)

    
    @classmethod
    def get_number_of_doctor(cls):
        return cls.__doctor_count
    
    def write_doctor_data_in_file(self):
        try:
            with open("./Database/doctor_data.txt",'a') as file:
                file.write(f'{self.get_firstname()}|{self.get_surname()}|{self.get_speciality()}\n')

        except FileNotFoundError:
            print("Database Not Found")


    @classmethod
    def delete_doctor_data(cls,doctors):
        try:
            with open('./Database/doctor_data.txt','w') as file:
                for doctor in doctors:
                    file.write(f"{doctor.get_firstname()}|{doctor.get_surname()}|{doctor.get_speciality()}\n")
                    
        except FileNotFoundError:
            print("Doctor Data Not Found")
    

    def __str__(self) :
        return f'{self.full_name():^30}|{self.__speciality:^15}'


doc1 = Doctor("Bashanta","Tiwari","Counsellor")
print(doc1.number_patient())