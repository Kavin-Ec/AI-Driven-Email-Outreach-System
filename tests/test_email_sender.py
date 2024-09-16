from backend.email_sender import send_email

def test_send_email(monkeypatch):
    # Mock the smtplib.SMTP_SSL function to simulate sending email without actually sending it
    def mock_smtp_ssl(*args, **kwargs):
        class MockSMTP:
            def login(self, user, password):
                pass
            def sendmail(self, from_addr, to_addrs, msg):
                pass
            def quit(self):
                pass
        return MockSMTP()

    monkeypatch.setattr("smtplib.SMTP_SSL", mock_smtp_ssl)

    result = send_email(
        to_email="recipient@example.com",
        subject="Test Email",
        body="This is a test email.",
        gmail_user="your_gmail@gmail.com",
        gmail_password="app_password"
    )
    
    assert result is None, "Email sending failed or returned an unexpected result"
