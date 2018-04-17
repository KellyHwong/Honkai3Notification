# python2
# from gi.repository import Gdk
import time
from PIL import Image
import smtplib
import cv2
# import imutils
import numpy
import os

# Global configs
MIN_MATCH_COUNT = 10

def image_match(img1,img2,MIN_MATCH_COUNT):
#     img1 = online#cv2.imread('box.png',0)          # queryImage
#     img2 = emiya#cv2.imread('box_in_scene.png',0) # trainImage

    # Initiate SIFT detector
    # sift = cv2.SIFT()
    sift = cv2.xfeatures2d.SIFT_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = sift.detectAndCompute(img1,None)
    kp2, des2 = sift.detectAndCompute(img2,None)

    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks = 50)

    flann = cv2.FlannBasedMatcher(index_params, search_params)

    matches = flann.knnMatch(des1,des2,k=2)

    # store all the good matches as per Lowe's ratio test.
    good = []
    for m,n in matches:
        if m.distance < 0.7*n.distance:
            good.append(m)

    if len(good) >= MIN_MATCH_COUNT:
        return True
    else:
        return False

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

# keep capturing the screen, and do image match
online = cv2.imread("images/online.png")
current_screen_file_path = "screencapture_" + "current_screen" + ".png"
pwd = os.getcwd()
while True:
    os.system("screencapture -x " + pwd +"/" + current_screen_file_path)
    current_screen = cv2.imread(current_screen_file_path)
    if image_match(online,current_screen,MIN_MATCH_COUNT):
        send_email()
        time.sleep(10)
    time.sleep(1)
