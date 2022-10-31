class Person:
    def __init__(self, names, otech, twonames, phone):
        self.names = names
        self.otech = otech
        self.twonames = twonames
        self.phone = phone

    def get_phone(self):
        return self.phone.get('private', None)

    def get_name(self):
        return f'{self.twonames} {self.names} {self.otech}'

    def get_work_phone(self):
        return self.phone.get('work', None)

    def get_sms_text(self):
        return f'Уважаемый {self.names} {self.otech}! Примите\
 участие в нашем беспроигрышном конкурсе для физических лиц'


class Company:
    def __init__(self, name_company, type_company, phone, *arab):
        self.name_company = name_company
        self.type_company = type_company
        self.phone = phone
        self.arab = arab

    def get_phone(self, key='contact'):
        res = None
        res = self.phone.get(key, None)
        if res:
            return res
        for person in self.arab:
            res = person.get_work_phone()
            if res:
                break
        return res

    def get_name(self):
        return self.name_company

    def get_sms_text(self):
        return f'Для компании {self.name_company} есть супер предложение! Примите участие в\
 нашем беспроигрышном конкурсе для {self.type_company}'


def send_sms(*joinn):
    for enjoy in joinn:
        num = enjoy.get_phone()
        if num:
            print(
                f'Отправлено СМС на номер {num} с текстом: {enjoy.get_sms_text()}')
        else:
            print(
                f'Не удалось отправить сообщение абоненту: {enjoy.get_name()}')


person1 = Person("Ivan", "Ivanovich", "Ivanov", {"private": 123, "work": 456})
person2 = Person("Ivan", "Petrovich", "Petrov", {"private": 789})
person3 = Person("Ivan", "Petrovich", "Sidorov", {"work": 789})
person4 = Person("John", "Unknown", "Doe", {})
company1 = Company("Bell", "ООО", {"contact": 111}, person3, person4)
company2 = Company("Cell", "АО", {"non_contact": 222}, person2, person3)
company3 = Company("Dell", "Ltd", {"non_contact": 333}, person2, person4)
send_sms(person1, person2, person3, person4, company1, company2, company3)
