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
# [thrust] = kN
# [specific_impulse] = m/s
# [diameter] = m
# [form_resistance] = -


first_rocket_stage = ActivePart(135000, 2010000, 34350000, 2580, 10.1, 0.1)
second_rocket_stage = ActivePart(37600, 421100, 5115000, 4130, 10.1, 0.1)
third_rocket_stage = ActivePart(12000, 108000, 1016000, 4130, 6.6, 0.1)
lunar_ship = ActivePart(10300, 17700, 95.75, 3050000, 3.9, 0)
lunar_landing_stage = ActivePart(2165, 8165, 45040, 3050, 0, 0)
lunar_take_off_stage = ActivePart(2315, 2355, 15600, 3050, 0, 0)

sum_mass = 334380  # Суммарная масса модулей

gravitational_constant = 6.674 * 10**(-11)
moon_mass = 7.3477 * 10**22
earth_mass = 5.9722 * 10**24
moon_radius = 1737100
earth_radius = 6378100
earth_pos = Vector(0, 0)
moon_pos = Vector(384400000, 0)
moon_earth_radius = 384400000
moon_angular_velocity = 16 * 10**(-5)

# ЕСЛИ ЗНАЧЕНИЕ ПАРАМЕТРА РАВНО 0, ЗНАЧИТ, ОН НЕ УКАЗАН В НАЧАЛЬНЫХ УСЛОВИЯХ

time_per_step = 10


def update_moon_pos():
    moon_pos.update_by_phi_and_module(moon_pos.phi + time_per_step * moon_angular_velocity, moon_earth_radius)
    return 0


def get_atmospheric_density(height):

    if height <= 500:
        return 1.2250
    elif height <= 1000:
        return 1.1673
    elif height <= 1500:
        return 1.1117
    elif height <= 2000:
        return 1.0581
    elif height <= 2500:
        return 1.0065
    elif height <= 3000:
        return 0.9569
    elif height <= 4000:
        return 0.9093
    elif height <= 5000:
        return 0.8194
    elif height <= 6000:
        return 0.7365
    elif height <= 7000:
        return 0.6601
    elif height <= 8000:
        return 0.59
    elif height <= 9000:
        return 0.5258
    elif height <= 10000:
        return 0.4671
    elif height <= 11000:
        return 0.4135
    elif height <= 12000:
        return 0.3648
    elif height <= 14000:
        return 0.3119
    elif height <= 16000:
        return 0.2279
    elif height <= 18000:
        return 0.1665
    elif height <= 20000:
        return 0.1216
    elif height <= 24000:
        return 0.0889
    elif height <= 28000:
        return 0.0469
    elif height <= 32000:
        return 0.0251
    elif height <= 36000:
        return 0.0136
    elif height <= 40000:
        return 7.26 * 10**(-3)
    elif height <= 50000:
        return 4.00 * 10**(-3)
    elif height <= 60000:
        return 1.03 * 10**(-3)
    elif height <= 80000:
        return 3.00 * 10**(-4)
    elif height <= 100000:
        return 1.85 * 10**(-5)
    else:
        return 0
