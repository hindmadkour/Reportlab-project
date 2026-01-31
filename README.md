# Application de Reporting Financier Automatisé / Automated Financial Reporting Application

Cette application web professionnelle génère des rapports financiers élégants au format PDF, dans un style comparable à celui d'un cabinet de conseil ou d'une banque d'investissement.

This professional web application generates elegant financial reports in PDF format, in a style comparable to that of a consulting firm or investment bank.

## Fonctionnalités / Features

- Interface web moderne et luxueuse avec palette de couleurs noir/doré
- Modern and luxurious web interface with black/gold color palette
- Génération automatique de rapports financiers PDF professionnels
- Automatic generation of professional financial PDF reports
- Design responsive (desktop & mobile)
- Responsive design (desktop & mobile)
- Données financières réalistes prédéfinies
- Predefined realistic financial data
- Animations et effets visuels raffinés
- Refined animations and visual effects

## Technologies utilisées / Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Génération PDF**: ReportLab
- **PDF Generation**: ReportLab
- **Design**: Approche minimaliste avec éléments dorés
- **Design**: Minimalist approach with golden elements

## Structure du projet / Project Structure

```
reportlab5/
│
├── app.py                 # Application Flask principale / Main Flask application
├── requirements.txt       # Dépendances Python / Python dependencies
├── README.md             # Documentation
│
├── templates/
│   └── index.html        # Page principale / Main page
│
└── static/
    └── css/
        └── style.css     # Styles personnalisés / Custom styles
```

## Installation et exécution / Installation and Execution

1. **Cloner le projet** (si nécessaire) ou naviguer vers le dossier du projet
1. **Clone the project** (if necessary) or navigate to the project folder

2. **Créer un environnement virtuel** (recommandé):
2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   ```

3. **Activer l'environnement virtuel**:
3. **Activate the virtual environment**:
   - Sur Windows:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Sur macOS/Linux:
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Installer les dépendances**:
4. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Lancer l'application**:
5. **Launch the application**:
   ```bash
   python app.py
   ```

6. **Accéder à l'application**:
6. **Access the application**:
   Ouvrez votre navigateur et rendez-vous à l'adresse: `http://127.0.0.1:5000`
   Open your browser and go to the address: `http://127.0.0.1:5000`

## Utilisation / Usage

1. Sur la page d'accueil, vous verrez un résumé des indicateurs financiers
1. On the home page, you will see a summary of financial indicators
2. Cliquez sur le bouton "Générer le rapport PDF"
2. Click on the "Générer le rapport PDF" button
3. Le rapport sera généré automatiquement et téléchargé au format PDF
3. The report will be generated automatically and downloaded in PDF format
4. Le rapport inclut:
4. The report includes:
   - Page de couverture élégante / Elegant cover page
   - Résumé exécutif / Executive summary
   - Tableau des indicateurs financiers / Financial indicators table
   - Analyse des performances / Performance analysis
   - Conclusion professionnelle / Professional conclusion
   - Pied de page avec numéro de page et mention de confidentialité / Footer with page number and confidentiality notice

## Personnalisation / Customization

Pour modifier les données financières, éditez le dictionnaire `FINANCIAL_DATA` dans le fichier `app.py`.

To modify the financial data, edit the `FINANCIAL_DATA` dictionary in the `app.py` file.

## Structure du rapport PDF généré / Generated PDF Report Structure

1. **Page de couverture** / **Cover Page**:
   - Titre: "Rapport Financier Annuel" / Title: "Annual Financial Report"
   - Nom de l'entreprise / Company name
   - Date de génération / Generation date

2. **Résumé exécutif** / **Executive Summary**:
   - Analyse synthétique des performances / Synthetic performance analysis

3. **Indicateurs financiers** / **Financial Indicators**:
   - Chiffre d'affaires / Revenue
   - Charges opérationnelles / Operating expenses
   - Résultat brut / Gross result
   - Impôts estimés / Estimated taxes
   - Résultat net / Net result
   - Taux de croissance / Growth rate

4. **Analyse des performances** / **Performance Analysis**:
   - Détail des résultats et interprétation / Detail of results and interpretation

5. **Conclusion** / **Conclusion**:
   - Synthèse et perspectives / Summary and perspectives

6. **Pied de page** / **Footer**:
   - Numéro de page / Page number
   - Mention de confidentialité / Confidentiality notice

## Design / Design

L'application utilise une palette de couleurs luxueuse:
The application uses a luxurious color palette:
- Noir (#0a0a0a) pour les éléments principaux / Black (#0a0a0a) for main elements
- Doré (#D4AF37) pour les accents et éléments importants / Gold (#D4AF37) for accents and important elements
- Gris clair (#f5f5f5) pour l'arrière-plan / Light gray (#f5f5f5) for the background
- Blanc (#ffffff) pour le contenu / White (#ffffff) for the content

La typographie est soignée avec des polices modernes et professionnelles, et l'interface inclut des animations subtiles pour améliorer l'expérience utilisateur.

Typography is carefully crafted with modern and professional fonts, and the interface includes subtle animations to enhance the user experience.

## Dépendances / Dependencies

- Flask: Framework web léger pour Python / Flask: Lightweight web framework for Python
- ReportLab: Bibliothèque de génération PDF / ReportLab: PDF generation library
- Bootstrap 5: Framework CSS pour le design responsive / Bootstrap 5: CSS framework for responsive design

## Auteur / Author

Hind Madkour  
Email: madkourhind@gmail.com

## Support / Support

Pour toute question ou problème technique, veuillez consulter la documentation de Flask et ReportLab:
For any questions or technical issues, please consult the Flask and ReportLab documentation:
- [Documentation Flask](https://flask.palletsprojects.com/) / [Flask Documentation](https://flask.palletsprojects.com/)
- [Documentation ReportLab](https://www.reportlab.com/docs/reportlab-userguide.pdf) / [ReportLab Documentation](https://www.reportlab.com/docs/reportlab-userguide.pdf)