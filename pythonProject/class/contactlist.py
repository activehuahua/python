import pickle


class Contact:
    def __init__(self, name, tel, sex):
        self.name = name
        self.tel = tel
        self.sex = sex

    def showDetail(self):
        return [self.name, self.tel, self.sex]


contacts = []
c = Contact('alex', '18086846185', 'male')
c1 = Contact('jianghua', '13980057365', 'male')
contacts.append(c)
contacts.append(c1)

contactfile = 'contact.data'

f = open(contactfile, 'wb')
pickle.dump(contacts, f)
f.close()

f = open(contactfile, 'rb')
contacts = pickle.load(f)

for i in contacts:
    print(i.showDetail())
