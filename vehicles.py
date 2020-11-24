from vector import *
from force import *
from active_part import *


class Vehicle:
    def __init__(self, current_mass, vehicle_position_x, vehicle_position_y, vehicle_velocity_x, vehicle_velocity_y,
                 vehicle_fuel_left, vehicle_orientation, thrust, fuel_burned_per_second, active_area):
        """Constructor"""
        self.current_mass = current_mass
        self.vehicle_position_x = vehicle_position_x
        self.vehicle_position_y = vehicle_position_y
        self.vehicle_velocity = Vector(vehicle_velocity_x, vehicle_velocity_y)
        self.vehicle_fuel_left = vehicle_fuel_left
        self.vehicle_orientation = vehicle_orientation  # MODULE MUST BE EQUAL TO 1 (VECTOR)
        self.thrust = thrust
        self.fuel_burned_per_second = fuel_burned_per_second
        self.current_acceleration = Vector(0, 0)  # Задаём вектор ускорения.
        self.active_area = active_area

    def apply_forces(self, thrust_enabled, vehicle_mass):
        self.vehicle_position_x += self.vehicle_velocity.x * time_per_step
        self.vehicle_position_y += self.vehicle_velocity.y * time_per_step

        sum_speed_gain_x = 0
        sum_speed_gain_y = 0

        earth_vehicle_position = Vector(earth_pos.x - self.vehicle_position_x, earth_pos.y - self.vehicle_position_y)
        moon_vehicle_position = Vector(moon_pos.x - self.vehicle_position_x, moon_pos.y - self.vehicle_position_y)

        if earth_vehicle_position.get_module() < earth_radius + 100000:  # ПРИМЕНЕНИЕ АЭРОДИНАМИЧЕСКОГО СОПРОТИВЛЕНИЯ
            resistance_vector = apply_resistance(vehicle_mass,
                                                 get_atmospheric_density(earth_vehicle_position.get_module() - earth_radius),
                                                 0.1, self.active_area, self.vehicle_velocity)
            sum_speed_gain_x += resistance_vector.x * time_per_step
            sum_speed_gain_y += resistance_vector.y * time_per_step

        if earth_vehicle_position.get_module() < moon_earth_radius // 10:  # ПРИМЕНЕНИЕ ГРАВИТАЦИИ ЗЕМЛИ
            gravity_vector_x = apply_gravity(earth_mass, earth_vehicle_position).x * time_per_step
            gravity_vector_y = apply_gravity(earth_mass, earth_vehicle_position).y * time_per_step
            sum_speed_gain_x += gravity_vector_x
            sum_speed_gain_y += gravity_vector_y

        if moon_vehicle_position.get_module() < moon_earth_radius // 100:  # ПРИМЕНЕНИЕ ГРАВИТАЦИИ ЛУНЫ
            gravity_vector_x = apply_gravity(moon_mass, moon_vehicle_position).x * time_per_step
            gravity_vector_y = apply_gravity(moon_mass, moon_vehicle_position).y * time_per_step
            sum_speed_gain_x += gravity_vector_x
            sum_speed_gain_y += gravity_vector_y

        if thrust_enabled:
            thrust_vector_x = apply_thrust(self.thrust, self.vehicle_orientation, self.current_mass).x * time_per_step
            thrust_vector_y = apply_thrust(self.thrust, self.vehicle_orientation, self.current_mass).y * time_per_step
            sum_speed_gain_x += thrust_vector_x
            sum_speed_gain_y += thrust_vector_y

        self.current_acceleration.update_by_xy(sum_speed_gain_x / time_per_step, sum_speed_gain_y / time_per_step)

        self.vehicle_velocity.update_by_xy(self.vehicle_velocity.x + sum_speed_gain_x, self.vehicle_velocity.y
                                           + sum_speed_gain_y)
        self.vehicle_fuel_left -= self.fuel_burned_per_second * time_per_step

        return 0

    # Эта функция выполняет поворот экзмепляра. Если поворот до заданного угла невозможен (слишком большие перегрузки),
    # она выполняет поворот на максимально большой угол (стремясь достичь целевого) и возвращает код 1. Если же поворот
    # возможен, она выполняет поворот и возвращает код 0.
    def rotation(self, max_angular_velocity, goal_angle):
        max_possible_rotation = max_angular_velocity * time_per_step
        if goal_angle - self.vehicle_orientation.phi >= max_possible_rotation:
            self.vehicle_orientation.update_by_phi_and_module(self.vehicle_orientation.phi + max_possible_rotation,
                                                              self.vehicle_orientation.module)
            return 1
        elif goal_angle - self.vehicle_orientation.phi <= max_possible_rotation:
            self.vehicle_orientation.update_by_phi_and_module(self.vehicle_orientation.phi - max_possible_rotation,
                                                              self.vehicle_orientation.module)
            return 1
        else:
            self.vehicle_orientation.update_by_phi_and_module(goal_angle, self.vehicle_orientation.module)
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
