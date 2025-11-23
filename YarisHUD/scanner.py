import obd
import time

LOG_FILE = "rapport_obd.txt"

def log(message):
    print(message)
    with open(LOG_FILE, "a") as f:
        f.write(message + "\n")

log("--- SCAN YARIS ---")
try:
    connection = obd.OBD()
    if not connection.is_connected():
        log("ECHEC CONNEXION")
        exit()
        
    cmds = [obd.commands.SPEED, obd.commands.RPM, obd.commands.ENGINE_LOAD, obd.commands.COOLANT_TEMP]
    
    for cmd in cmds:
        if cmd in connection.supported_commands:
            val = connection.query(cmd)
            log(f"{cmd.name}: {val.value}")
        else:
            log(f"{cmd.name}: NON SUPPORTÉ")
except Exception as e:
    log(f"ERREUR: {e}")