from pymavlink import mavutil
import rzm
import time

# Starting a connection
    copter = mavutil.mavlink_connection('udpin:localhost:14533')

# Waiting for the first heartbeat
    copter.wait_heartbeat()

# Printing the SYS_ID and the component id of the drone
    print("Heartbeat from the system (system %u component %u)" %
            (drone.target_system, drone.target_component))

# arming:
    rzm.arm(copter)

# guided mode set for receiving commands
    rzm.mode_set(copter, 'GUIDED')

# taking off:
    rzm.takeoff_drone(drone, 10)

# wait till takeoff
    time.sleep(20)

# landing:
    rzm.land_drone(drone, 0, 0)
