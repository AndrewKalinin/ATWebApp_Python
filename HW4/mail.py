import smtplib
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

fromaddr = 'ak89037234894@bk.ru'
toaddr = 'ak89037234894@bk.ru'
mypass = 'Andryuha81'
reportname = "report.html"

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Отчет"
text = "Hello"

msg.attach(MIMEText(text))

with open(reportname, "r") as f:
	part = MIMEApplication(f.read(), Name=basename(reportname))
	part['Content-Disposition'] = 'attachment; filename="%s"' % basename(reportname)
	msg.attach(part)

body = "Тестовое сообщение"
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
server.login(fromaddr, mypass)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
