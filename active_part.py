import math
from vector import *


class ActivePart:
    def __init__(self, raw_mass, fuel_mass, thrust, specific_impulse, diameter, form_resistance):
        self.raw_mass = raw_mass
        self.fuel_mass = fuel_mass
        self.thrust = thrust
        self.fuel_burned_per_second = thrust / specific_impulse
        self.active_area = math.pi * diameter**2 / 4
        self.form_resistance = form_resistance

# [raw_mass] = kg
# [fuel_mass] = kg
# [thrust] = N
# [specific_impulse] = m/s
# [diameter] = m
# [form_resistance] = -


first_rocket_stage = ActivePart(135000, 2010000, 34350000, 2580, 10.1, 0.1)
second_rocket_stage = ActivePart(37600, 421100, 5115000, 4130, 10.1, 0.1)
third_rocket_stage = ActivePart(12000, 108000, 1016000, 4130, 6.6, 0.1)
lunar_ship = ActivePart(10300, 17700, 95750, 3050000, 3.9, 0)
lunar_landing_stage = ActivePart(2165, 8165, 45040, 3050, 0, 0)
lunar_take_off_stage = ActivePart(2315, 2355, 15600, 3050, 0, 0)

# ЕСЛИ ЗНАЧЕНИЕ ПАРАМЕТРА РАВНО 0, ЗНАЧИТ, ОН НЕ УКАЗАН В НАЧАЛЬНЫХ УСЛОВИЯХ

sum_mass = 334380  # Суммарная масса модулей

# [gravitational_constant] = N*m^2/kg^2
# [moon_mass] = kg
# [earth_mass] = kg
# [moon_radius] = m
# [earth_radius] = m
# [moon_earth_radius] = m
# [moon_angular_velocity] = rad/s

gravitational_constant = 6.674 * 10**(-11)
moon_mass = 7.3477 * 10**22
earth_mass = 5.9722 * 10**24
moon_radius = 1737100
earth_radius = 6378100
moon_earth_radius = 384405000
moon_angular_velocity = 2,66 * 10**(-6)
moon_pos = Vector(moon_earth_radius, 0)
earth_pos = Vector(0, 0)

time_per_step = 100


def update_moon_pos():
    moon_pos.update_by_phi_and_module(moon_pos.phi + time_per_step * moon_angular_velocity, moon_earth_radius)
    return 0
