import time
from dronekit import connect, VehicleMode, LocationGlobalRelative

def takeoff_land(aTargetAltitude):
    print ("Pre-arm checking...")
    
    while not vehicle.is_armable:
        print ("Pre-arm conditions are required")
        time.sleep(1)

    print("Flight Mode = GUIDED")
    # Copter should arm in GUIDED mode
    vehicle.mode    = VehicleMode("GUIDED")

    print("Arm")
    vehicle.armed   = True

    # Confirm vehicle armed before attempting to take off
    while not vehicle.armed:
        print ("Drone ready to takeoff.")
        time.sleep(1)

    print ("Takeoff")
    vehicle.simple_takeoff(aTargetAltitude) # Take off to target altitude

    # Wait until the vehicle reaches a safe height before processing the goto (otherwise the command
    #  after Vehicle.simple_takeoff will execute immediately).
    while True:
        print (" Yükseklik: ", vehicle.location.global_relative_frame.alt)
        #Break and return from function just below target altitude.
        if vehicle.location.global_relative_frame.alt>=aTargetAltitude*0.95:
            print ("Landing...")
            vehicle.mode = VehicleMode("LAND")
            break
        time.sleep(1)

try:
    vehicle = connect('/dev/ttyACM0',baud=921600)   # RAKIS Drone
    #vehicle = connect('127.0.0.1:14550', wait_ready=True)  # Simulation in Gazebo
except:
    print("Connection Failed !!")

try:
    aTargetAltitude=5
    target=int(aTargetAltitude)
    takeoff_land(target)
except:
    print("Please enter a acceptable altitude:")


