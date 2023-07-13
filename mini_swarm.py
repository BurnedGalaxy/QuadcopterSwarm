from pymavlink import mavutil
from geopy.distance import geodesic
import time

copter1 = mavutil.mavlink_connection("udpin:127.0.0.1:14560")
copter1.wait_heartbeat()
print("Heartbeat from copter1: system %u, component %u" %
        (copter1.target_system, copter1.target_component))

copter2 = mavutil.mavlink_connection("udpin:127.0.0.1:14570")
copter2.wait_heartbeat()
print("Heartbeat from copter2: system %u, component %u" %
        (copter2.target_system, copter2.target_component))


gps1 = copter1.recv_match(type='GLOBAL_POSITION_INT', blocking=True).to_dict()
print(gps1)
