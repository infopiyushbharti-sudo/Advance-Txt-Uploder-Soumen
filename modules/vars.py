#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "22282574"))
API_HASH = environ.get("API_HASH", "06ab0aa02164cfb2d71c3e7223afab1e")
BOT_TOKEN = environ.get("BOT_TOKEN", "8384555145:AAF1zy3z_QkRCLQv7RuP5pxTb8thcsX3Nhc")

OWNER = int(environ.get("OWNER", "1278128855"))
CREDIT = environ.get("CREDIT", "𝘽𝙊𝙏𝙎")
cookies_file_path = os.getenv("cookies_file_path", "youtube_cookies.txt")

TOTAL_USER = os.environ.get('TOTAL_USERS', '8222519141').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '5680454765').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))



