from pymavlink import mavutil
import rzm
import time

# Start a connection via UDP port to SITL

print("before connecting")
copter = mavutil.mavlink_connection('udpin:127.0.0.1:14533')

# Wait for the heartbeat
drone.wait_heartbeat()

# Printing the system id and component id of the drone
print("Heartbeat from system (system %u component %u)"
        %(drone.target_system, drone.target_component))

# Arming
rzm.arm(copter)

time.sleep(5)

# disarming
rzm.disarm(copter)
