from flask import Flask, render_template, request, send_file, jsonify
import io
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from datetime import datetime
import os

app = Flask(__name__)

# Sample financial data for multiple enterprises
ENTERPRISE_DATA = {
    'luxury_finance': {
        'company_name': 'Luxury Finance Corp',
        'report_date': datetime.now().strftime('%B %d, %Y'),
        'financial_indicators': {
            'revenue': 2450000,
            'operational_costs': 1250000,
            'gross_result': 1200000,
            'estimated_taxes': 360000,
            'net_result': 840000,
            'growth_rate': 12.5
        },
        'synthetic_analysis': """
        Notre analyse financière montre une performance solide avec une croissance de 12,5% par rapport à l'année précédente. 
        Le chiffre d'affaires s'élève à 2 450 000 €, générant un résultat net de 840 000 € après impôts estimés à 360 000 €.
        Les coûts opérationnels sont bien maîtrisés à 51% du chiffre d'affaires, ce qui témoigne d'une gestion efficace des ressources.
        """
    },
    'tech_innovations': {
        'company_name': 'Tech Innovations SARL',
        'report_date': datetime.now().strftime('%B %d, %Y'),
        'financial_indicators': {
            'revenue': 1850000,
            'operational_costs': 920000,
            'gross_result': 930000,
            'estimated_taxes': 279000,
            'net_result': 651000,
            'growth_rate': 8.5
        },
        'synthetic_analysis': """
        Notre analyse financière montre une performance solide avec une croissance de 8,5% par rapport à l'année précédente. 
        Le chiffre d'affaires s'élève à 1 850 000 €, générant un résultat net de 651 000 € après impôts estimés à 279 000 €.
        Les coûts opérationnels sont bien maîtrisés à 49,7% du chiffre d'affaires, ce qui témoigne d'une gestion efficace des ressources.
        """
    },
    'global_services': {
        'company_name': 'Global Services Ltd',
        'report_date': datetime.now().strftime('%B %d, %Y'),
        'financial_indicators': {
            'revenue': 3200000,
            'operational_costs': 1800000,
            'gross_result': 1400000,
            'estimated_taxes': 420000,
            'net_result': 980000,
            'growth_rate': 15.2
        },
        'synthetic_analysis': """
        Notre analyse financière montre une performance exceptionnelle avec une croissance de 15,2% par rapport à l'année précédente. 
        Le chiffre d'affaires s'élève à 3 200 000 €, générant un résultat net de 980 000 € après impôts estimés à 420 000 €.
        Les coûts opérationnels sont optimisés à 56,3% du chiffre d'affaires, démontrant une excellente maîtrise des dépenses.
        """
    }
}

# Default financial data
FINANCIAL_DATA = ENTERPRISE_DATA['luxury_finance']
@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html', data=FINANCIAL_DATA, enterprises=ENTERPRISE_DATA)

@app.route('/select-enterprise/<enterprise_id>')
def select_enterprise(enterprise_id):
    """Select an enterprise and return its data"""
    if enterprise_id in ENTERPRISE_DATA:
        return jsonify(ENTERPRISE_DATA[enterprise_id])
    else:
        return jsonify({'error': 'Enterprise not found'}), 404
