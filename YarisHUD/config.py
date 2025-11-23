import os

# --- ÉCRAN ---
LARGEUR = 800
HAUTEUR = 480
HUD_MIROIR = True       # Mettre False pour tester sur PC à l'endroit
MODE_SIMULATION = True  # Mettre False dans la voiture
TEMPS_AUTOSTART = 10.0

# --- PALETTES DE COULEURS (JOUR / NUIT) ---
# Structure : { "NOM": {"JOUR": (R,G,B), "NUIT": (R,G,B)} }
PALETTE = {
    "FOND":        {"JOUR": (10, 10, 15),   "NUIT": (0, 0, 0)},
    "TEXTE_PRINC": {"JOUR": (0, 255, 255),  "NUIT": (255, 140, 0)},
    "TEXTE_SEC":   {"JOUR": (200, 200, 200),"NUIT": (100, 100, 100)},
    "ALERT":       {"JOUR": (255, 0, 0),    "NUIT": (200, 0, 0)}
}

# Helper pour récupérer la couleur
def get_color(nom, est_nuit):
    mode = "NUIT" if est_nuit else "JOUR"
    return PALETTE[nom][mode]

# --- CHEMINS ---
BASE_DIR = os.path.dirname(__file__)
FONT_PATH = os.path.join(BASE_DIR, "assets/fonts/Orbitron-Bold.ttf")
IMG_PATH = os.path.join(BASE_DIR, "assets/images/logo.png")