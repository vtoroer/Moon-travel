import vector as vt
import vechiles
import numpy as np
import math

# к моменту начала с этим блоком мы уже должны находиться в СО, связанной с луной
def aiming(lunar_ship, disconnected_part, moon_position_x, moon_position_y, slope_speed_moon, moon_radius, moon_acceleration):
# корабль, позиция необходимой точки на Луне, угловая скорость луны, радиус луны, g луны, временной шаг
    speed_needed_norm = 3 / 2
    speed_needed_tang = 1 / 2
    radius_vector = Vector(lunar_ship.vechile_position_x, lunar_ship.vechile_position_y)
    aim_speed = slope_speed_moon * moon_radius
    while radius_vector.get_module() > moon_radius:
        angle_rv_speed = math.pi - math.acos(np.dot(radius_vector, lunar_ship.vechile_velocity()) \
                                   / (radius_vector.get_module() * lunar_ship.vechile_velocity.get_module()))
        # угол между радиусом-вектором и скростью
        angle_rv_orientation = math.pi - lunar_ship.vechile_orientation + radius_vector.get_phi()
        # угол между радиусом вектором и ориентацией
        speed_norm = lunar_ship.vechile_velosity.get_module() * math.cos(angle_rv_speed)
        speed_tang = lunar_ship.vechile_velosity.get_module() * math.sin(angle_rv_speed) - aim_speed
        # измеряем тангенциальную скорость относительно поверхности луны
        # считаем примерное время, через которое мы окажется на Луне, следующая часть может быть изменена
        acceleration_norm = (moon_acceleration - (speed_tang ** 2) / radius_vector.get_module()) / 2
        time_lun_land = abs(speed_norm - speed_needed_norm) / acceleration_norm
        acceleration_tang = speed_tang * time_lun_land
        perfect_angle = math.atan()
        # TODO применить к ракете силу, обновить координаты
        for i in range(10):
            lunar_ship.rotation()
            lunar_ship.apply_forces()
            disconnected_part.apply_forces(False, disconnected_part.current_mass)
        radius_vector.update_by_xy(lunar_ship.vechile_position_x, lunar_ship.vechile_position_y)
        
    if (speed_tang <= 1) and (speed_norm <= 3):
        print ("We're alive, man!")
    else:
        print ("Oh, sorry, my friend. Hope next time'd be better.")
    radius_vector = none   
# TODO после перехода в СО связанной с Землёй, рассчитать положение точки на Луне
# TODO добавить проверку максимальной перегрузки

def wait_six_hours (ship_up, ship_moon, current_time, slope_speed_moon, moon_radius):
    time_gone = 60*60*6
    orbita_radius = pow(ship_up.vechile_position_x**2 + ship_up.vechile_position_y**2, 0.5)
    # находим необходимые константы
    
    angle_up = ship_up.vechile_velocity.get_module()*time_gone/orbita_radius
    ship_up.vechile_orientation += angle
    angle_1_1 = angle_up + ship_up.vechile_velocity.get_phi()
    ship_up.vechile_velocity.update_by_phi_and_module(angle_1_1, ship_up.vechile_velocity.get_module())
    radius_vector_1 = Vector(ship_up.vechile_position_x, ship_up.vechile_position_y)
    angle_up += radius_vector.get_phi()
    radius_vector_1.update_by_phi_and_module(angle_1, orbita_radius)
    ship_up.vechile_orientation_x = radius_vector.get_x
    ship_up.vechile_orientation_y = radius_vector.get_y
    radius_vector_1 = none
    # обновляем информацию о летающей части
    
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
    return current_time += time_gone, 
    
def left_the_moon (ship)
# TODO подобрать идеальный момент, взлететь (оказывается, задача очень похожа не первую функцию)
def pre_docking (ship)
# возможно, эта функция не понадобится
