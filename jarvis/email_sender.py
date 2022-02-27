import smtplib
import smtplib, ssl

def sendmail(subject,content,reciever_email):
    try:
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"
        sender_email = "anasna6005@gmail.com"  # Enter your address
        receiver_email = reciever_email  # Enter receiver address
        password = "Kl08@x555"
        message = f"""\
        Subject: {subject}

        {content}."""

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
    except:
        print("Email could not be send")
