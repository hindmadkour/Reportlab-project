"""
Example script showing how to customize financial data
"""

import requests
import json

# Example of custom financial data
custom_data = {
    "company_name": "Tech Innovations SARL",
    "report_date": "Décembre 2023",
    "financial_indicators": {
        "revenue": 1850000,
        "operational_costs": 920000,
        "gross_result": 930000,
        "estimated_taxes": 279000,
        "net_result": 651000,
        "growth_rate": 8.5
    },
    "synthetic_analysis": """
    Notre analyse financière montre une performance solide avec une croissance de 8,5% par rapport à l'année précédente. 
    Le chiffre d'affaires s'élève à 1 850 000 €, générant un résultat net de 651 000 € après impôts estimés à 279 000 €.
    Les coûts opérationnels sont bien maîtrisés à 49,7% du chiffre d'affaires, ce qui témoigne d'une gestion efficace des ressources.
    """
}

print("Exemple de données personnalisées pour le rapport financier :")
print(json.dumps(custom_data, indent=2, ensure_ascii=False))

print("\nPour utiliser ces données, vous pouvez :")
print("1. Modifier le dictionnaire FINANCIAL_DATA dans app.py")
print("2. Implémenter une API qui accepte ces données via POST")
print("3. Créer un formulaire HTML pour saisir ces données")