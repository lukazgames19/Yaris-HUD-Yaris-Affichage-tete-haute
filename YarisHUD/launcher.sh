#!/bin/bash
sleep 5

# CORRECTION ICI : lucas au lieu de pi
cd /home/lucas/YarisHUD

export DISPLAY=:0

while true; do
    echo "Lancement du HUD..."
    python3 main.py
    echo "HUD fermé ou planté. Redémarrage dans 2s..."
    sleep 2
done