# Dependancy inversion ( SOLID -> D)
# This ensures that High level(parent) class must not dependent of Low (child) level class


# It violates the single dependency ('S'OLID) as the notification is using to send email.Notification must serve a single task
class EmailService:
    def send(self, message):
        print(f"Sending email: {message}")


class Notification:
    def __init__(self):
        self.service = EmailService()

    def notify(self, message):
        self.service.send(message)
        

# so the correct code is 
class NotificationService:
    def send(self, message):
        pass

class EmailService(NotificationService):
    def send(self, message):
        print(f"Sending email: {message}")

class Notification:
    def __init__(self, service: NotificationService):
        self.service = service
    
    def notify(self, message):
        self.service.send(message)

# Usage
email_service = EmailService()
notification = Notification(email_service)
notification.notify("Hello!")
        
        