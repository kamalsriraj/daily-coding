rocket_specs = {
    "GSLV": {"min_fuel": 400, "max_wind": 45, "payload_max": 5000},
    "PSLV": {"min_fuel": 150, "max_wind": 55, "payload_max": 1750}
}
vehicle_name = (input("Enter the vehicle name 'GSLV' or 'PSLV' : ").upper())
fuel = float(input("Enter the current fuel(in tons):"))
wind_speed = float(input("Enter the current wind speed(in km/hr): "))
weight = float(input("Enter the target payload weight: "))

if vehicle_name in rocket_specs:
    rocket = rocket_specs[vehicle_name]
    if(fuel < rocket["min_fuel"]):
        print("LAUNCH ABORTED: Insufficient fuel payload!")
    elif(wind_speed > rocket["max_wind"]):
        print("LANCH HOLD:Wiind speed exceed structural safety thresholds")
    elif(weight > rocket["payload_max"]):
        print("LAUNCH ABORTED: Payload weight capacity exceeded!")
    else:
        print(f"LAUNCH AUTHORIZED! Safe flight vector locked for {vehicle_name}.")
    




 
