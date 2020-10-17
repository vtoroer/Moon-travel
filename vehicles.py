from vector import *
from force import *


class Vehicle:
    def __init__(self, current_mass, vehicle_position_x, vehicle_position_y, vehicle_velocity_x, vehicle_velocity_y,
                 vehicle_fuel_left, vehicle_orientation, thrust, fuel_burned_per_second):
        """Constructor"""
        self.current_mass = current_mass
        self.vehicle_position_x = vehicle_position_x
        self.vehicle_position_y = vehicle_position_y
        self.vehicle_velocity = Vector(0, 465)  # Стартовая скорость такая, потому что ракета вращается с Землей
        self.vehicle_fuel_left = vehicle_fuel_left
        self.vehicle_orientation = vehicle_orientation  # MODULE MUST BE EQUAL TO 1 (VECTOR)
        self.thrust = thrust
        self.fuel_burned_per_second = fuel_burned_per_second

    # Эта функция выполняет увеличение скорости при применении силы (thrust). 
    def thrust(self, seconds_per_step):
        self.vehicle_velocity.x += apply_thrust(self.thrust, self.vehicle_orientation, self.current_mass).x \
                                   * seconds_per_step
        self.vehicle_velocity.y += apply_thrust(self.thrust, self.vehicle_orientation, self.current_mass).y \
                                   * seconds_per_step
        return 0

    # Эта функция выполняет поворот экзмепляра. Если поворот до заданного угла невозможен (слишком большие перегрузки), 
    # она выполняет поворот на максимально большой угол (стремясь достичь целевого) и возвращает код 1. Если же поворот
    # возможен, она выполняет поворот и возвращает код 0.
    def rotation(self, max_angular_velocity, goal_angle, seconds_per_step):
        max_possible_rotation = max_angular_velocity * seconds_per_step
        if goal_angle - self.vehicle_orientation.phi >= max_possible_rotation:
            self.vehicle_orientation.phi += max_possible_rotation
            return 1
        elif goal_angle - self.vehicle_orientation.phi <= max_possible_rotation:
            self.vehicle_orientation.phi -= max_possible_rotation
            return 1
        else:
            self.vehicle_orientation.phi = goal_angle
            return 0

    def disconnection(self, separated_part, active_part):
        self.current_mass -= separated_part.current_mass + self.vehicle_fuel_left
        self.vehicle_fuel_left = active_part.total_fuel
        self.thrust = active_part.thrust
        # внешние силы остаются те же, внутренние, видимо, отдельно считаются
        self.fuel_burned_per_second = active_part.fuel_burned_per_second

    def connection(self, separated_part):
        self.current_mass += separated_part.current_mass
        self.vehicle_fuel_left += separated_part.total_fuel
        # self.thrust = active_part.thrust + separated_part.thrust
        self.fuel_burned_per_second += separated_part.fuel_burned_per_second
        # считаем, что относительная скорость мала

    # TODO: MAKE A FUNCTIONS FOR ROTATION AND THRUST

    # FUEL BURNED PER SECOND (dm/dt = F/V, TO CALCULATE BASED ON THIS FORMULA)

    def disconnect(self, main_part, sp_current_mass, sp_vehicle_fuel_left, sp_fuel_burned_per_second):
        # вся ракета, сухая масса ЛМ, топливо ЛМ, кол-во топлива, сжигаемого ЛМ
        # остальное не меняется
        # то, что начинается с sp относится к separated part
        lunar_module = Vehicle(sp_current_mass, main_part.vehicle_position_x,
                               main_part.vehicle_position_y, main_part.vehicle_velocity_x, main_part.vehicle_velocity_y,
                               sp_vehicle_fuel_left, main_part.vehicle_orientation, main_part.thrust,
                               sp_fuel_burned_per_second)
        main_part.disconnection(lunar_module)
        return 0

    def connect(self, first, second):
        first.connecton(second)
        second = None
        return 0

