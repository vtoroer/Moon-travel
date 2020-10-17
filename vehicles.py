class Vehicle:
    def __init__(self, current_mass, vehicle_position_x, vehicle_position_y, vehicle_velocity_x, vehicle_velocity_y,
                 vehicle_fuel_left, vehicle_orientation, thrust, fuel_burned_per_second):
        """Constructor"""
        self.current_mass = current_mass
        self.vehicle_position_x = vehicle_position_x
        self.vehicle_position_y = vehicle_position_y
        self.vehicle_velocity_x = vehicle_velocity_x
        self.vehicle_velocity_y = vehicle_velocity_y
        self.vehicle_fuel_left = vehicle_fuel_left
        self.vehicle_orientation = vehicle_orientation  # MODULE MUST BE EQUAL TO 1 (VECTOR)
        self.thrust = thrust
        self.fuel_burned_per_second = fuel_burned_per_second


    def disconnection(self, separated_part, active_part):
        self.current_mass -= separated_part.current_mass + self.vehicle_fuel_left
        self.vehicle_fuel_left = active_part.total_fuel
        self.thrust = active_part.thrust
# внешние силы остаются те же, внутренние, видимо, отдельно считаются
        self.fuel_burned_per_second = active_part.fuel_burned_per_second

    def connecton(self, separated_part):
        self.current_mass += separated_part.current_mass
        self.vehicle_fuel_left += separated_part.total_fuel
#        self.thrust = active_part.thrust + separated_part.thrust
        self.fuel_burned_per_second += separated_part.fuel_burned_per_second   
# считаем, что относительная скорость мала

    # TODO: MAKE A FUNCTIONS FOR ROTATION AND THRUST

    #FUEL BURNED PER SECOND (dm/dt = F/V, TO CALCULATE BASED ON THIS FORMULA)

def disconnect(main_part, sp_current_mass, sp_vehicle_fuel_left, sp_fuel_burned_per_second):
# вся ракета, сухая масса ЛМ, топливо ЛМ, кол-во топлива, сжигаемого ЛМ
# остальное не меняется
# то, что начинается с sp относится к separated part
    lunar_module = Vehicle(sp_current_mass, main_part.vehicle_position_x,
    main_part.vehicle_position_y, main_part.vehicle_velocity_x, main_part.vehicle_velocity_y,
    sp_vehicle_fuel_left, main_part.vehicle_orientation, main_part.thrust, 
    sp_fuel_burned_per_second)
    main_part.disconnection(lunar_module)

def connect(first, second):
    first.connecton(second)
    second = None
