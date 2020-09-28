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
        self.current_mass -= active_part.raw_mass
        self.vehicle_fuel_left = active_part.total_fuel
        self.thrust = active_part.thrust
        self.fuel_burned_per_second = active_part.fuel_burned_per_second
        # TODO: MESSAGE THAT DISCONNECTION HAS OCCURRED (EGOR'S TASK)

    # TODO: MAKE A FUNCTION FOR A LUNAR MODULE DISCONNECTION AND CONNECTION

    # TODO: MAKE A FUNCTIONS FOR ROTATION AND THRUST

    # TODO: MAKE A CLASS OF ACTIVE_PARTS AND INCLUDE ALL CHARACTERISTICS SUCH AS:
    #  RAW MASS, FUEL MASS, FUEL BURNED PER SECOND (dm/dt = F/V, TO CALCULATE BASED ON THIS FORMULA)
    
    # 12345
   
    
