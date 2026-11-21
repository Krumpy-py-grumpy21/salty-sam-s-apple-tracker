import math

#math variables for position function


    #variables that can be found already

        #wheel stuff
wheel_diameter_cm = 8.745 #This size is specific to the lego spike prime wheel diameter size. Might not be used next year (specifically 2027-2028)
wheel_radius_cm = wheel_diameter_cm/2

        #measurements of robot size
width_of_robot = 18.2 
distance_of_wheel_from_center = 14.45/2
car_direction = 0 #measure the degree of direction each time, for real time adjustments.
car_hitboxFront = 11.5 #measure front in cm
car_hitboxBack =  7.5 #measure back in cm #total sides is 19cm
car_hitboxWidth = width_of_robot/2 #measure sides and divide in cm

        #variables founded from it

wheel_360deg_cm = round(wheel_diameter_cm*math.pi, 2)
wheel_1deg_cm = wheel_360deg_cm/360
area_wheel = wheel_radius_cm




map_size_width = 199.5 #Size of the official map in centimeters
map_size_height = 114.1






#The class containing all the important code

class robot_movement_functions():
    #Defines the origin aka initial position of the robot.
    def __init__(self, origin, first_rotate):  
        originx = origin[0]
        originy = origin[1]
        self.origin = (originx, originy, first_rotate)
        
    
    

    #Ignore the other comments, they're just me learning. This method converts a list of your data, (specifically robot rotations in degrees) into cartesian plane oordinates.
    def new_distance_coverter_all(self, hystory):    
        converted_hystory = []
        x_s, y_s, rotate_s = self.origin[0], self.origin[1], self.origin[2]
        # v = vector 
        #d = direction
            #I experimented with this new data converter, and realized that it was starting at the exact same position each time. To fix this, I should record its direction, and add the previous coordinates, which it is not doing.
        
        for step_raw, rotate in hystory:
            step = step_raw*wheel_1deg_cm
            rotate_s += rotate  # _s at the end of variable means stockpile.
            rad_ = math.radians(rotate_s)
    
            # hypotenuse already equals vector, but to find adjacent(x), it's cah function.
            x_s += math.cos(rad_)*step #because rad_ equals direction of robot, and step basically is hypotenuse.
            # hypotenuse already equals vector, but to find opposite(y), it's soh function.
            y_s += math.sin(rad_)*step

            converted_hystory.append((round(x_s, 3), round(y_s, 3), rotate_s))
        return converted_hystory
    
    
    
    
    
    #converts centimeters into the exact degrees the robot needs to turn to reach that amount
    def cm_to_rotation(self, cm_steps):
        value = cm_steps/wheel_1deg_cm
        return round(value, 2)
    
    
    
    
    #Does the oppsite of the above method, and converts robot's rotation
    def rotation_to_cm(self, rotation):
        value = rotation*wheel_1deg_cm
        return round(value)
    
    
    
    #With this method, you can set a goal on a cartesian plane you want the robot to reach, and if you used the other methods, you could find out how to set your robot where.
    def position_seeker(end_pos_goal, end_pos_achieve):
        if end_pos_goal == end_pos_achieve:
            print("Achieved goal.", end_pos_goal)
        else:
            x = end_pos_achieve[0]-end_pos_goal[0]
            y = end_pos_achieve[1]-end_pos_goal[1]
            print("go x", x, "go y", y)
            return x, y



    #finds the position of origin without too much measuring, Since the lego league map is so big, You could measure from the north west of your map to 40 cm south, 40 cm east and get the same value for measuring from the bottom left. You just need to specify the direction.
    def map_position_finder(compass_horizontal, compass_vertical, x, y):
        print("\n position finder arguments:   horiontal (left, right),   and vertical (up, down)\n")
        try:
            
            if compass_horizontal == "down":
                originx = x
            if compass_horizontal == "up":
                originx = map_size_height-x
            if compass_vertical == "left":
                originy = y
            if compass_vertical == "right":
                originy = map_size_width-y
    
            return originx, originy
        except:
            print("Error with your positional argument\n\n\n")

