
from simplegmail import Gmail

gmail = Gmail() 
sender_email = ""
def send_email(recipient, subject, message):
    message = message.replace("\n", "<br>")
    params = {
        "to": recipient,
        "sender": #Enter your Gmail address,
        "subject": subject,
        "msg_html": message,
    }

    message = gmail.send_message(**params) 
    
    print("Message sent successfully")

