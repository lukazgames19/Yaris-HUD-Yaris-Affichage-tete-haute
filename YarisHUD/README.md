# 🚗 Yaris Hybrid HUD (Cyberpunk Edition)

Un affichage tête haute (HUD) DIY pour Toyota Yaris 4 Hybride, basé sur Raspberry Pi et OBDII.
Design inspiré des interfaces Cyberpunk / Sci-Fi.

![Status](https://img.shields.io/badge/Status-Work_In_Progress-yellow)
![Python](https://img.shields.io/badge/Python-3.x-blue)

## ✨ Fonctionnalités

* **Connexion OBDII Bluetooth** : Récupération temps réel (Vitesse, RPM, Charge Moteur, Température Eau).
* **Dual Theme** :
    * 🔴 **Mode ZEN** : Minimaliste pour la conduite de nuit (inspiré Saab Night Panel).
    * 🔵 **Mode CYBER** : Interface complète avec jauges dynamiques et indicateur de batterie hybride.
* **Gestion Jour/Nuit** : Bascule automatique des couleurs via capteur de luminosité.
* **Auto-Start** : Démarrage autonome et résilient sur Raspberry Pi.
* **Miroir HUD** : Inversion automatique de l'affichage pour projection sur pare-brise.

## 🛠️ Matériel Requis

* **Ordinateur** : Raspberry Pi Zero 2 W (ou 3B+).
* **Affichage** : Écran LCD 4.3" HDMI (Waveshare IPS 800x480 recommandé).
* **Data** : Adaptateur OBDII Bluetooth (vLinker MC+ recommandé).
* **Capteur** : Module Photoresistor (KY-018) pour la luminosité.

## 📦 Installation

1.  Cloner le projet :
    ```bash
    git clone [https://github.com/TON_PSEUDO/YarisHUD.git](https://github.com/TON_PSEUDO/YarisHUD.git)
    cd YarisHUD
    ```

2.  Installer les dépendances :
    ```bash
    pip3 install -r requirements.txt
    ```

3.  Lancer le HUD :
    ```bash
    python3 main.py
    ```

## 🔧 Configuration

Le fichier `config.py` permet de modifier :
* Les couleurs des thèmes.
* La résolution de l'écran.
* Le mode Simulation (pour tester sans voiture).

## 📸 Aperçu

*(Ici tu pourras ajouter des captures d'écran de ton interface plus tard)*

## 📄 Licence

Projet sous licence MIT - libre de modification et de partage.