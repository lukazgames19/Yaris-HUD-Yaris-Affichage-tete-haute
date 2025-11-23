import time
import random
import math

try:
    import obd
    OBD_INSTALLE = True
except ImportError:
    OBD_INSTALLE = False

class Telemetrie:
    def __init__(self, simulation=False):
        self.simulation = simulation
        self.connection = None
        self.est_connecte = False
        
        # Stockage données
        self.vitesse = 0
        self.rpm = 0
        self.load = 0
        self.temp = 0
        self.batterie = 60 # Départ à 60%

        if not self.simulation and OBD_INSTALLE:
            self.connecter()

    def connecter(self):
        try:
            # fast=False est plus stable pour le vLinker
            self.connection = obd.Async(fast=False, timeout=30)
            self.connection.watch(obd.commands.SPEED)
            self.connection.watch(obd.commands.RPM)
            self.connection.watch(obd.commands.ENGINE_LOAD)
            self.connection.watch(obd.commands.COOLANT_TEMP)
            self.connection.start()
            self.est_connecte = self.connection.is_connected()
        except:
            self.est_connecte = False

    def get_data(self):
        """
        Retourne : (vitesse, rpm, load, temp, batterie, est_connecte)
        """
        
        # --- MODE SIMULATION ---
        if self.simulation or not self.est_connecte:
            t = time.time()
            self.vitesse = int(abs(math.sin(t * 0.5)) * 110)
            
            # Simulation RPM Hybride (0 si vitesse faible parfois)
            if self.vitesse < 10 and random.random() > 0.5: 
                self.rpm = 0
            else: 
                self.rpm = int(self.vitesse * 35) + random.randint(-50, 50)
            
            self.load = int(abs(math.sin(t * 0.5 + 0.5)) * 100)
            self.temp = int(min(90, t * 2))
            
            # Simulation Batterie
            if self.load > 50: self.batterie -= 0.1
            else: self.batterie += 0.1
            
            # Bornes batterie 40-80%
            self.batterie = max(40, min(80, self.batterie))

            return self.vitesse, self.rpm, self.load, self.temp, int(self.batterie), False

        # --- MODE RÉEL ---
        if self.connection and self.connection.is_connected():
            self.vitesse = int(self.connection.query(obd.commands.SPEED).value.magnitude or 0)
            self.rpm = int(self.connection.query(obd.commands.RPM).value.magnitude or 0)
            self.load = int(self.connection.query(obd.commands.ENGINE_LOAD).value.magnitude or 0)
            self.temp = int(self.connection.query(obd.commands.COOLANT_TEMP).value.magnitude or 0)
            
            # Note: La batterie réelle demandera un PID spécifique plus tard
            return self.vitesse, self.rpm, self.load, self.temp, 60, True
            
        return 0, 0, 0, 0, 0, False