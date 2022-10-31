# Транспорт
class Transport:
    pass


# Воздушный транспорт
class AirTransport(Transport):
    pass


# Авиация
class Aviation(AirTransport):
    pass


# Военные самолеты
class MilitaryAircraft(Aviation):
    pass


# Бомбардировщики
class Bombers(MilitaryAircraft):
    pass


# Перехватчики
class Interceptors(MilitaryAircraft):
    pass


# Штурмовики
class AttackAircraft(MilitaryAircraft):
    pass


# Самолеты гражданской авиации
class CivilAircraft(Aviation):
    pass


# Широкофюзеляжные самолеты
class WideBody(CivilAircraft):
    pass


# Узкофюзеляжные самолеты
class NarrowBody(CivilAircraft):
    pass


# Региональные и местные самолеты
class RegionalLocal(CivilAircraft):
    pass


# Воздухоплавание
class Aeronautics(AirTransport):
    pass


# Дирижабль
class Blimp(Aeronautics):
    pass


# Тепловой дирижабль
class ThermalBlimp(Blimp):
    pass


# Вакуумный дирижабль
class VacuumBlimp(Blimp):
    pass


# Воздушные шары
class Balloons(Aeronautics):
    pass


# Водный транспорт
class WaterTransport(Transport):
    pass


# Грузовой водный транспорт
class GoodsWaterTransport(WaterTransport):
    pass


# Пассажирский водный транспорт
class PassengerWaterTransport(WaterTransport):
    pass


# Технический водный транспорт
class TechnicalWaterTransport(WaterTransport):
    pass


# Наземный транспорт
class LandTransport(Transport):
    pass


# Велосипедный наземный транспорт
class Bicycle(LandTransport):
    pass


# Движивый животными наземный транспорт
class AnimalDriven(LandTransport):
    pass


# Автомобильный наземный транспорт
class Automotive(LandTransport):
    pass


# Общественный автомобильный транспорт
class PublicRoadTransport(Automotive):
    pass


# Грузовой автомобильный транспорт
class GoodsRoadTransport(Automotive):
    pass


# Легковой автомобильный транспорт
class LightMotorVehicles(Automotive):
    pass


# Железнодорожный наземный транспорт
class Railway(LandTransport):
    pass


# Трамвай
class Tram(Railway):
    pass


# Метро
class Underground(Railway):
    pass


# Поезд
class Train(Railway):
    pass


# Космический транспорт
class SpaceTransport(Transport):
    pass
