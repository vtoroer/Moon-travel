import math.pi

class ActivePart:
  def __init__(self, raw_mass, fuel_mass, thrust, specific_impulse, diameter, form_resistance)
    self.raw_mass = raw_mass
    self.fuel_mass = fuel_mass
    self.thrust = thrust
    self.fuel_burned_per_second = thrust / specific_impulse
    self.active_area = math.pi * diameter**2 / 4
    self.form_resistance = form_resistance
    
first_rocket_stage = ActivePart(135, 2010, 34350, 2580, 10.1, 0.1)
second_rocket_stage = ActivePart(37.6, 421.1, 5115, 4130, 10.1, 0.1)
third_rocket_stage = ActivePart(12, 108, 1016, 4130, 6.6, 0.1)
lunar_ship = ActivePart(10.3, 17.7, 95.75, 3050, 3.9, 0)
lunar_landing_stage = ActivePart(2.165, 8.165, 45.04, 3050, 0, 0)
lunar_take_off_stage = ActivePart(2.315, 2.355, 15.6, 3050, 0, 0)
