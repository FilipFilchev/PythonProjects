import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
sender_email = "your_email@gmail.com"
receiver_email = "recipient_email@example.com"
subject = "Hello people!"
message = "This is a test email sent from Python."

# SMTP server configuration (Gmail in this example)
smtp_server = "smtp.gmail.com"
smtp_port = 587
username = "your_email@gmail.com"
password = "your_password"

# Create a multipart message
msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = subject

# Attach the message to the MIMEMultipart object
msg.attach(MIMEText(message, "plain"))

try:
    # Create a secure connection with the SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()

    # Login to the email account
    server.login(username, password)

    # Send the email
    server.sendmail(sender_email, receiver_email, msg.as_string())
    print("Email sent successfully!")
except Exception as e:
    print("An error occurred while sending the email:", str(e))
finally:
    # Terminate the SMTP session
    server.quit()
