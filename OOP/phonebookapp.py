class contact:
    phone_dict=[]
    
    def __init__(self,name,phonenum):
        self.name=name
        self.phone=phonenum

        contact.phone_dict.append(self)

    def show_contact(self):
        return f"name: {self.name},contact num: {self.phone}"
        
    @classmethod
    def show_all_contact(cls):
        if len(cls.phone_dict)==0:
            print("no contact fond in dict")
        else:
            print("all contct from directry1")
            for contact in cls.phone_dict:
                print(contact.show_contact())

    @classmethod
    def search_contact(cls,search_name):
        for contact in cls.phone_dict:
            if contact.name.lower() == search_name.lower():
                return f"{contact.name} number {contact.phone}"
        return f"no contact found {search_name}"
    
    @staticmethod
    def validate_phone_number(number):
        if len(number) >= 10 and number.isdigit():
            return True
        else:
            return False

n_contacts=int(input("how many contact yo want add> : "))
for i in range(n_contacts):
    name=input("enter your name : ")
    phone_num=input("enter the phone number ")
    if contact.validate_phone_number(phone_num):
        c1=contact(name,phone_num)
    else:
        print(f"invalid phone number {name},phone number atlest 10 digit ")

contact.show_all_contact()



# c1=contact("pondi",7990026342)
# c1=contact("dhruv",704622129)
# print(contact.search_contact("Gaurav"))
# print(contact.search_contact("daksh"))

# print(contact.phone_dict)
# print(c1.show_contact())

# c1.show_all_contact()