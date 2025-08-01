# 🛠️ Projet Data Engineer – Analyse de Ventes (Python + SQLite)

Ce projet simple montre comment :
- Charger des données CSV avec Python et Pandas,
- Les stocker dans une base SQLite,
- Réaliser une analyse simple (CA par magasin).

## 📁 Structure du projet

data-engineer/
├── data/
│ └── ventes.csv
├── db/
│ └── ventes.db (généré automatiquement)
├── scripts/
│ ├── importer_csv.py
│ └── analyser_donnees.py
├── requirements.txt
├── run_project.py (optionnel)
└── README.md

markdown
Copier
Modifier

## 🧰 Prérequis

- Python 3.8+
- pip
- SQLite (inclus avec Python)
- VS Code + WSL (facultatif)

## 🚀 Installation

1. Cloner ou créer le dossier :
```bash
cd ~/data-engineer
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
Exécuter l'import des données :

bash
Copier
Modifier
python3 scripts/importer_csv.py
Analyser les données :

bash
Copier
Modifier
python3 scripts/analyser_donnees.py
📊 Exemple de sortie
markdown
Copier
Modifier
     magasin  total_ca
0      Lyon        90
1  Marseille       120
2      Paris       150
📦 Fichier requirements.txt
nginx
Copier
Modifier
pandas
✅ À venir
Export des résultats en Excel ou CSV

Dashboard Power BI connecté à SQLite

Intégration avec Docker

🧑‍💻 Auteur
Laurent J. – Projet personnel de formation Data Engineer