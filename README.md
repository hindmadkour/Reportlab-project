# Application de Reporting Financier Automatisé

Cette application web professionnelle génère des rapports financiers élégants au format PDF, dans un style comparable à celui d'un cabinet de conseil ou d'une banque d'investissement.

## Fonctionnalités

- Interface web moderne et luxueuse avec palette de couleurs noir/doré
- Génération automatique de rapports financiers PDF professionnels
- Design responsive (desktop & mobile)
- Données financières réalistes prédéfinies
- Animations et effets visuels raffinés

## Captures d'écran

![Dashboard](static/images/dashboard.png)

## Technologies utilisées

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Génération PDF**: ReportLab
- **Design**: Approche minimaliste avec éléments dorés

## Structure du projet

```
reportlab5/
│
├── app.py                 # Application Flask principale
├── requirements.txt       # Dépendances Python
├── README.md             # Documentation
│
├── templates/
│   └── index.html        # Page principale
│
└── static/
    └── css/
        └── style.css     # Styles personnalisés
```

## Installation et exécution

1. **Cloner le projet** (si nécessaire) ou naviguer vers le dossier du projet

2. **Créer un environnement virtuel** (recommandé):
   ```bash
   python -m venv venv
   ```

3. **Activer l'environnement virtuel**:
   - Sur Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Sur macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Installer les dépendances**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Lancer l'application**:
   ```bash
   python app.py
   ```

6. **Accéder à l'application**:
   Ouvrez votre navigateur et rendez-vous à l'adresse: `http://127.0.0.1:5000`

## Utilisation

1. Sur la page d'accueil, vous verrez un résumé des indicateurs financiers
2. Cliquez sur le bouton "Générer le rapport PDF"
3. Le rapport sera généré automatiquement et téléchargé au format PDF
4. Le rapport inclut:
   - Page de couverture élégante
   - Résumé exécutif
   - Tableau des indicateurs financiers
   - Analyse des performances
   - Conclusion professionnelle
   - Pied de page avec numéro de page et mention de confidentialité

## Personnalisation

Pour modifier les données financières, éditez le dictionnaire `FINANCIAL_DATA` dans le fichier `app.py`.

## Structure du rapport PDF généré

1. **Page de couverture**:
   - Titre: "Rapport Financier Annuel"
   - Nom de l'entreprise
   - Date de génération

2. **Résumé exécutif**:
   - Analyse synthétique des performances

3. **Indicateurs financiers**:
   - Chiffre d'affaires
   - Charges opérationnelles
   - Résultat brut
   - Impôts estimés
   - Résultat net
   - Taux de croissance

4. **Analyse des performances**:
   - Détail des résultats et interprétation

5. **Conclusion**:
   - Synthèse et perspectives

6. **Pied de page**:
   - Numéro de page
   - Mention de confidentialité

## Design

L'application utilise une palette de couleurs luxueuse:
- Noir (#0a0a0a) pour les éléments principaux
- Doré (#D4AF37) pour les accents et éléments importants
- Gris clair (#f5f5f5) pour l'arrière-plan
- Blanc (#ffffff) pour le contenu

La typographie est soignée avec des polices modernes et professionnelles, et l'interface inclut des animations subtiles pour améliorer l'expérience utilisateur.

## Dépendances

- Flask: Framework web léger pour Python
- ReportLab: Bibliothèque de génération PDF
- Bootstrap 5: Framework CSS pour le design responsive

## Auteur

Hind Madkour  
Email: madkourhind@gmail.com

## Support

Pour toute question ou problème technique, veuillez consulter la documentation de Flask et ReportLab:
- [Documentation Flask](https://flask.palletsprojects.com/)
- [Documentation ReportLab](https://www.reportlab.com/docs/reportlab-userguide.pdf)