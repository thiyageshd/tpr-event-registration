class CommunicationService:
    def send_sms(self, phone, message):
        # Implement SMS sending logic
        print(f"Sending SMS to {phone}: {message}")

    def send_whatsapp(self, phone, message):
        # Implement WhatsApp sending logic
        print(f"Sending WhatsApp to {phone}: {message}")

    def send_email(self, email, subject, body):
        # Implement email sending logic
        print(f"Sending email to {email}: Subject - {subject}, Body - {body}")