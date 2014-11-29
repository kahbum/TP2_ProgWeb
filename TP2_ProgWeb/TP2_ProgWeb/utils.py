import smtplib
def sendPassword(email, password):
    SMTP_SERVER = 'smtp.gmail.com'
    SMTP_PORT = 587

    admin_sender = 'tp2.progweb@gmail.com'
    admin_password = 'fib12358'
    recipient = email
    subject = 'Primeiro acesso: senha inicial'
    body = 'Para acessar o sistema utilize os seguintes dados:<br/>'
    body += 'email: ' + email + '<br/>'
    body += 'senha: ' + password + '<br/>'

    body = "" + body + ""

    headers = ["From: " + admin_sender,
               "Subject: " + subject,
               "To: " + recipient,
               "MIME-Version: 1.0",
               "Content-Type: text/html"]
    headers = "\r\n".join(headers)

    msg = headers + "\r\n\r\n" + body

    session = smtplib.SMTP(SMTP_SERVER + ':' + repr(SMTP_PORT))

    session.ehlo()
    session.starttls()
    session.ehlo
    session.login(admin_sender, admin_password)

    session.sendmail(admin_sender, recipient, msg)
    session.quit()