class Contact:
    all_contacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contact.append(self)

class Supplier(Contact):
    def order(self, order):
        print(f"I want to send {order} to {self.name}")
    
class Friend(Contact):
    def __init__(self, name, email, phone):
        super().__init__(name, email)
        self.phone = phone
        