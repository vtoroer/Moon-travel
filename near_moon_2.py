import vector as vt
import vechiles
import active_part
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

# в случае успеха выводится 0
def find_orbit(ship, moon_acceleration, phi_moon_aim, moon_angular_velocity):
    radius_vector = Vector(ship.vehicle_position_x, ship.vehicle_position_y)
    aim_vector = Vector(moon_radius*math.cos(phi_moon_aim), moon_radius*math.sin(phi_moon_aim))
    # вводим радиус-вектор, с началом в центре Луны и концом на ракете
    moon_surf_dist = radius_vector.get_module() - moon_radius
    # с помощью формул из интернета считаем сколько времени будем падать при нулевой норм скорости
    # и сколько времени нужно, чтобы сбросить тангенцальную скорость до 0
    delta_v = math.sqrt(2*moon_acceleration*moon_surf_dist)
    delta_t = ship.current_mass*3050/ship.thrust*(1-math.exp(-delta_v/3050))
    angle_speed_tang = math.pi/2 - radius_vector.get_phi
    tang_speed = (abs(ship.vehicle_velocity.get_module()*math.cos(angle_speed_tang)) - 
                  moon_angular_velocity*radius_vector.get_module())
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

def moon_landing(ship, moon_radius, moon_angular_velocity):
    radius_vector = Vetor(ship.vehicle_position_x, ship.vehicle_position_y)
    height = radius_vector.get_module() - moon_radius
    moon_acceleration = gravitational_constant * moon_mass / moon_radius**2
    # полностью гасим нормальную скорость, помним, что угловая скорость должна остаться
    tang_speed = (abs(ship.vehicle_velocity.get_module()*math.cos(angle_speed_tang)) - 
                  moon_angular_velocity*radius_vector.get_module())
    goal_angle = radius_vector.get_phi() + math.pi/2
    if (goal_angle) >= (2*math.pi):
        if goal_angle < -math.pi*2:
            goal_angle += math.pi*2
        elif goal_angle > math.pi*2:
            goal_angle -= math.pi*2
    if (tang_speed >= 0.5) and (height >= 10000):
        ship.rotation(0.05555555, goal_angle)
        return True
    # вычисляем delta-v, смотрим, когда надо начинать тормозить
    speed_reduce = lunar_ship.specific_impulse * math.log(ship.current_mass /
                   lunar_ship.raw_mass)
    moment_inerce = lunar_module.raw_mass() * moon_radius**2
    energy_sh_rotation = moment_inerce*moon_angular_velocity**2 / 2
    speed_is_going_be = math.sqrt(2*height*moon_acceleration + 
                                  ship.vehicle_velocity.get_module() ** 2 
                                  - energy_sh_rotation/lunar_module.raw_mass())
    angle_bw_velocity_rv = ((radius_vector.get_x()*ship.vehicle_velocity.get_x +
                             radius_vector.get_y()*ship.vehicle_velocity.get_y)/
                             (radius_vector.get_module()*ship.vehicle_velocity.get_module()))
    radius_vector = None
    if (speed_is_going_be >= speed_reduce) and (height >= 50) and (angle_bw_velocity_rv < 0):
        # момент, когда надо начинать тормозить, найден
        ship = turn_against_speed(ship)
        return True, False
    # если высота меньше 50 метров, используем аккуратную настройку
    elif (height >= 50):
        return False, False
    elif (height < 50) and (speed_is_going_be >= speed_reduce) and (angle_bw_velocity_rv < 0):
        if (height>0): 
            ship = turn_against_speed(ship)
            return True, False
        else:
            return False, True
    elif (height < 50) and (angle_bw_velocity_rv >= 0):
        if (height>0):
            return False, False
        else:
            return False, True
    elif (height < 50) and (speed_is_going_be < speed_reduce) and (angle_bw_velocity_rv < 0):
        if (height>0):
            return False, False
        else: 
            return False, True

# обновляет положение коробля, считает время и понимает, пора ли уже взлетать
# вывод - корабль в небе, кор. на луне, прошло времени, пора ли взлетать
def waiting(ship_moon, ship_orbit, time_step, moon_angular_velocity, time_waited):
    # rv - радиус-вектор
    rv_moon = Vector(ship_moon.vehicle_position_x, ship_moon.vehicle_position_y)
    rv_moon.update_by_phi_and_module(time_step*moon_angular_velocity, 
                                     rv_moon.get_module())
    ship_moon.vehicle_position_x = rv_moon.get_x()
    ship_moon.vehicle_position_y = rv_moon.get_y()
    ship_orbit.apply_forces(False, ship_orbit.current_mass)
    time_waited += time_step
    if (time_waited == 3600) and nearest_orbit: 
        is_ready = True
    else:
        is_ready = False
    return ship_moon, ship_orbit, time_waited, is_ready

def actions_near_moon(THRUST_ENABLED, ARE_DISCONNECTED, TIME_TO_FALL, IS_LANDED_MOON, 
                      READY_TAKEOFF_MOON, TIME_ON_MOON, READY_CONNECTING, rocket_one)
    if ARE_DISCONNECTED == False: 
            rocket_two = disconnect_lsh(rocket_one)
            # rocket__two - это лунный модуль, далее управляем им
            ARE_DISCONNECTED = True
        if TIME_TO_FALL == 1: 
            THRUST_ENABLED = get_lower_to_moon(rocket_two)
                if THRUST_ENABLED == False:
                    TIME_TO_FALL = find_orbit(rocket_two, gravitational_constant*moon_mass / 
                                   math.sqrt((rocket_two.vehicle_position_x) ** 2 + (rocket_two.vehicle_position_y) ** 2), 
                                   moon_aim_position.get_phi())
        elif TIME_TO_FALL == 0:
                THRUST_ENABLED, IS_LANDED_MOON = moon_landing(rocket_two, moon_radius, moon_angular_velocity)
                if IS_LANDED_MOON:
                    rocket_two, rocket_one, TIME_ON_MOON, READY_TAKEOFF_MOON = waiting(rocket_two, 
                                                    rocket_one, time_per_step, moon_angular_velocity, TIME_ON_MOON)

        rocket_one.apply_forces(False, rocket_one.current_mass)
        rocket_two.apply_forces(THRUST_ENABLED, rocket_two.current_mass)
        update_moon_pos()
        if READY_CONNECTING == True:
            rocket_two = connect(rocket_two, rocket_two)
            ARE_DISCONNECTED = False
    return NUMBER_OF_PHASE += 1
