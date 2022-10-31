class Transport:
    pass


# Разделим транспорт на 4 вида: водный, воздушный,
# наземный и космический.


class WaterTransport(Transport):
    pass


# Разделим водный транспорт на 2 подвида: морской и речной.


class SeaTransport(WaterTransport):
    pass


class RiverTransport(WaterTransport):
    pass


class AirTransport(Transport):
    pass


# Разделим воздушный транспорт на 2 вида: авиация и воздухоплавание.


class Aviation(AirTransport):
    pass


# Разделим авиацию на 4 подвида: дальняя, военно-транспортная,
# оперативно-тактическая и армейская.


class FarAviation(Aviation):
    pass


class MilitaryTransportAviation(Aviation):
    pass


class OperationalTacticalAviation(Aviation):
    pass


class ArmyAviation(Aviation):
    pass


class Aeronautics(AirTransport):
    pass


# Разделим воздухоплавание на дирижабли и воздушные шары.


class Dirigible(Aeronautics):
    pass


class Balloons(Aeronautics):
    pass


class GroundTransport(Transport):
    pass


# Разделим наземный транспорт на 4 вида: железнодорожный, автомобильный, 
# велосипедный и движимый животными.


class RailwayTransport(GroundTransport):
    pass


class AutomobileTransport(GroundTransport):
    pass


class BicycleTransport(GroundTransport):
    pass


class DrivenByAnimalsTransport(GroundTransport):
    pass


class SpaceTransport(Transport):
    pass


# Разделим космический транспорт на 3 вида: малоскоростной,
# субсветовой и сверхсветовой.


class LowSpeedTransport(SpaceTransport):
    pass


class SublightTransport(SpaceTransport):
    pass


class SuperluminalTransport(SpaceTransport):
    pass