@app.route('/generate-report', methods=['POST'])
def generate_report():
    """Generate and return the financial PDF report"""
    try:
        # Get data from request (in a real app, this would come from form inputs)
        data = request.get_json() or FINANCIAL_DATA
        
        # Create a bytes buffer for the PDF
        buffer = io.BytesIO()
        
        # Create the PDF document
        doc = SimpleDocTemplate(buffer, pagesize=A4, 
                                rightMargin=72, leftMargin=72,
                                topMargin=72, bottomMargin=18)
        
        # Container for the 'Flowable' objects
        story = []
        
        # Styles
        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name='CustomTitle',
                                  parent=styles['Heading1'],
                                  fontSize=24,
                                  spaceAfter=30,
                                  textColor=colors.HexColor('#D4AF37'),  # Gold color
                                  alignment=1))  # Center alignment
        
        styles.add(ParagraphStyle(name='CustomHeading',
                                  parent=styles['Heading2'],
                                  fontSize=16,
                                  spaceAfter=12,
                                  textColor=colors.HexColor('#000000')))
        
        styles.add(ParagraphStyle(name='CustomBody',
                                  parent=styles['Normal'],
                                  fontSize=10,
                                  spaceAfter=12,
                                  textColor=colors.HexColor('#333333')))
        
        styles.add(ParagraphStyle(name='CustomSubHeading',
                                  parent=styles['Heading3'],
                                  fontSize=12,
                                  spaceAfter=8,
                                  textColor=colors.HexColor('#000000')))
        
        # Cover page
        story.append(Spacer(1, 2*inch))
        story.append(Paragraph("Rapport Financier Annuel", styles['CustomTitle']))
        story.append(Spacer(1, 0.5*inch))
        story.append(Paragraph(data['company_name'], styles['CustomHeading']))
        story.append(Spacer(1, 0.2*inch))
        story.append(Paragraph(data['report_date'], styles['CustomBody']))
        story.append(PageBreak())
        
        # Executive Summary
        story.append(Paragraph("Résumé Exécutif", styles['CustomHeading']))
        story.append(Paragraph(data['synthetic_analysis'], styles['CustomBody']))
        story.append(Spacer(1, 0.3*inch))
        
        # Financial Table
        story.append(Paragraph("Indicateurs Financiers Clés", styles['CustomHeading']))
        
        # Prepare table data
        financial_data = data['financial_indicators']
        table_data = [
            ['Indicateur', 'Valeur'],
            ['Chiffre d\'affaires', f"{financial_data['revenue']:,} €"],
            ['Charges opérationnelles', f"{financial_data['operational_costs']:,} €"],
            ['Résultat brut', f"{financial_data['gross_result']:,} €"],
            ['Impôts estimés', f"{financial_data['estimated_taxes']:,} €"],
            ['Résultat net', f"{financial_data['net_result']:,} €"],
            ['Taux de croissance (%)', f"{financial_data['growth_rate']}%"]
        ]
        
        # Create table
        table = Table(table_data, colWidths=[3*inch, 2*inch])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#000000')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.HexColor('#FFFFFF')),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#F5F5F5')),
            ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#CCCCCC')),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 10),
        ]))
        
        story.append(table)
        story.append(Spacer(1, 0.3*inch))
        
        # Key Performance Indicators
        story.append(Paragraph("Ratio de Performance Clés", styles['CustomHeading']))
        
        # Calculate additional KPIs
        revenue = financial_data['revenue']
        operational_costs = financial_data['operational_costs']
        gross_result = financial_data['gross_result']
        net_result = financial_data['net_result']
        
        kpi_data = [
            ['Ratio', 'Valeur', 'Interprétation'],
            ['Marge brute', f"{(gross_result/revenue)*100:.1f}%", 'Rentabilité avant frais généraux'],
            ['Marge nette', f"{(net_result/revenue)*100:.1f}%", 'Rentabilité finale'],
            ['Charge opérationnelle', f"{(operational_costs/revenue)*100:.1f}%", 'Effort de gestion'],
            ['Productivité', f"{revenue/100:.0f} €/pers", 'Chiffre d\'affaires par employé*']
        ]
        
        # Create KPI table
        kpi_table = Table(kpi_data, colWidths=[2*inch, 1*inch, 2*inch])
        kpi_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#000000')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.HexColor('#FFFFFF')),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#F5F5F5')),
            ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#CCCCCC')),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 10),
            ('ALIGN', (1, 1), (1, -1), 'RIGHT'),  # Right align values
        ]))
        
        story.append(kpi_table)
        story.append(Paragraph("* Estimation basée sur 100 équivalents temps plein", styles['CustomSubHeading']))
        story.append(Spacer(1, 0.3*inch))
        
        # Performance Analysis
        story.append(Paragraph("Analyse des Performances", styles['CustomHeading']))
        performance_text = f"""
        Au cours de cette période, {data['company_name']} a démontré une croissance robuste de {financial_data['growth_rate']}%, 
        atteignant un chiffre d'affaires de {financial_data['revenue']:,} €. Cette performance s'explique par une gestion optimale 
        des coûts opérationnels qui représentent {financial_data['operational_costs']/financial_data['revenue']*100:.1f}% 
        du chiffre d'affaires, permettant ainsi un résultat brut de {financial_data['gross_result']:,} €.
        <br/><br/>
        Après déduction des impôts estimés à {financial_data['estimated_taxes']:,} €, le résultat net s'établit à 
        {financial_data['net_result']:,} €, reflétant une rentabilité solide de l'entreprise avec une marge nette de 
        {(financial_data['net_result']/financial_data['revenue'])*100:.1f}%.
        """
        story.append(Paragraph(performance_text, styles['CustomBody']))
        story.append(Spacer(1, 0.3*inch))
        
        # Market Positioning
        story.append(Paragraph("Positionnement Concurrentiel", styles['CustomHeading']))
        market_text = f"""
        Dans un contexte économique marqué par l'inflation et la volatilité des marchés, {data['company_name']} 
        démontre une résilience remarquable. Avec une marge nette de {(financial_data['net_result']/financial_data['revenue'])*100:.1f}%, 
        l'entreprise se positionne favorablement par rapport à la moyenne sectorielle estimée à 8-10%.
        <br/><br/>
        La croissance de {financial_data['growth_rate']}% dépasse l'indice du marché (+3,2%), témoignant d'une stratégie 
        commerciale efficace et d'une capacité d'innovation reconnue.
        """
        story.append(Paragraph(market_text, styles['CustomBody']))
        story.append(Spacer(1, 0.3*inch))
        
        # Strategic Outlook
        story.append(Paragraph("Perspectives Stratégiques", styles['CustomHeading']))
        outlook_text = """
        Pour l'exercice prochain, nous anticipons une stabilisation du marché avec une croissance modérée de 4-6%. 
        Notre stratégie se concentrera sur trois axes :
        <br/><br/>
        • Optimisation continue de notre structure de coûts<br/>
        • Diversification de notre portefeuille client<br/>
        • Investissement dans l'innovation et la digitalisation
        <br/><br/>
        Ces initiatives devraient permettre de maintenir notre avantage concurrentiel et de générer une croissance 
        durable dans les années à venir.
        """
        story.append(Paragraph(outlook_text, styles['CustomBody']))
        story.append(Spacer(1, 0.3*inch))
        
        # Conclusion
        story.append(Paragraph("Conclusion", styles['CustomHeading']))
        conclusion_text = f"""
        Les résultats financiers de l'exercice démontrent la solidité de notre modèle économique et la qualité 
        de notre gestion. Avec un résultat net de {financial_data['net_result']:,} € et une croissance de {financial_data['growth_rate']}%, 
        {data['company_name']} confirme sa trajectoire de performance.
        <br/><br/>
        Nous restons engagés à maintenir cette dynamique tout en explorant de nouvelles opportunités de développement, 
        assurant ainsi la création de valeur pour nos actionnaires et partenaires.
        """
        story.append(Paragraph(conclusion_text, styles['CustomBody']))
        
        # Build PDF
        doc.build(story, 
                  onFirstPage=lambda canvas, doc: _draw_footer(canvas, doc, data),
                  onLaterPages=lambda canvas, doc: _draw_footer(canvas, doc, data))
        
        # Reset buffer pointer to the beginning
        buffer.seek(0)
        
        # Return the PDF as a downloadable attachment
        return send_file(
            buffer,
            as_attachment=True,
            download_name=f"rapport_financier_{data['company_name'].replace(' ', '_')}_{datetime.now().strftime('%Y%m%d')}.pdf",
            mimetype='application/pdf'
        )
    except Exception as e:
        return jsonify({'error': str(e)}), 500
def _draw_footer(canvas, doc, data):
    """Draw footer on each page"""
    canvas.saveState()
    canvas.setFont('Helvetica', 9)
    canvas.drawString(inch, 0.75 * inch, "Document confidentiel - À usage exclusif")
    canvas.drawRightString(doc.width + doc.leftMargin, 0.75 * inch, f"Page {doc.page}")
    canvas.restoreState()

if __name__ == '__main__':
    app.run(debug=True)