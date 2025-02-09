class Person():
    def __init__(self,first_name,surname,age,mobile,address):
        self.__first_name = first_name
        self.__surname = surname
        self.__age = age
        self.__mobile = mobile
        self.__address = address

    def full_name(self):
        return f"{self.__first_name} {self.__surname}"

    def get_firstname(self):
        return self.__first_name

    def get_surname(self):
        return self.__surname
    
    def get_address(self):
        return self.__address
    
    def get_age(self):
        return self.__age

    def get_mobile(self):
        return self.__mobile
    
    def set_firstname(self,new_firstname):
        self.__first_name = new_firstname

    def set_surname(self,new_surname):
        self.__surname = new_surname
    
    def set_address(self,new_address):
        self.__address = new_address

    def set_age(self,new_age):
        if(new_age>0):
            self.__age = new_age
        else:
            print("Invalid Age: Age Cannot be Zero or Negative")

    def set_mobile(self,new_mobile):
        if(len(new_mobile) == 10):
            self.__mobile = new_mobile
        else:
            print("PhoneNumber should be of 10 digit")

    @classmethod
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