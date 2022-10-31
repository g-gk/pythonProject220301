class Transport:
    pass


# Водные транспорты
class WaterTransports(Transport):
    pass


class WarShips(WaterTransports):
    pass


class SeaVessels(WaterTransports):
    pass


class SailingVessels(WaterTransports):
    pass


class AircraftCarrier(WarShips):
    pass


class Battleship(WarShips):
    pass


class Submarine(WarShips):
    pass


class Destroyer(WarShips):
    pass


class Frigate(WarShips):
    pass


class Cruiser(WarShips):
    pass


class Liner(SeaVessels):
    pass


class Ferryboat(SeaVessels):
    pass


class Icebreaker(SeaVessels):
    pass


class Tanker(SeaVessels):
    pass


class BulkCarriers(SeaVessels):
    pass


class Galley(SailingVessels):
    pass


class Brigantine(SailingVessels):
    pass


class Caravels(SailingVessels):
    pass


class Clipper(SailingVessels):
    pass


class Galleon(SailingVessels):
    pass


class Schooner(SailingVessels):
    pass


# Воздушный транспорт
class AirTransport(Transport):
    pass


class Aviation(AirTransport):
    pass


class Aeronautics(AirTransport):
    pass


class Airplane(Aviation):
    pass


class Helicopter(Aviation):
    pass


class Aeroplane(Aviation):
    pass


class Fighter(Aviation):
    pass


class Bomber(Aviation):
    pass


class AirBalloon(Aeronautics):
    pass


class Airship(Aeronautics):
    pass


class Parachute(Aeronautics):
    pass


# Наземный транспорт
class GroundTransport(Transport):
    pass


class Railway(GroundTransport):
    pass


class BicycleTransport(GroundTransport):
    pass


class Road(GroundTransport):
    pass


class Cart(GroundTransport):
    pass


class Train(Railway):
    pass


class Locomotive(Railway):
    pass


class ReservedSeat(Train):
    pass


class Coupe(Train):
    pass


class Bicycle(BicycleTransport):
    pass


class Moped(BicycleTransport):
    pass


class Skateboard(BicycleTransport):
    pass


class Scooter(BicycleTransport):
    pass


class MotorTransport(Road):
    pass


class PassengerCar(Road):
    pass


class Truck(Road):
    pass


class RouteTransport(Road):
    pass


class Bus(RouteTransport):
    pass


class Trolleybus(RouteTransport):
    pass


class Tram(RouteTransport):
    pass


# Космический транспорт
class SpaceTransport(Transport):
    pass


class Rocket(SpaceTransport):
    pass


class Sputnik(SpaceTransport):
    pass


class SpaceStation(SpaceTransport):
    pass
