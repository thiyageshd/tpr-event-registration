class CommunicationService:
    def send_sms(self, phone_number, message):
        # Implement SMS sending logic
        print(f"Sending SMS to {phone_number}: {message}")

    def send_whatsapp(self, phone_number, message):
        # Implement WhatsApp sending logic
        print(f"Sending WhatsApp to {phone_number}: {message}")

    def send_email(self, email, subject, body):
        # Implement email sending logic
        print(f"Sending email to {email}: Subject - {subject}, Body - {body}")