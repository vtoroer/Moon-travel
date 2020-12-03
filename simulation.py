from plotting import *
from vehicles import *
from vector import *
from active_part import *
import arcade

THRUST_ENABLED = False
SCREEN_WIDTH = 1480
SCREEN_HEIGHT = 800
FACTOR = 5 * 10**(-6)


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):

        self.f_rocket_velocity = open('data_files/rocket_velocity.txt', 'w')
        self.f_rocket_distance_to_the_earth = open('data_files/rocket_distance_to_the_earth.txt', 'w')
        self.f_rocket_distance_to_the_moon = open('data_files/rocket_distance_to_the_moon.txt', 'w')
        self.f_rocket_acceleration = open('data_files/rocket_acceleration.txt', 'w')
        self.f_rocket_velocity.close()
        self.f_rocket_distance_to_the_earth.close()
        self.f_rocket_distance_to_the_moon.close()
        self.f_rocket_acceleration.close()  # ОЧИСТКА ФАЙЛОВ

        super().__init__(width, height)
        global rocket_one
        rocket_one = Vehicle(sum_mass, 6371000 + 100000, 0, 0, 1.2*7910, first_rocket_stage.fuel_mass, Vector(1, 0),
                             first_rocket_stage.thrust, first_rocket_stage.fuel_burned_per_second,
                             first_rocket_stage.active_area)
        self.total_sim_steps = 0
        self.moon_lander_steps = 0
        self.command_module_steps = 0
        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):

        pass

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        earth_radius_drawn = earth_radius * FACTOR
        moon_radius_drawn = moon_radius * FACTOR
        rad = 2  # Радиус точки, указывающей местоположение ракеты
        arcade.draw_circle_filled(SCREEN_WIDTH / 2 + rocket_one.vehicle_position_x * FACTOR,
                                  SCREEN_HEIGHT / 2 + rocket_one.vehicle_position_y * FACTOR, rad, arcade.color.YELLOW)
        arcade.draw_circle_filled(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                                  earth_radius_drawn, arcade.color.GREEN)  # ОТРИСОВКА ЗЕМЛИ
        arcade.draw_circle_filled(SCREEN_WIDTH / 2 + moon_pos.x * FACTOR, SCREEN_HEIGHT / 2 + moon_pos.y * FACTOR,
                                  moon_radius_drawn, arcade.color.WHITE)  # ОТРИСОВКА ЛУНЫ
        arcade.draw_text(f"x_position: {round(rocket_one.vehicle_position_x / 1000, 3)} km",
                         SCREEN_WIDTH - 150, SCREEN_HEIGHT - 15, arcade.color.WHITE, 10)
        arcade.draw_text(f"y_position: {round(rocket_one.vehicle_position_y / 1000, 3)} km",
                         SCREEN_WIDTH - 150, SCREEN_HEIGHT - 30, arcade.color.WHITE, 10)
        arcade.draw_text(f"x_velocity: {round(rocket_one.vehicle_velocity.x / 1000, 3)} km/s",
                         SCREEN_WIDTH - 150, SCREEN_HEIGHT - 45, arcade.color.WHITE, 10)
        arcade.draw_text(f"y_velocity: {round(rocket_one.vehicle_velocity.y / 1000, 3)} km/s",
                         SCREEN_WIDTH - 150, SCREEN_HEIGHT - 60, arcade.color.WHITE, 10)
        arcade.draw_text(f"velocity: {round(rocket_one.vehicle_velocity.get_module() / 1000, 3)} km/s",
                         SCREEN_WIDTH - 150, SCREEN_HEIGHT - 75, arcade.color.WHITE, 10)
        arcade.draw_text(f"acceleration_x: {round(rocket_one.current_acceleration.x, 3)} m/s",
                         SCREEN_WIDTH - 150, SCREEN_HEIGHT - 90, arcade.color.WHITE, 10)
        arcade.draw_text(f"acceleration_y: {round(rocket_one.current_acceleration.y, 3)} m/s",
                         SCREEN_WIDTH - 150, SCREEN_HEIGHT - 105, arcade.color.WHITE, 10)
        arcade.draw_text(f"acceleration: {round(rocket_one.current_acceleration.get_module(), 3)} m/s",
                         SCREEN_WIDTH - 150, SCREEN_HEIGHT - 120, arcade.color.WHITE, 10)
        arcade.draw_text(f"TIME: {self.total_sim_steps * time_per_step // 3600} : {self.total_sim_steps * time_per_step % 3600 // 60} : {self.total_sim_steps * time_per_step  % 60}",
                         SCREEN_WIDTH - 150, SCREEN_HEIGHT - 135, arcade.color.WHITE, 10)  # ЗДЕСЬ РИСУЕТСЯ ВИЗУАЛИЗАЦИЯ

    def on_update(self, delta_time):
        # print(str(rocket_one.vehicle_velocity.get_module()))
        rocket_one.apply_forces(THRUST_ENABLED, rocket_one.current_mass)
        update_moon_pos()
        self.total_sim_steps += 1

        self.f_rocket_velocity = open('data_files/rocket_velocity.txt', 'a')
        self.f_rocket_velocity.write(str(rocket_one.vehicle_velocity.get_module()) + '\n')
        self.f_rocket_velocity.close()

        self.f_rocket_distance_to_the_earth = open('data_files/rocket_distance_to_the_earth.txt', 'a')
        self.f_rocket_distance_to_the_earth.write(str(Vector(rocket_one.vehicle_position_x - earth_pos.x,
                                                             rocket_one.vehicle_position_y - earth_pos.y).get_module()
                                                      - earth_radius) + '\n')
        self.f_rocket_distance_to_the_earth.close()

        self.f_rocket_distance_to_the_moon = open('data_files/rocket_distance_to_the_moon.txt', 'a')
        self.f_rocket_distance_to_the_moon.write(str(Vector(rocket_one.vehicle_position_x - moon_pos.x,
                                                            rocket_one.vehicle_position_y - moon_pos.y).get_module()
                                                      - moon_radius) + '\n')
        self.f_rocket_distance_to_the_moon.close()

        self.f_rocket_acceleration = open('data_files/rocket_acceleration.txt', 'a')
        self.f_rocket_acceleration.write(str(rocket_one.current_acceleration.get_module()) + '\n')
        self.f_rocket_acceleration.close()

        # LANDING

        lngth = (rocket_one.vehicle_position_x ** 2 + rocket_one.vehicle_position_y ** 2) ** 0.5
        if earth_radius + 3000 < lngth < earth_radius + 10000 and rocket_one.vehicle_velocity.get_module() < 300:
            print("Landing was a success!")

            self.f_rocket_velocity = open('data_files/rocket_velocity.txt', 'r')
            plot(self.total_sim_steps, self.f_rocket_velocity, "velocity over time", "velocity")
            self.f_rocket_velocity.close()

            self.f_rocket_distance_to_the_earth = open('data_files/rocket_distance_to_the_earth.txt', 'r')
            plot(self.total_sim_steps, self.f_rocket_distance_to_the_earth, "distance to earth's surface over time",
                 "distance")
            self.f_rocket_distance_to_the_earth.close()

            self.f_rocket_distance_to_the_moon = open('data_files/rocket_distance_to_the_moon.txt', 'r')
            plot(self.total_sim_steps, self.f_rocket_distance_to_the_moon, "distance to moon's surface over time",
                 "distance")
            self.f_rocket_distance_to_the_moon.close()

            self.f_rocket_acceleration = open('data_files/rocket_acceleration.txt', 'r')
            plot(self.total_sim_steps, self.f_rocket_acceleration, "acceleration over time",
                 "acceleration")
            self.f_rocket_acceleration.close()
            exit()
        elif (rocket_one.vehicle_position_x**2 + rocket_one.vehicle_position_y**2) ** 0.5 <= earth_radius:
            print("Crash!")

            self.f_rocket_velocity = open('data_files/rocket_velocity.txt', 'r')
            plot(self.total_sim_steps, self.f_rocket_velocity, "velocity over time", "velocity")
            self.f_rocket_velocity.close()

            self.f_rocket_distance_to_the_earth = open('data_files/rocket_distance_to_the_earth.txt', 'r')
            plot(self.total_sim_steps, self.f_rocket_distance_to_the_earth, "distance to earth's surface over time",
                 "distance")
            self.f_rocket_distance_to_the_earth.close()

            self.f_rocket_distance_to_the_moon = open('data_files/rocket_distance_to_the_moon.txt', 'r')
            plot(self.total_sim_steps, self.f_rocket_distance_to_the_moon, "distance to moon's surface over time",
                 "distance")
            self.f_rocket_distance_to_the_moon.close()

            self.f_rocket_acceleration = open('data_files/rocket_acceleration.txt', 'r')
            plot(self.total_sim_steps, self.f_rocket_acceleration, "acceleration over time",
                 "acceleration")
            self.f_rocket_acceleration.close()
            exit()
        elif rocket_one.current_acceleration.get_module() > 98.1:
            print("Crew is dead")

            self.f_rocket_velocity = open('data_files/rocket_velocity.txt', 'r')
            plot(self.total_sim_steps, self.f_rocket_velocity, "velocity over time", "velocity")
            self.f_rocket_velocity.close()

            self.f_rocket_distance_to_the_earth = open('data_files/rocket_distance_to_the_earth.txt', 'r')
            plot(self.total_sim_steps, self.f_rocket_distance_to_the_earth, "distance to earth's surface over time",
                 "distance")
            self.f_rocket_distance_to_the_earth.close()

            self.f_rocket_distance_to_the_moon = open('data_files/rocket_distance_to_the_moon.txt', 'r')
            plot(self.total_sim_steps, self.f_rocket_distance_to_the_moon, "distance to moon's surface over time",
                 "distance")
            self.f_rocket_distance_to_the_moon.close()

            self.f_rocket_acceleration = open('data_files/rocket_acceleration.txt', 'r')
            plot(self.total_sim_steps, self.f_rocket_acceleration, "acceleration over time",
                 "acceleration")
            self.f_rocket_acceleration.close()
            exit()
        """ All the logic to move, and the game logic goes here. """

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        global FACTOR
        if key == arcade.key.UP:
            FACTOR += 10**(-6)
        elif key == arcade.key.DOWN:
            FACTOR -= 5 * 10**(-7)


def run_simulation():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()

