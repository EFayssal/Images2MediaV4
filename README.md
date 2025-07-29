# 🔐 Images2 Secure Media Player Phase 2 

Application Flask pour importer, chiffrer, lire et déchiffrer des fichiers médias dans un format sécurisé `.Images2`.

---

## ✅ Objectif

Créer un lecteur média minimaliste qui :

- 📥 Importe des fichiers audio/vidéo (.mp4, .mp3, .avi, etc.)
- 🔐 Les chiffre avec AES 256 et les exporte en `.Images2`
- 🔓 Permet le déchiffrement et la restitution au format d’origine
- 🎵 Gère une playlist locale des médias utilisés
- 🧠 Protège l’accès grâce à une clé unique d’entreprise (stockée ou entrée à la première utilisation)

---

## 🧠 Technologies

- **Backend** : Python (Flask)
- **Frontend** : HTML / CSS
- **Crypto** : PyCryptodome (AES 256 bits, mode CBC)
- **Stockage de clé** : fichier local sécurisé (`key.txt`)

---

## 🚧 Avancement

| Fonctionnalité                                  | État         |
|-------------------------------------------------|--------------|
| Initialisation de projet Flask                  | ✅ Terminé    |
| Interface HTML + upload                         | ✅ Terminé    |
| Système de clé sécurisée (clé.txt)              | ✅ Terminé    |
| Chiffrement AES (.Images2)                      | ✅ Terminé    |
| Déchiffrement AES vers fichier original         | ✅ Terminé    |
| Gestion de playlist (liste des fichiers)        | ✅ Terminé    |
| Lecture dans navigateur (`<video>/<audio>`)     | 🟡 En cours   |
| Sécurisation de la clé (chiffrée + mot de passe)| 🟡 En cours   |
| Export .exe (via pyinstaller)                   | 🔲 À faire    |
| Documentation utilisateur                       | 🔲 À faire    |

---

## ▶️ Lancer l'application

```bash
# Installer les dépendances
pip install -r requirements.txt

# Lancer le serveur Flask
python app.py

📜 Licence
Projet interne - usage réservé à l’entreprise Images2

✍️ Auteur
Faissal EL HOUARI  - Projet BTS SIO SLAM 2025

