from vector import *
from math import *
from active_part import *


# apply_gravity returns acceleration for a vehicle due to a gravitational force
def apply_gravity(body_mass, body_vehicle):
    body_vehicle_copy = Vector(body_vehicle.x, body_vehicle.y) # Чтобы не менять вектор снаружи
    vector = body_vehicle_copy.multiply(gravitational_constant * body_mass / pow(body_vehicle.module, 3))
    return vector


# NOTE that vehicle orientation vector's module must be equal to zero
# apply_thrust returns acceleration for a vehicle due to a thrust
def apply_thrust(thrust, vehicle_orientation, vehicle_mass):
    vehicle_orientation_copy = Vector(vehicle_orientation.x, vehicle_orientation.y)
    vector = vehicle_orientation_copy.multiply(thrust / vehicle_mass)
    return vector


# constant is a composition of all constants
# apply_resistance returns acceleration for a vehicle due to an air resistance
def apply_resistance(vehicle_mass, atmospheric_density, resistance_coefficient, vehicle_resistance_area, vehicle_velocity):
    constant = resistance_coefficient * atmospheric_density * vehicle_resistance_area / vehicle_mass / 2
    vehicle_velocity_copy = Vector(vehicle_velocity.x, vehicle_velocity.y)
    vector = vehicle_velocity_copy.multiply(constant * vehicle_velocity.module)
    vector.update_by_xy(-vector.x, -vector.y)
    return vector
