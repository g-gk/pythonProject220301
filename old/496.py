# Заготовка для игры

class Weapon:
    def __init__(self, name, damage, range):
        self.name = name
        self.damage = damage
        self.range = range

    def hit(self, actor, target):
        if target.is_alive():
            x1, y1 = actor.get_coords()
            x2, y2 = target.get_coords()
            s = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** .5
            if s > self.range:
                print(f'Враг слишком далеко для оружия {self.name}')
            else:
                print(f'Врагу нанесен урон оружием {self.name} в размере {self.damage}')
                target.get_damage(self.damage)
        else:
            print('Враг уже повержен')

    def __str__(self):
        return self.name


class BaseCharacter:
    def __init__(self, pos_x, pos_y, hp):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.hp = hp

    def move(self, delta_x, delta_y):
        self.pos_x += delta_x
        self.pos_y += delta_y

    def is_alive(self):
        return self.hp > 0

    def get_damage(self, amount):
        self.hp -= amount

    def get_coords(self):
        return self.pos_x, self.pos_y


class BaseEnemy(BaseCharacter):
    def __init__(self, pos_x, pos_y, weapon, hp):
        super().__init__(pos_x, pos_y, hp)
        self.weapon = weapon

    def hit(self, target):
        if target.__class__ is MainHero:
            self.weapon.hit(self, target)
        else:
            print('Могу ударить только Главного героя')

    def __str__(self):
        return f'Враг на позиции {self.get_coords()} с оружием {self.weapon}'


class MainHero(BaseCharacter):
    def __init__(self, pos_x, pos_y, name, hp):
        super().__init__(pos_x, pos_y, hp)
        self.name = name
        self.weapon = []
        self.cur_weapon = 0

    def hit(self, target):
        if self.weapon:
            if target.__class__ is BaseEnemy:
                self.weapon[self.cur_weapon].hit(self, target)
            else:
                print('Могу ударить только Врага')
        else:
            print('Я безоружен')

    def add_weapon(self, weapon):
        if weapon.__class__ is Weapon:
            print(f'Подобрал {weapon}')
            self.weapon.append(weapon)
        else:
            print('Это не оружие')

    def next_weapon(self):
        n = len(self.weapon)
        if n == 1:
            print('У меня только одно оружие')
        elif n > 1:
            self.cur_weapon += 1
            self.cur_weapon %= n
            print(f'Сменил оружие на {self.weapon[self.cur_weapon]}')
        else:
            print('Я безоружен')

    def heal(self, amount):
        self.hp += amount
        if self.hp > 200:
            self.hp = 200
        print(f'Полечился, теперь здоровья {self.hp}')


def main():
    print('----- Пример 1 -----')
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

    print('----- Пример 2 -----')
    weapon1 = Weapon("Кинжал", 5, 1)
    weapon2 = Weapon("Световой меч", 25, 3)
    weapon3 = Weapon("Рогатка", 1, 50)
    weapon4 = Weapon("Большая рогатка", 2, 100)
    princess = BaseCharacter(100, 100, 100)
    archer = BaseEnemy(50, 50, weapon3, 100)
    armored_swordsman = BaseEnemy(10, 10, weapon2, 500)
    archer.hit(armored_swordsman)
    armored_swordsman.move(30, 30)
    print(armored_swordsman.get_coords())
    main_hero = MainHero(0, 0, "Король Артур", 200)
    main_hero.move(20, 20)
    print(main_hero.get_coords())
    print(isinstance(armored_swordsman, BaseCharacter))
    print(isinstance(main_hero, BaseCharacter))
    print(isinstance(main_hero, BaseEnemy))
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
    archer.hit(main_hero)

    print('----- Пример 3 -----')

    print('----- Пример 4 -----')


if __name__ == '__main__':
    main()
