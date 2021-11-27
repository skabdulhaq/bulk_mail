import smtplib
# Don't run like this Change the below 2 lines

email = XXXXXXXX"
password = "XXXXXXX"


def email_send(from_email, password_, to_email, subject_, message):
    postman = smtplib.SMTP(host="smtp.gmail.com", port=587)
    postman.starttls()
    postman.login(user=from_email, password=password_)
    postman.sendmail(from_addr=from_email, to_addrs=to_email,
                     msg=f"Subject:{subject_}\n\n{message}")
    postman.close()


def email_list(prefix, total_students, suffix):
    # Example
    # prefix = "125009"
    # suffix = "@sastra.ac.in"
    # total_students = 250
    list_of_emails = []
    for roll in range(1, total_students+1):
        if len(str(roll)) == 1:
            roll = f"00{roll}"
        elif len(str(roll)) == 2:
            roll = f"0{roll}"
        emails_ = prefix + str(roll) + suffix
        list_of_emails.append(emails_)
    return list_of_emails


subject = "Hay batch mates check out our Telegram group"

for emails in email_list("125009", 250, "@sastra.ac.in"):
    email_send(email, password, emails, subject, f"Hi {emails} i made a Telegram group for school of mechanical "
                                                 f"students"
                                                 f"(freshers and Unofficial)\n"
                                                 f"And i Welcome you To join this Group if your interested\n"
                                                 f"this message is sent to 250 students of school of mechanical "
                                                 f"students with automated programme so,no reply!!\n"
                                                 f"wanna check out this code??\njoin telegram group!!\n"
                                                 f"Link1: https://t.me/joinchat/kbHNflrfEbYzMTQ1\n"
                                                 f"Link2: https://telegram.me/joinchat/kbHNflrfEbYzMTQ1")
