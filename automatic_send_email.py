import smtplib
import ssl

# function that send emails


def send_email(message):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"  # server
    sender_email = "sender@gmail.com"
    receiver_email = "receiver@gmail.com"
    password = "sender_password"

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        try:
            server.login(sender_email, password)
            res = server.sendmail(sender_email, receiver_email, message)
            print('email sent!')
        except:
            print("could not login or send the mail.")


# calling the fundtion
send_email("Hello just trying my automated email code...")
