"""
Test script to verify PDF generation functionality
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app, generate_report
import json

def test_pdf_generation():
    """Test PDF generation"""
    with app.test_client() as client:
        # Test the main route
        response = client.get('/')
        if response.status_code == 200:
            print("Main page test PASSED")
        else:
            print("Main page test FAILED")
            return False
            
        # Test PDF generation
        response = client.post('/generate-report', 
                             data=json.dumps({}),
                             content_type='application/json')
        
        # Check if response is successful
        if response.status_code == 200 and response.content_type == 'application/pdf':
            print("PDF generation test PASSED")
            # Save the PDF to disk for verification
            with open('test_report.pdf', 'wb') as f:
                f.write(response.data)
            print("PDF saved as test_report.pdf")
            return True
        else:
            print("PDF generation test FAILED")
            print(f"Status code: {response.status_code}")
            print(f"Content type: {response.content_type}")
            return False
if __name__ == "__main__":
    test_pdf_generation()