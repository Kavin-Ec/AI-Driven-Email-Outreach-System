from backend.email_review import review_email

def test_email_review():
    email_draft = "Hello John, I wanted to introduce you to our product..."
    email_templates = "Winning template examples go here."

    reviewed_email = review_email(email_draft, email_templates)
    
    assert isinstance(reviewed_email, str), "Email review failed"
    assert len(reviewed_email) > 0, "Reviewed email is empty"
