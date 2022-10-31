class Weapon:
    def __init__(self, name, damage, ranges):
        self.name = name
        self.damage = damage
        self.range = ranges

    def hit(self, actor, target):
        if target.is_alive():
            ranges = pow((actor.pos_x - target.pos_x) ** 2 +
                         (actor.pos_y - target.pos_y) ** 2, 0.5)
            if ranges < self.range:
                target.get_damage(self.damage)
                print(f'Врагу нанесен урон оружием {self.name} в размере {self.damage}')
            else:
                print(f'Враг слишком далеко для оружия {self.name}')
        else:
            print('Враг уже повержен')

    def __str__(self):
        return self.name


class BaseCharacter:
    def __init__(self, x, y, hp):
        self.pos_x = x
        self.pos_y = y
        self.hp = hp

    def move(self, delta_x, delta_y):
        self.pos_y += delta_y
        self.pos_x += delta_x

    def is_alive(self):
        return True if self.hp > 0 else False

    def get_damage(self, amount):
        self.hp -= amount

    def get_coords(self):
        return (self.pos_x, self.pos_y)


class BaseEnemy(BaseCharacter):
    def __init__(self, x, y, weapon, hp):
        super(BaseEnemy, self).__init__(x, y, hp)
        self.weapon = weapon

    def hit(self, target):
        if target.__class__.__name__ == 'MainHero':
            self.weapon.hit(self, target)
        else:
            print('Могу ударить только Главного героя')

    def __str__(self):
        return f'Враг на позиции ({self.pos_x}, {self.pos_y}) с оружием {self.weapon}'


class MainHero(BaseCharacter):
    def __init__(self, x, y, name, hp):
        super(MainHero, self).__init__(x, y, hp)
        self.name = name
        self.weapons = list()
        self.weapon = None

    def hit(self, target):
        if not self.weapon:
            print('Я безоружен')
        elif target.__class__.__name__ != 'BaseEnemy':
            print('Могу ударить только Врага')
        else:
            self.weapon.hit(self, target)

    def add_weapon(self, weapon):

        if weapon.__class__.__name__ != 'Weapon':
            print('Это не оружие')
        elif self.weapon is None:
            print(f'Подобрал {weapon.name}')
            self.weapon = weapon
        else:
            print(f'Подобрал {weapon.name}')
            self.weapons.append(weapon)

    def next_weapon(self):
        if not self.weapons and not self.weapon:
            print('Я безоружен')
        elif self.weapon and not self.weapons:
            print('У меня только одно оружие')
        else:
            self.weapons.append(self.weapon)
            self.weapon = self.weapons[0]
            del self.weapons[0]
            print(f'Сменил оружие на {self.weapon.name}')

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
