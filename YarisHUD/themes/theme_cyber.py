import pygame
import math
import config

class ThemeCyber:
    def __init__(self):
        try:
            self.font_geant = pygame.font.Font(config.FONT_PATH, 140)
            self.font_grand = pygame.font.Font(config.FONT_PATH, 50)
            self.font_moyen = pygame.font.Font(config.FONT_PATH, 30)
            self.font_petit = pygame.font.Font(config.FONT_PATH, 18)
        except:
            self.font_geant = pygame.font.SysFont("arial", 140)
            self.font_grand = pygame.font.SysFont("arial", 50)
            self.font_moyen = pygame.font.SysFont("arial", 30)
            self.font_petit = pygame.font.SysFont("arial", 18)

    def draw_arc(self, surface, x, y, radius, start_angle, end_angle, width, color):
        rect = (x - radius, y - radius, radius * 2, radius * 2)
        start_rad = math.radians(start_angle)
        end_rad = math.radians(end_angle)
        pygame.draw.arc(surface, color, rect, start_rad, end_rad, width)

    def dessiner(self, surface, data, est_nuit):
        vitesse, rpm, load, temp, batterie, _ = data
        
        c_princ = config.get_color("TEXTE_PRINC", est_nuit)
        c_sec   = config.get_color("TEXTE_SEC", est_nuit)
        c_alert = config.get_color("ALERT", est_nuit)
        cx, cy = config.LARGEUR // 2, config.HAUTEUR // 2

        # 1. VITESSE
        txt_v = self.font_geant.render(str(vitesse), True, c_princ)
        rect_v = txt_v.get_rect(center=(cx, cy - 15))
        surface.blit(txt_v, rect_v)
        
        lbl_kmh = self.font_petit.render("KM/H", True, c_sec)
        rect_lbl = lbl_kmh.get_rect(center=(cx, cy + 75))
        surface.blit(lbl_kmh, rect_lbl)

        # 2. JAUGE RPM (Gauche)
        pct_rpm = min(rpm / 5000, 1.0)
        self.draw_arc(surface, cx, cy, 220, 140, 210, 15, (40,40,40))
        if rpm > 0:
            angle_fin = 140 + (pct_rpm * 70)
            c_rpm = c_princ if rpm < 4000 else c_alert
            self.draw_arc(surface, cx, cy, 220, 140, angle_fin, 15, c_rpm)
        
        txt_rpm = self.font_petit.render(f"{rpm} RPM", True, c_sec)
        surface.blit(txt_rpm, (cx - 230, cy + 95)) # Position basse validée

        # 3. JAUGE PWR (Droite)
        pct_load = load / 100
        self.draw_arc(surface, cx, cy, 220, 330, 400, 15, (40,40,40))
        angle_fin = 330 + (pct_load * 70)
        c_load = (0, 255, 100) if load < 70 else (255, 50, 0)
        self.draw_arc(surface, cx, cy, 220, 330, angle_fin, 15, c_load)
        
        txt_load = self.font_petit.render(f"PWR {load}%", True, c_sec)
        surface.blit(txt_load, (cx + 240, cy - 10)) # Position droite validée

        # 4. TEMP (Bas)
        y_temp = cy + 130
        pygame.draw.rect(surface, (40,40,40), (cx - 100, y_temp, 200, 10))
        w_temp = min((temp / 100) * 200, 200)
        c_temp = c_princ if temp < 90 else c_alert
        if temp < 50: c_temp = (0, 100, 255)
        pygame.draw.rect(surface, c_temp, (cx - 100, y_temp, w_temp, 10))
        
        txt_temp = self.font_petit.render(f"{temp}°C", True, c_sec)
        rect_temp = txt_temp.get_rect(center=(cx, y_temp + 20))
        surface.blit(txt_temp, rect_temp)

        # 5. EV
        if rpm == 0:
            txt_ev = self.font_grand.render("EV", True, (0, 255, 120))
            bg_ev = pygame.Surface((100, 60))
            bg_ev.set_alpha(30)
            bg_ev.fill((0, 255, 0))
            surface.blit(bg_ev, (cx - 50, cy - 140))
            surface.blit(txt_ev, (cx - 30, cy - 140))

        # 6. BATTERIE (Sous PWR)
        lbl_bat = self.font_petit.render("BAT", True, c_sec)
        surface.blit(lbl_bat, (cx + 240, cy + 95))
        
        c_bat = c_princ
        if batterie < 50: c_bat = c_alert
        txt_bat = self.font_moyen.render(f"{batterie}%", True, c_bat)
        surface.blit(txt_bat, (cx + 240, cy + 115))