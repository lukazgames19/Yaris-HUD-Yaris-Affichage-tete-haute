import pygame
import time
import config
from telemetrie import Telemetrie
from themes.theme_cyber import ThemeCyber
from themes.theme_zen import ThemeZen

# --- INITIALISATION ---
pygame.init()
ecran = pygame.display.set_mode((config.LARGEUR, config.HAUTEUR))
pygame.display.set_caption("YARIS HUD - SYSTEM V2.0")

# Modules
moteur_data = Telemetrie(simulation=config.MODE_SIMULATION)
theme_cyber = ThemeCyber()
theme_zen = ThemeZen()

# Optimisation : On prépare le voile noir (Nuit) UNE SEULE FOIS
voile_noir = pygame.Surface((config.LARGEUR, config.HAUTEUR))
voile_noir.fill((0, 0, 0))
voile_noir.set_alpha(75) # Réglage sombre

# Chargement Logo
try:
    logo_brut = pygame.image.load(config.IMG_PATH)
    scale = 150 / logo_brut.get_width()
    logo_img = pygame.transform.scale(logo_brut, (150, int(logo_brut.get_height() * scale)))
except:
    logo_img = None

# Polices Globales
try:
    font_hub = pygame.font.Font(config.FONT_PATH, 40)
    font_boot = pygame.font.Font(config.FONT_PATH, 18)
except:
    font_hub = pygame.font.SysFont("arial", 40, bold=True)
    font_boot = pygame.font.SysFont("arial", 18)

# --- ETATS ---
ETAT_BOOT = 0
ETAT_HUB = 1
ETAT_HUD = 2

etat_actuel = ETAT_BOOT
current_theme_name = "CYBER"

# Variables Boot
logs_boot = ["SYSTEM INIT...", "LOADING KERNEL...", "LOADING THEMES...", "OBD CONNECTED.", "READY."]
ligne_log = 0
last_log_time = time.time()

# Variables Hub
timer_hub_start = 0
est_nuit = False

# --- BOUCLE ---
running = True
clock = pygame.time.Clock()
surface_temp = pygame.Surface((config.LARGEUR, config.HAUTEUR))

while running:
    # A. EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: running = False
        
        # Touche N pour simuler la nuit
        if event.type == pygame.KEYDOWN and event.key == pygame.K_n:
            est_nuit = not est_nuit
            print(f"Mode Nuit: {est_nuit}")

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if config.HUD_MIROIR: x = config.LARGEUR - x

            # Hub Logic
            if etat_actuel == ETAT_HUB:
                # Gauche (Cyber)
                if 50 < x < 350 and 100 < y < 400:
                    current_theme_name = "CYBER"
                    etat_actuel = ETAT_HUD
                # Droite (Zen)
                if 450 < x < 750 and 100 < y < 400:
                    current_theme_name = "ZEN"
                    etat_actuel = ETAT_HUD
            
            # HUD Logic (Retour)
            elif etat_actuel == ETAT_HUD:
                if 0 < x < 150 and 0 < y < 150:
                    etat_actuel = ETAT_HUB
                    timer_hub_start = time.time()

    # B. DESSIN
    couleur_fond = config.get_color("FOND", est_nuit)
    surface_temp.fill(couleur_fond)

    # --- BOOT ---
    if etat_actuel == ETAT_BOOT:
        if time.time() - last_log_time > 0.4:
            ligne_log += 1
            last_log_time = time.time()
        if ligne_log >= len(logs_boot) + 2:
            etat_actuel = ETAT_HUB
            timer_hub_start = time.time()
            
        if logo_img:
            surface_temp.blit(logo_img, (config.LARGEUR//2 - 75, 40))
        
        for i in range(min(ligne_log, len(logs_boot))):
            c_log = config.get_color("TEXTE_PRINC", est_nuit)
            txt = font_boot.render(logs_boot[i], True, c_log)
            rect = txt.get_rect(center=(config.LARGEUR//2, 200 + (i*30)))
            surface_temp.blit(txt, rect)

    # --- HUB ---
    elif etat_actuel == ETAT_HUB:
        elapsed = time.time() - timer_hub_start
        if elapsed > config.TEMPS_AUTOSTART:
            etat_actuel = ETAT_HUD
            
        c_txt = config.get_color("TEXTE_PRINC", est_nuit)
        c_sec = config.get_color("TEXTE_SEC", est_nuit)
        c_alert = config.get_color("ALERT", est_nuit)

        # Btn Cyber
        pygame.draw.rect(surface_temp, c_sec, (50, 100, 300, 300), border_radius=15)
        pygame.draw.rect(surface_temp, c_txt, (50, 100, 300, 300), 4, border_radius=15)
        surface_temp.blit(font_hub.render("CYBER", True, c_txt), (90, 220))

        # Btn Zen
        pygame.draw.rect(surface_temp, c_sec, (450, 100, 300, 300), border_radius=15)
        pygame.draw.rect(surface_temp, c_alert, (450, 100, 300, 300), 4, border_radius=15)
        surface_temp.blit(font_hub.render("ZEN", True, c_alert), (530, 220))
        
        reste = int(config.TEMPS_AUTOSTART - elapsed)
        surface_temp.blit(font_boot.render(f"AUTOSTART: {reste}", True, (255,255,255)), (350, 450))

    # --- HUD ---
    elif etat_actuel == ETAT_HUD:
        data = moteur_data.get_data()
        
        if current_theme_name == "CYBER":
            theme_cyber.dessiner(surface_temp, data, est_nuit)
        elif current_theme_name == "ZEN":
            theme_zen.dessiner(surface_temp, data, est_nuit)

    # Assombrissement Nuit (Optimisé)
    if est_nuit:
        surface_temp.blit(voile_noir, (0, 0))

    # Miroir
    if config.HUD_MIROIR:
        surface_finale = pygame.transform.flip(surface_temp, True, False)
    else:
        surface_finale = surface_temp

    ecran.blit(surface_finale, (0, 0))
    pygame.display.flip()
    clock.tick(30)

pygame.quit()