print("Enter the code as 'SEC-G2' or 'ERR-B1'")
code = str(input("Enter the six digit code: ").upper())
status_code = code[0:3]
sector_code = code[4:6]
if(status_code == "SEC"):
    if(sector_code == "G2"):
        print("MISSION STATUS: GREEN. Spacecraft is perfectly safe in Deep Space.")
    else:
        print( "MISSION STATUS: ORANGE. Orbit path needs a minor adjustment.")
   
elif(status_code == "ERR"):
    if(sector_code == "B1"):
        print("CRITICAL WARNING: Fuel line anomaly detected!")
    else:
        print("CRITICAL WARNING: Communication antenna misalignment!")
    
