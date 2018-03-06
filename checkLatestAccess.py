import smtplib

def validate_ip(s):
    a = s.split('.')
    if len(a) != 4:
        return False
    for x in a:
        if not x.isdigit():
            return False
        i = int(x)
        if i < 0 or i > 255:
            return False
    return True

def sndMail(mssg):
    import smtplib

    gmail_user = "xxxxxxxxxxx@gmail.com"
    gmail_password = "xxxxxxxxxxxxxxxxx"

    fromAddr = gmail_user
    toAddr = "xxxxxxxxxxxxx@gmail.com"
    subject = "Apache server new alert !"
    body = mssg

    email_text = """\  
    From: %s  
    To: %s  
    Subject: %s

    %s
    """ % (fromAddr, toAddr, subject, body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(fromAddr, toAddr, email_text)
        server.close()

        print ("Email sent!")
    except:
        print ("Something went wrong...")

infile = "/var/log/apache2/access.log"
newMsg = ""

while True:
    with open(infile) as myfile:
        lstLine = list(myfile)[-1]
        ip = (lstLine.split(" ")[0])

        if(validate_ip(ip)):
            tmp = lstLine.split(" ")[3]
            tmp = tmp.split(":")[0] + ":" + tmp.split(":")[1] + ":" + tmp.split(":")[2]
            msg = ip + " Time : " + tmp + "]"
            if ( msg != newMsg ):
                sndMail(msg)
            newMsg = msg