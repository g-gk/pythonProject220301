# СМС-рассылка

class Person:
    def __init__(self, name1, name2, name3, phones: dict):
        self.name1 = name1
        self.name2 = name2
        self.name3 = name3
        self.phones = phones

    def get_phone(self):
        return self.phones.get('private', None)

    def get_name(self):
        return f'{self.name3} {self.name1} {self.name2}'

    def get_work_phone(self):
        return self.phones.get('work', None)

    def get_sms_text(self):
        return f'Уважаемый {self.name1} {self.name2}! \
Примите участие в нашем беспроигрышном конкурсе для физических лиц'


class Company:
    def __init__(self, name, type_c, phones: dict, *persons: Person):
        self.name = name
        self.type_c = type_c
        self.phones = phones
        self.persons = persons

    def get_phone(self):
        if 'contact' in self.phones:
            return self.phones['contact']
        for p in self.persons:
            work_phone = p.get_work_phone()
            if work_phone:
                return work_phone

    def get_name(self):
        return self.name

    def get_sms_text(self):
        return f'Для компании {self.name} есть супер предложение! \
Примите участие в нашем беспроигрышном конкурсе для {self.type_c}'


def send_sms(*args: (Person, Company)):
    for arg in args:
        res = arg.get_phone()
        if res:
            print(f'Отправлено СМС на номер {res} с текстом: {arg.get_sms_text()}')
        else:
            print(f'Не удалось отправить сообщение абоненту: {arg.get_name()}')


def main():
    print('----- Пример 1 -----')
    person1 = Person("Ivan", "Ivanovich", "Ivanov", {"private": 123, "work": 456})
    person2 = Person("Ivan", "Petrovich", "Petrov", {"private": 789})
    person3 = Person("Ivan", "Petrovich", "Sidorov", {"work": 789})
    person4 = Person("John", "Unknown", "Doe", {})
    company1 = Company("Bell", "ООО", {"contact": 111}, person3, person4)
    company2 = Company("Cell", "АО", {"non_contact": 222}, person2, person3)
    company3 = Company("Dell", "Ltd", {"non_contact": 333}, person2, person4)
    send_sms(person1, person2, person3, person4, company1, company2, company3)

    print('----- Пример 2 -----')
    person1 = Person("Степан", "Петрович", "Джобсов", {"private": 555})
    person2 = Person("Боря", "Иванович", "Гейтсов", {"private": 777, "work": 888})
    person3 = Person("Семен", "Робертович", "Возняцкий", {"work": 789})
    person4 = Person("Леонид", "Арсенович", "Торвальдсон", {})
    company1 = Company("Яблочный комбинат", "ООО", {"contact": 111}, person1, person3)
    company2 = Company("ПластОкно", "АО", {"non_contact": 222}, person2)
    company3 = Company("Пингвинья ферма", "Ltd", {"non_contact": 333}, person4)
    send_sms(person1, person2, person3, person4, company1, company2, company3)

    print('----- Пример 3 -----')

    print('----- Пример 4 -----')


if __name__ == '__main__':
    main()
