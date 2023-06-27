#SPENSER YOUNG


import os
os.system("pip install instabot")
from instabot import Bot

bot = Bot()
username = input("Enter your Username: ")
password = input("Enter your Password: ")
image = input("Enter the image name plase extention: ")
caption= input("Enter the publication descrition: ")

bot.uploand_photo(image, caption=caption)￼Enter
