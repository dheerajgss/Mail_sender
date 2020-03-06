import smtplib as simple

session = simple.SMTP('smtp.gmail.com', 587)
session.starttls()
session.login("sender_emailid", "sender_password")
message = "Message to be sent"
session.sendmail("sender_emailid", "receiver_emailid", message)
session.quit()

""" Here sender_emailid, sender_password, receiver_emailid, message are to be filled as per requirements """
