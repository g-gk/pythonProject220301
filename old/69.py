# Сайт поиска вакансий
class Profile:
    def __init__(self, name_prof):
        self.name_prof = name_prof

    def info(self):
        return ''

    def describe(self):
        print(self.name_prof + self.info())


class Vacancy(Profile):
    def __init__(self, name_prof, zp):
        super().__init__(name_prof)
        self.zp = zp

    def info(self):
        return f'Предлагаемая зарплата: {self.zp}'


class Resume(Profile):
    def __init__(self, name_prof, stazh):
        super().__init__(name_prof)
        self.stazh = stazh

    def info(self):
        return f'Стаж работы: {self.stazh}'
