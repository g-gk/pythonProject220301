class Weapon:
    # инициализатор
    def __init__(self, name, damage, range):
        self.name = name
        self.damage = damage
        self.range = range

    # проверяет, жив ли персонаж
    def hit(self, actor, target):
        # если мертв
        if not target.is_alive():
            print('Враг уже повержен')
        # проверка расстояния от actor до target
        elif self.range ** 2 >= (target.pos_x - actor.pos_x) ** 2 + (
                target.pos_y - actor.pos_y) ** 2:
            print(f'Врагу нанесен урон оружием {self.name} в размере {self.damage}')
            target.hp -= self.damage
        else:
            print(f'Враг слишком далеко для оружия {self.name}')

    # приведение к строке
    def __str__(self):
        return self.name


class BaseCharacter:
    # инициализатор
    def __init__(self, pos_x, pos_y, hp):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.hp = hp

    # перемещает персонажа на delta_x и delta_y в игровом мире
    def move(self, delta_x, delta_y):
        self.pos_x += delta_x
        self.pos_y += delta_y

    # проверка, жив ли персонаж
    def is_alive(self):
        if self.hp <= 0:
            return False
        return True

    # убавляет количество жизней персонажа на amount
    def get_damage(self, amount):
        if self.is_alive():
            self.hp -= amount

    # возвращает кортеж с текущими координатами персонажа
    def get_coords(self):
        return self.pos_x, self.pos_y


class BaseEnemy(BaseCharacter):
    # инициализатор
    def __init__(self, pos_x, pos_y, weapon, hp):
        super().__init__(pos_x, pos_y, hp)
        self.weapon = weapon

    # для удара персонажа target
    def hit(self, target):
        # если ударяемый персонаж не является главным героем
        if not target.__class__.__name__ == 'MainHero':
            print('Могу ударить только Главного героя')
        else:
            self.weapon.hit(self, target)

    # приведение к строке
    def __str__(self):
        return f'Враг на позиции ({self.pos_x}, {self.pos_y}) с оружием {self.weapon.name}'


class MainHero(BaseCharacter):
    # инициализатор
    def __init__(self, pos_x, pos_y, name, hp):
        super().__init__(pos_x, pos_y, hp)
        self.name = name
        self.weapons = []
        self.number_weapon = 0

    # для удара персонажа target
    def hit(self, target):
        # если оружия нет
        if not self.weapons:
            print('Я безоружен')
        else:
            # проверка, является ли ударяемый объектом класса BaseEnemy
            if target.__class__.__name__ == 'BaseEnemy':
                self.weapons[self.number_weapon].hit(self, target)
            else:
                print('Могу ударить только Врага')

    # добавляет оружие в инвентарь персонажа
    def add_weapon(self, weapon):
        if weapon.__class__.__name__ == 'Weapon':
            self.weapons.append(weapon)
            print(f'Подобрал {weapon}')
        else:
            print('Это не оружие')

    # для смены оружия
    def next_weapon(self):
        if len(self.weapons) > 0:
            # если есть только одно оружие
            if len(self.weapons) == 1:
                print('У меня только одно оружие')
            # смена оружия на следующее
            else:
                self.number_weapon += 1
                # в порядке подбора, по кругу
                if self.number_weapon == len(self.weapons):
                    self.number_weapon = 0
                print(f'Сменил оружие на {self.weapons[self.number_weapon]}')
        # Если оружия нет
        else:
            print('Я безоружен')

    # для повышения количества жизней персонажа на amount
    def heal(self, amount):
        self.hp += amount
        if self.hp > 200:
            self.hp = 200
        print(f'Полечился, теперь здоровья {self.hp}')


weapon1 = Weapon("Короткий меч", 5, 1)
weapon2 = Weapon("Длинный меч", 7, 2)
weapon3 = Weapon("Лук", 3, 10)
weapon4 = Weapon("Лазерная орбитальная пушка", 1000, 1000)
princess = BaseCharacter(100, 100, 100)
archer = BaseEnemy(50, 50, weapon3, 100)
armored_swordsman = BaseEnemy(10, 10, weapon2, 500)
archer.hit(armored_swordsman)
armored_swordsman.move(10, 10)
print(armored_swordsman.get_coords())
main_hero = MainHero(0, 0, "Король Артур", 200)
main_hero.hit(armored_swordsman)
main_hero.next_weapon()
main_hero.add_weapon(weapon1)
main_hero.hit(armored_swordsman)
main_hero.add_weapon(weapon4)
main_hero.hit(armored_swordsman)
main_hero.next_weapon()
main_hero.hit(princess)
main_hero.hit(armored_swordsman)
main_hero.hit(armored_swordsman)
