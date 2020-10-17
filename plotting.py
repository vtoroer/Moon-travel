# В этом файле указаны функции для работы с данными
import numpy as np
import matplotlib.pyplot as plt


# ЭТА ФУНКЦИЯ СОЗДАЁТ ОДИН ГРАФИК
def plot(steps, file_name, plot_name, variable):

    file = open(file_name, 'r')

    data = np.zeros(shape=steps)

    for i in range(0, steps):
        data[i] = float(file.readline())

    f = plt.figure()
    ax = f.add_subplot()

    ax.plot(data)
    ax.grid()

    #  Добавляем подписи к осям и название графика:
    ax.set_xlabel('time (s)')
    ax.set_ylabel(variable)
    plt.title(plot_name)

    # plt.show()

    f.savefig("speed_over_time.pdf", bbox_inches='tight')
    return 0


# ЭТА ФУНКЦИЯ СОЗДАЁТ ВСЕ НЕОБХОДИМЫЕ ГРАФИКИ
def final_plotting(total_sim_steps, moon_lander_steps, command_module_steps):

    plot(total_sim_steps, 'data_files/rocket_velocity.txt', 'speed_over_time', 'speed (m/s)')
    plot(total_sim_steps, 'data_files/rocket_distance_to_the_moon.txt', 'distance_to_the_moon_over_time', 'distance (m)')
    plot(total_sim_steps, 'data_files/rocket_distance_to_the_earth.txt', 'distance_to_the_earth_over_time',
         'distance (m)')
    plot(total_sim_steps, 'data_files/rocket_acceleration.txt', 'acceleration_over_time', 'acceleration (m^2/s)')

    plot(moon_lander_steps, 'data_files/moon_lander_velocity.txt', 'speed_over_time', 'speed (m/s)')
    plot(moon_lander_steps, 'data_files/moon_lander_distance_to_the_moon.txt', 'distance_to_the_moon_over_time',
         'distance (m)')
    plot(moon_lander_steps, 'data_files/moon_lander_acceleration.txt', 'acceleration_over_time', 'acceleration (m^2/s)')

    plot(command_module_steps, 'data_files/command_module_velocity.txt', 'speed_over_time', 'speed (m/s)')
    plot(command_module_steps, 'data_files/command_module_distance_to_the_earth.txt', 'distance_to_the_earth_over_time',
         'distance (m)')
    plot(command_module_steps, 'data_files/command_module_overload.txt', 'overload_over_time', 'overload (m^2/s)')

    return 0



