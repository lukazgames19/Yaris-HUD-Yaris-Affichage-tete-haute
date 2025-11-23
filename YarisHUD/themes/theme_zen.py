import pygame
import config

class ThemeZen:
    def __init__(self):
        try:
            self.font_vitesse = pygame.font.Font(config.FONT_PATH, 200)
            self.font_unit = pygame.font.Font(config.FONT_PATH, 30)
            self.font_mini = pygame.font.Font(config.FONT_PATH, 20)
        except:
            self.font_vitesse = pygame.font.SysFont("arial", 200)
            self.font_unit = pygame.font.SysFont("arial", 30)
            self.font_mini = pygame.font.SysFont("arial", 20)

    def dessiner(self, surface, data, est_nuit):
        vitesse, rpm, load, temp, batterie, _ = data
        
        # Couleurs forcées pour le Zen
        if est_nuit:
            c_princ = (200, 50, 50) # Rouge Audi
            c_sec = (100, 30, 30)
            c_batt = (200, 50, 50)
        else:
            c_princ = (220, 220, 220)
            c_sec = (100, 100, 100)
            c_batt = (0, 200, 100)

        cx, cy = config.LARGEUR // 2, config.HAUTEUR // 2

        # 1. VITESSE
        txt_v = self.font_vitesse.render(str(vitesse), True, c_princ)
        rect_v = txt_v.get_rect(center=(cx, cy - 20))
        surface.blit(txt_v, rect_v)
        
        txt_unit = self.font_unit.render("km/h", True, c_sec)
        surface.blit(txt_unit, (cx - 35, cy + 80))

        # 2. BARRE BATTERIE (0-100%)
        pygame.draw.rect(surface, (30, 30, 30), (200, config.HAUTEUR - 20, 400, 4))
        
        pct_absolu = max(0.0, min(1.0, batterie / 100.0))
        w_bat = pct_absolu * 400
        
        c_dyn = c_batt
        if batterie < 40: c_dyn = (255, 100, 0)
        
        pygame.draw.rect(surface, c_dyn, (200, config.HAUTEUR - 20, w_bat, 4))
        
        txt_bat = self.font_mini.render(f"{batterie}%", True, (80, 80, 80))
        surface.blit(txt_bat, (610, config.HAUTEUR - 30))

        # 3. INDICATEUR EV
        if rpm == 0:
            pygame.draw.circle(surface, (0, 200, 100), (cx + 180, cy + 20), 10)
            lbl_ev = self.font_mini.render("EV", True, (0, 200, 100))
            surface.blit(lbl_ev, (cx + 200, cy + 10))