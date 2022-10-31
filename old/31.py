class Person:
    def __init__(self, name, pat, last_name, phones):
        self.name = name
        self.pat = pat
        self.last_name = last_name
        self.phones = phones

    def get_phone(self):
        if 'private' in self.phones:
            return self.phones['private']
        else:
            return None

    def get_name(self):
        return f'{self.last_name} {self.name} {self.pat}'

    def get_work_phone(self):
        if 'work' in self.phones:
            return self.phones['work']
        else:
            return None

    def get_sms_text(self):
        return f'Уважаемый {self.name} {self.pat}! Примите участие ' \
               f'в нашем беспроигрышном конкурсе для физических лиц'


class Company:
    def __init__(self, name, typ, phones, *persons):
        self.name = name
        self.type = typ
        self.phones = phones
        self.persons = list(persons)

    def get_phone(self):
        if 'contact' in self.phones:
            return self.phones['contact']
        else:
            for i in self.persons:
                phone = i.get_work_phone()
                if phone:
                    return phone
            return None

    def get_name(self):
        return self.name

    def get_sms_text(self):
        return f'Для компании {self.name} есть супер предложение! ' \
               f'Примите участие в нашем беспроигрышном конкурсе для {self.type}'


def send_sms(*persons):
    for i in list(persons):
        phone = i.get_phone()
        if phone:
            print(f'Отправлено СМС на номер {phone} с текстом:', i.get_sms_text())
        else:
            print(f'Не удалось отправить сообщение абоненту:', i.get_name())


person1 = Person("Ivan", "Ivanovich", "Ivanov", {"private": 123, "work": 456})
person2 = Person("Ivan", "Petrovich", "Petrov", {"private": 789})
person3 = Person("Ivan", "Petrovich", "Sidorov", {"work": 789})
person4 = Person("John", "Unknown", "Doe", {})
company1 = Company("Bell", "ООО", {"contact": 111}, person3, person4)
company2 = Company("Cell", "АО", {"non_contact": 222}, person2, person3)
company3 = Company("Dell", "Ltd", {"non_contact": 333}, person2, person4)
send_sms(person1, person2, person3, person4, company1, company2, company3)
