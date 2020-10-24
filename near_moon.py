import vector as vt
import vechiles
import numpy as np
import math

# к моменту начала с этим блоком мы уже должны находиться в СО, связанной с луной
def aiming(ship, moon_position, slope_speed_moon, moon_radius, moon_acceleration):
# корабль, позиция необходимой точки на Луне, угловая скорость луны, радиус луны
    speed_needed_norm = 3 / 2
    speed_needed_tang = 1 / 2
    radius_vector = Vector(ship.vechile_position_x, ship.vechile_position_y)
    aim_speed = slope_speed_moon * moon_radius
    while radius_vector.get_module() > moon_radius:
        angle_rv_speed = math.pi - math.acos(np.dot(radius_vector, ship.vechile_velocity()) \
                                   / (radius_vector.get_module() * ship.vechile_velocity.get_module()))
        # угол между радиусом-вектором и скростью
        speed_norm = ship.vechile_velosity.get_module() * math.cos(angle_rv_speed)
        speed_tang = ship.vechile_velosity.get_module() * math.sin(angle_rv_speed) - aim_speed
        # измеряем тангенциальную скорость относительно поверхности луны
        # считаем примерное время, через которое мы окажется на Луне, следующая часть может быть изменена
        acceleration = (moon_acceleration - (speed_tang ** 2) / radius_vector.get_module()) / 2
        time_lun_land = abs(speed_norm - speed_needed_norm) / acceleration
    if (speed_tang <= 1) and (speed_norm <= 3):
        print ("We're alive, man!")
    else:
        print ("Oh, sorry, my friend. Hope next time'd be better.")
# TODO учесть вращение Луны вокруг своей оси (или понять, почему этого не нужно делать)
# TODO после перехода в СО связанной с Землёй, рассчитать положение точки на Луне
# TODO добавить проверку максимальной перегрузки
