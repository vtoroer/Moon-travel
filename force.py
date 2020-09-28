from vector import *
from math import *


class Force:
    def __init__(self, x, y):
        """Constructor"""
        self.x = x
        self.y = y


# apply_gravity returns acceleration for a vehicle due to a gravitational force
def apply_gravity(gravitational_coefficient, moon_vehicle):
    vector = moon_vehicle.multiply(gravitational_coefficient / pow(moon_vehicle.module(), 3))
    return vector


# NOTE that vehicle orientation vector's module must be equal to zero
# apply_thrust returns acceleration for a vehicle due to a thrust
def apply_thrust(thrust, vehicle_orientation):
    vector = vehicle_orientation.multiply(thrust)
    return vector


# constant is a composition of all constants
# apply_resistance returns acceleration for a vehicle due to an air resistance
def apply_resistance(vehicle_mass, atmospheric_density, resistance_coefficient, vehicle_resistance_area, vehicle_speed):
    constant = 2 * resistance_coefficient * atmospheric_density * vehicle_resistance_area / vehicle_mass
    vector = vehicle_speed.multiply(constant * vehicle_speed.module(), )
    return vector
