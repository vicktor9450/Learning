import poplib
import smtplib
from email import parser
import ipgetter
from subprocess import check_output

to_send = 0
IP = 0
sendee = 0
ethip = 0


def send_ip(user, pwd, recipient, subject, body):
    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print 'successfully sent the mail'
    except:
        print "failed to send mail"

pop_conn = poplib.POP3_SSL('pop.gmail.com')
pop_conn.user('YOUR_EMAIL_ADDRESS@gmail.com')
pop_conn.pass_('YOUR_PASSWORD')
#  Get messages from server:
messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]
# Concat message pieces:
messages = ["\n".join(mssg[1]) for mssg in messages]
#  Parse message into an email object:
messages = [parser.Parser().parsestr(mssg) for mssg in messages]
for message in messages:
    if message['subject'] == 'IP' or message['subject'] == 'Ip' or message['subject'] == 'ip' or \
                    message['subject'] == 'IP ' or message['subject'] == 'Ip ' or message['subject'] == 'ip ':
        print "passed"
        sender = (message['From'])
        sendee = sender.split("<")[-1].split(">")[0]
        print sendee
        IP = ipgetter.myip()
        print(IP)
        ethip = check_output(['hostname', '-I'])
        print ethip
        to_send = 1
    else:
        print "failed"
pop_conn.quit()
if to_send == 1:
    send_ip('YOUR_EMAIL_ADDRESS@gmail.com', 'YOUR_PASSWORD', sendee, IP, 'Internet IP is: '
                                            ''+IP+'\n'+'Web Server is: '+IP+':8080'+'\n'+'Local IP is '+ethip)
    to_send = 0