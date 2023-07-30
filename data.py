import datetime
import smtplib
from last import cement_,brick_,sand_,recipient_email

to=datetime.date.today()
already=[]

def firstmail(recipient_email):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "chinna@student.tce.edu"
    password = "X9ozB!63yGzX"

    # Create the email message
    subject = f"You are subscribe for the material ordering date"
    body = f"Material order date will be updated daily basics\n\nAll the information will send to this {recipient_email}"
    #recipient_email = "ashokkg@student.tce.edu"
    message = f"Subject: {subject}\n\n{body}"
    # Send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, recipient_email, message)
    print('\nEmail Sent!\n')
        

firstmail(recipient_email)

while True:
    to=datetime.date.today()
    for i in range(0,len(cement_)):
        if to==cement_[i]['Date']:
            if to not in already:
            #Set up the SMTP server
                smtp_server = "smtp.gmail.com"
                smtp_port = 587
                sender_email = "chinna@student.tce.edu"
                password = "X9ozB!63yGzX"

                # Create the email message
                subject = f"Reordering Cement for {cement_[i]['Name of the Activity']}"
                body = f"Name of the Activity: {cement_[i]['Name of the Activity']}\n\nDate:{to}\n\nUsage in Nos:{cement_[i]['Usage in Nos']}\n\nStorage in Nos: {cement_[i]['Storage in Nos']}\n\nOrdering in Nos:{cement_[i]['Ordered in Nos']}\n\nFor Vendor's Details visit this site: https://constructioncart.store/\n"
                #recipient_email = "ashokkg@student.tce.edu"
                message = f"Subject: {subject}\n\n{body}"
                # Send the email
                with smtplib.SMTP(smtp_server, smtp_port) as server:
                    server.starttls()
                    server.login(sender_email, password)
                    server.sendmail(sender_email, recipient_email, message)
    
    for i in range(0,len(sand_)):
        if to==sand_[i]['Date']:
            if to not in already:
            #Set up the SMTP server
                smtp_server = "smtp.gmail.com"
                smtp_port = 587
                sender_email = "chinna@student.tce.edu"
                password = "X9ozB!63yGzX"

                # Create the email message
                subject = f"Reordering Sand for {sand_[i]['Name of the Activity']}"
                body = f"Name of the Activity: {sand_[i]['Name of the Activity']}\n\nDate:{to}\n\nUsage in Nos:{sand_[i]['Usage in m³']}\n\nStorage in Nos: {sand_[i]['Storage in m³']}\n\nOrdering in m3: 11.32 m3 (4 unit)\n\nFor Vendor's Details visit this site: https://constructioncart.store/\n"
                recipient_email = "ashokkg@student.tce.edu"
                message = f"Subject: {subject}\n\n{body}"

                # Send the email
                with smtplib.SMTP(smtp_server, smtp_port) as server:
                    server.starttls()
                    server.login(sender_email, password)
                    server.sendmail(sender_email, recipient_email, message)
    for i in range(0,len(brick_)):
        if to==brick_[i]['Order Dates'][0]:# or (to==brick_[i]['Order Dates'][1] or to==brick_[i]['Order Dates'][2]):
            if to not in already:
            #Set up the SMTP server
                smtp_server = "smtp.gmail.com"
                smtp_port = 587
                sender_email = "chinna@student.tce.edu"
                password = "X9ozB!63yGzX"
                print(to)
                # Create the email message
                subject = f"Reordering Brick for {brick_[i]['Name of the Activity']}"
                body = f"Name of the Activity: {brick_[i]['Name of the Activity']}\n\nDate:{to}\n\nUsage in Nos:{brick_[i]['Usage in Nos']}\n\nStorage in Nos: {brick_[i]['Storage in Nos']}\n\nOrdering in No's: 4000 No's Brick\n\nFor Vendor's Details visit this site: https://constructioncart.store/\n"
                recipient_email = "ashokkg@student.tce.edu"
                message = f"Subject: {subject}\n\n{body}"

                # Send the email
                with smtplib.SMTP(smtp_server, smtp_port) as server:
                    server.starttls()
                    server.login(sender_email, password)
                    server.sendmail(sender_email, recipient_email, message)

    already.append(to)


#print(sand_[0]["Date"])
# brick_=[{'Name of the Activity': 'Ground_Floor_Lintel_Level_BrickWork', 'Usage in Nos': 9228, 'Storage in Nos': 3559, 'Order Dates': [datetime.date(2023, 4, 29), datetime.date(2023, 4, 19), datetime.date(2023, 4, 19)]}]
# print("kjcnasnklascknlmkls")
# for i in range(0,len(brick_)):
#         if to==brick_[i]['Order Dates'][0] or (to==brick_[i]['Order Dates'][1] or to==brick_[i]['Order Dates'][2]):
#             print(brick_[0]['Order Dates'][0])
