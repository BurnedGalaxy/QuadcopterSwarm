## Each side tracing is the implimentation of the movement_test.py program

from  pymavlink import mavutil
import rzm
import time

# Getting heartbeat from the vehicle
copter = mavutil.mavlink_connection('udpin:localhost:14533')
copter.wait_heartbeat()

# Printing the SYS_ID and the component ID of the vehicle
print("Heartbeat from the system (system %u component %u)" %
        (copter.target_system, copter.target_component))

# Distance in metres of the square to be traced
side = 10

# side 1
print("Side 1")
pre_msg = copter.recv_match(type='LOCAL_POSITION_NED', blocking=True).to_dict()
pre_x = pre_msg['x']

rzm.move_drone_ned(copter, side, 0, 0)

print("Approaching the first vertex...")
while True:
    msg = copter.recv_match(type='LOCAL_POSITION_NED', blocking=True).to_dict()
    if (side-1 <= msg['x'] - pre_x <= side+1):
        break

# side 2
print("Side 2")
pre_msg = copter.recv_match(type='LOCAL_POSITION_NED', blocking=True).to_dict()
pre_y = pre_msg['y']

rzm.move_drone_ned(copter, 0, side, 0)

print("Approaching the second vertex...")
while True:
    msg = copter.recv_match(type='LOCAL_POSITION_NED', blocking=True).to_dict()
    if (side-1 <= msg['y'] - pre_y <= side+1):
        break

# side 3
print("Side 3")
pre_msg = copter.recv_match(type='LOCAL_POSITION_NED', blocking=True).to_dict()
pre_x = pre_msg['x']

rzm.move_drone_ned(copter, -side, 0, 0)

print("Approaching the third vertex...")
while True:
    msg = copter.recv_match(type='LOCAL_POSITION_NED', blocking=True).to_dict()
    if (-side-1 <= msg['x'] - pre_x <= -side+1):
        break

# side 4
print("Side 4")
pre_msg = copter.recv_match(type='LOCAL_POSITION_NED', blocking=True).to_dict()
pre_y = pre_msg['y']

rzm.move_drone_ned(copter, 0, -side, 0)

print("Approaching the fourth vertex...")
while True:
    msg = copter.recv_match(type='LOCAL_POSITION_NED', blocking=True).to_dict()
    if (-side-1 <= msg['y'] - pre_y <= -side+1):
        break
