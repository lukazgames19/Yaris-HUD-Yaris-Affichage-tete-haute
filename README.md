# 🚗 Yaris Hybrid HUD (Cyberpunk Edition)

Un affichage tête haute (HUD) DIY pour Toyota Yaris 4 Hybride, basé sur Raspberry Pi et OBDII.
Design inspiré des interfaces Cyberpunk / Sci-Fi.

## ✨ Fonctionnalités

* **Connexion OBDII Bluetooth** : Récupération temps réel (Vitesse, RPM, Charge Moteur, Température Eau).
* **Dual Theme** :
    * 🔴 **Mode ZEN** : Minimaliste pour la conduite de nuit.
    * 🔵 **Mode CYBER** : Interface complète avec jauges dynamiques.
* **Gestion Jour/Nuit** : Bascule automatique des couleurs (Simulé ou Capteur).
* **Auto-Start** : Démarrage autonome sur Raspberry Pi.

## 🛠️ Matériel Requis

* **Ordinateur** : Raspberry Pi Zero 2 W.
* **Affichage** : Écran LCD 4.3" HDMI (Waveshare IPS 800x480).
* **Data** : Adaptateur OBDII Bluetooth (vLinker MC+).

## 📦 Installation

1.  Cloner le projet :
    ```bash
    git clone [https://github.com/lukazgames19/YarisHUD.git](https://github.com/lukazgames19/YarisHUD.git)
    cd YarisHUD
    ```

2.  Installer les dépendances :
    ```bash
    pip3 install pygame obd
    ```

3.  Lancer le HUD :
    ```bash
    python3 main.py
    ```
