from backend.email_generation import generate_email

def test_email_generation():
    research_report = {
        "name": "John Doe",
        "company": "Example Corp",
        "details": "CEO, tech enthusiast"
    }
    product_catalog = "Our product helps automate sales tasks efficiently."
    
    email = generate_email(research_report, product_catalog)
    
    assert isinstance(email, str), "Email generation failed"
    assert len(email) > 0, "Email content is empty"
