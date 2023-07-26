starting_position = int(input("Enter Starting Position"))
ending_position = int(input("Enter Ending Position"))

starting_time = int(input("Enter Starting Time"))
ending_time = int(input("Enter Ending Time"))

velocity = (ending_position - starting_position / ending_time - starting_time)
acceleration = velocity / (ending_time - starting_time)
print("Velocity is " , velocity)
print("Acceleration is " , acceleration)
