from backend.email_monitoring import check_email

def test_check_email(monkeypatch):
    # Mock the imaplib.IMAP4_SSL function to simulate checking email
    def mock_imap_ssl(*args, **kwargs):
        class MockIMAP:
            def login(self, user, password):
                pass
            def select(self, folder):
                pass
            def search(self, charset, search_criteria):
                return "OK", [b'1 2 3']
        return MockIMAP()

    monkeypatch.setattr("imaplib.IMAP4_SSL", mock_imap_ssl)

    result = check_email("your_gmail@gmail.com", "app_password")
    
    assert result == [b'1 2 3'], "Email monitoring failed"
