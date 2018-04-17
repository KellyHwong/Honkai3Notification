# python2
from gi.repository import Gdk
import time

import smtplib

window = Gdk.get_default_root_window()
x, y, width, height = window.get_geometry()

print("The size of the root window is {} x {}".format(width, height))

# keep capturing the screen, and do image match
# while True:
#     pass
pb = Gdk.pixbuf_get_from_window(window, x, y, width, height)

resized = imutils.resize(gray, width = int(gray.shape[1] * scale))
        r = gray.shape[1] / float(resized.shape[1])

# send email when matching success

def send_email():
    FROM = 'xxx@gmail.com'
    TO  = 'xxx@gmail.com'

    username = 'xxx@gmail.com'
    password = 'xxx'
    server = smtplib.SMTP('smtp.gmail.com:587')

    message = "\r\n".join([
      "From: xxx@gmail.com",
      "To: xxx@gmail.com",
      "Subject: Honkai3 Notification",
      "",
      "Your friend has logged in the game! ^_^"
      ])

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(FROM, TO, message)
    server.close()
    print 'successfully sent the mail'
