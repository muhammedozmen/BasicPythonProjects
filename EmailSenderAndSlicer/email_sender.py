from email.message import EmailMessage
import ssl
import smtplib

# fill up this section
email_sender = 'change this'
email_password = 'change this'

# fill up this section
email_receiver = 'change this'

subject = "I tried something"
body = """
Really, Im trying sometging dude
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)


context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())