import math.pi

class ActivePart:
  def __init__(self, raw_mass, fuel_mass, thrust, specific_impulse, diameter, form_resistance)
    self.raw_mass = raw_mass
    self.fuel_mass = fuel_mass
    self.sum_mass = raw_mass+fuel_mass
    self.thrust = thrust
    self.fuel_burned_per_second = thrust / specific_impulse
    self.active_area = math.pi * diameter**2 / 4
    self.form_resistance = form_resistance

#[raw_mass] = kg
#[fuel_mass] = kg
#[sum_mass] = kg
#[thrust] = N
#[fuel_burned_per_second] = kg/s
#[specific_impulse] = m/s
#[diameter] = m
#[active_area] = m^2
#[form_resistance] = -

first_rocket_stage = ActivePart(135000, 2010000, 34350000, 2580, 10.1, 0.1)
second_rocket_stage = ActivePart(37600, 421100, 5115000, 4130, 10.1, 0.1)
third_rocket_stage = ActivePart(12000, 108000, 1016000, 4130, 6.6, 0.1)
lunar_ship = ActivePart(10300, 17700, 95.75, 3050000, 3.9, 0)
lunar_landing_stage = ActivePart(2165, 8165, 45040, 3050, 0, 0)
lunar_take_off_stage = ActivePart(2315, 2355, 15600, 3050, 0, 0)

#ЕСЛИ ЗНАЧЕНИЕ ПАРАМЕТРА РАВНО 0, ЗНАЧИТ ОН НЕ УКАЗАН В НАЧАЛЬНЫХ УСЛОВИЯХ

time_per_step = 0.01
