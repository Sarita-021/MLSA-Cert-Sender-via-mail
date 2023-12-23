import smtplib
from email.message import EmailMessage
import csv

htmltemplatepath = "Data/mailtemplate.html"

def get_participants(f):
    data = [] 
    with open(f, mode="r", encoding='iso-8859-1') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    return data

def gethtmltemplate(htmltemplatepath=htmltemplatepath):
    return open(htmltemplatepath, "r").read()

def getmail(name, event, ambassador):
    sub = f"Certificate of Participation in {event}"
    html = gethtmltemplate(htmltemplatepath)
    body = html.format(name=name, event=event, ambassador=ambassador)
    return sub, body

def send_mail(list_participate, hostEmailId, event_Name, password, host_Name):
    for index, participate in enumerate(list_participate):
        name = participate["Name"]
        pemail = participate["Email"]
        filepath = ["{}.pdf".format(name)]
        sub, body = getmail(name, event_Name, host_Name)
        
        msg = EmailMessage()
        msg['Subject'] = sub
        msg['From'] = hostEmailId
        msg['To'] = pemail
        msg.set_content('This is a plain text email')
        msg.add_alternative(body, subtype='html')

        for file in filepath:
            with open("Data/Pdf/{}".format(file), 'rb') as f:
                file_data = f.read()
                file_name = "{}.pdf".format(name)

            msg.add_attachment (file_data, maintype='application', subtype='octet-stream', filename=file_name)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(hostEmailId, password)
            smtp.send_message(msg)
        
        print("Mail Send to {}".format(name))

# get participants path
participate_file = "Data/data.csv"

# get participants
list_participate = get_participants(participate_file)

# Enter your GmailId here 
hostEmailId = "hostgmail@gmail.com"

# Enter your name here [Ambassador Name]
host_Name = "Your Name"

#Enter your GmailId password here
password= "Your GmailId Password"

#Enter event name
event_Name = "Your Event Name"

#Send Mail
send_mail(list_participate, hostEmailId, event_Name ,password, host_Name)
