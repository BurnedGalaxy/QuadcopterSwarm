import rzm
from pymavlink import mavutil
import time

# Connecting to the drone via UDP port for SITL
copter = mavutil.mavlink_connection('udpin:localhost:14533')
copter.wait_heartbeat()

# Printing the Drone SYS_ID and component ID
print("Heartbeat from the system (system %u component %u)" %
        (copter.target_system, copter.target_component))

# Arming the drone
rzm.arm(copter)

# Setting GUIDED mode for commanding from companion computer
rzm.mode_set(copter, 'GUIDED')

# Taking off the vehicle
rzm.takeoff_drone(copter, 10)

time.sleep(10)

# Desired coordinates from the drone (NED)

x = 10
y = 0
z = -10

# Getting the initial coordinates (NED)
pre_msg = copter.recv_match(type='LOCAL_POSITION_NED', blocking=True).to_dict()

pre_x = pre_msg['x']
pre_y = pre_msg['y']
pre_z = pre_msg['z']

print("Initial coordinates x: %3d, y: %3d, z= %3d" %(pre_x, pre_y, pre_z))

# Moving the copter to the final coordinates
rzm.move_drone_ned(copter, x, y, z)

# Displaying the coordinates till the copter reaches its final position
while True:
    msg = copter.recv_match(type='LOCAL_POSITION_NED', blocking=True).to_dict()
    time.sleep(0.5)
    print("x: %3d, y: %3d, z= %3d" %(msg['x'], msg['y'], msg['z']))

    if (x-1 <= msg['x'] - pre_x <= x+1) and (y-1 <= msg['y'] - pre_y <= y+1) and (z <= msg['z'] - pre_z <= z+1):
        break
