import vector as vt
import vechiles
import numpy as np
import math

# к моменту начала с этим блоком мы уже должны находиться в СО, связанной с луной
# разворачиваем ракету "спиной" к скорости
def turn_against_speed(ship):
    cos_angle_speed_orien = ((ship.vehicle_velocity.get_x()*ship.vehicle_orientation.get_x()
                            + ship.vehicle_velocity.get_y()*ship.vehicle_orientation.get_y())
                            / (ship.vehicle_velocity.get_module() * ship.vehicle_orientation.get_module()))
    epsilon = 0.01
    print(ship.vehicle_position_x, ship.vehicle_position_y)
    if abs(cos_angle_speed_orien + 1) > epsilon:
       goal_ang = math.pi + ship.vehicle_velocity.get_phi()
       if goal_ang > math.pi*3/2:
          goal_ang -= math.pi*2
       ship.rotation(0.05555555, goal_ang)
    return ship

# функция говорит, надо ли ещё тормозить, приравниваем её THRUST_ENABLED
def get_lower_to_moon(ship):
    radius_vector = Vector(ship.vehicle_position_x, ship.vehicle_position_y)
    # вводим радиус-вектор, с началом в центре Луны и концом на ракете
    moon_surf_dist = radius_vector.get_module() - moon_radius
    ship = turn_against_speed(ship)
    # тормозим до тех пор, пока не достигнем высоты орбиты не больше 45 км
    radius_vector = None
    if moon_surf_dist >= 45000: 
        return True
    else: return False

# в случае успеха выводится 0
def find_orbit(ship, moon_acceleration, phi_moon_aim):
    radius_vector = Vector(ship.vehicle_position_x, ship.vehicle_position_y)
    aim_vector = Vector(moon_radius*math.cos(phi_moon_aim), moon_radius*math.sin(phi_moon_aim))
    # вводим радиус-вектор, с началом в центре Луны и концом на ракете
    moon_surf_dist = radius_vector.get_module() - moon_radius
    # с помощью формул из интернета считаем сколько времени будем падать при нулевой норм скорости
    # и сколько времени нужно, чтобы сбросить тангенцальную скорость до 0
    delta_v = math.sqrt(2*moon_acceleration*moon_surf_dist)
    delta_t = ship.current_mass*3050/ship.thrust*(1-math.exp(-delta_v/3050))
    angle_speed_tang = math.pi/2 - radius_vector.get_phi
    tang_speed = abs(ship.vehicle_velocity.get_module()*math.cos(angle_speed_tang))
    delta_tau = tang_speed * ship.current_mass / ship.thrust
    aim_vector.update_by_phi_and_module(aim_vector.get_phi() + moon_angular_velocity*
                                        (delta_t + delta_tau), moon_radius)
    # посчитаем расстояние до цели с запасом в отрицательную сторону 
    angle_aim_fall = aim_vector.get_phi() - radius_vector.get_phi()
    if abs(angle_aim_fall) >= (2*math.pi):
        if angle_aim_fall < -math.pi*2:
            angle_aim_fall += math.pi*2
        elif angle_aim_fall > math.pi*2:
            angle_aim_fall -= math.pi*2
    distance_aim_fall = moon_radius*angle_aim_fall
    radius_vector = None
    if (distance_aim_fall <= 100) and (distance_aim_fall >= 0):
        return 0
    else: return 1

def waiting (ship_up, ship_moon, current_time, slope_speed_moon, moon_radius):
    # находим необходимые константы
    
    angle_moon = slope_speed_moon*time_left
    ship_moon.vechile_orientation += angle_moon
    angle_2_2 = angle_moon + ship_moon.vechile_velocity.get_phi()
    ship_moon.vechile_velocity.update_by_phi_and_module(angle_2_2, ship_moon.vechile_velocity.get_module())
    radius_vector_2 = Vector(ship_moon.vechile_position_x, ship_moon.vechile_position_y)
    angle_moon += radius_vector.get_phi()
    radius_vector_2.update_by_phi_and_module(angle_moon, moon_radius)
    ship_moon.vechile_orientation_x = radius_vector.get_x
    ship_moon.vechile_orientation_y = radius_vector.get_y
    radius_vector_2 = none
    # обновляем информацию о части, сидящей на Луне
    return current_time += time_gone 
    
