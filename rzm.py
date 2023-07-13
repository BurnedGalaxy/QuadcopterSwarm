###############################################################
##           Library for working with multirotors            ##
##                    Based on pymavlink                     ##
##             Created by Ahmed Razim, Jul 2023              ##
###############################################################

from pymavlink import mavutil
import sys

# Printing ACK messages
def print_ack(drone):
    print(drone.recv_match(type='COMMAND_ACK', blocking=True))

# Arming the vehicle
def arm(drone):
    drone.mav.command_long_send(drone.target_system, drone.target_component,
            mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM, 0, 1, 0, 0, 0, 0, 0, 0)
    print_ack(drone)

# Disarming the vehicle
def disarm(drone):
    drone.mav.command_long_send(drone.target_system, drone.target_component,
            mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM, 0, 0, 0, 0, 0, 0, 0, 0)
    print_ack(drone)

# Setting the flight mode
def mode_set(drone, mode):

    if mode not in drone.mode_mapping():
        print('Unknown mode : {}'.format(mode))
        print('Try:', list(drone.mode_mapping().keys()))
        sys.exit(1)

    mode_id = drone.mode_mapping()[mode]
    drone.set_mode(mode_id)
    print_ack(drone)

# Taking off the vehicle
def takeoff_drone(drone, alt):
    drone.mav.command_long_send(drone.target_system, drone.target_component,
            mavutil.mavlink.MAV_CMD_NAV_TAKEOFF, 0, 0, 0, 0, 0, 0, 0, alt)
    print_ack(drone)

# Landing the vehicle
def land_drone(drone, lat, lon):
    drone.mav.command_long_send(drone.target_system, drone.target_component,
            mavutil.mavlink.MAV_CMD_NAV_LAND, 0, 0, 0, 0, 0, lat, lon, 0)
    print_ack(drone)

# Moving the vehicle to a desired distance (NED)
def move_drone_ned(drone, x, y, z):
    drone.mav.send(mavutil.mavlink.MAVLink_set_position_target_local_ned_message(
        10, drone.target_system, drone.target_component,
        mavutil.mavlink.MAV_FRAME_LOCAL_OFFSET_NED, int(0b110111111000), x, y, z,
        0, 0, 0, 0, 0, 0, 0, 0))

# Moving the vehicle to a specific GPS coordinates
def move_drone_global(drone, lat, lon, alt):
    drone.mav.send(mavutil.mavlink.MAVLink_set_position_target_global_int_message(
        10, drone.target_system, drone.target_component,
        mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, int(0b110111111000),
        int(lat * 10 ** 7), int(lon * 10 ** 7), alt,
        0, 0, 0, 0, 0, 0, 0, 0))
