try:
        import sys
        import base64
        import os
except ModuleNotFoundError:
        print("eksik modul yükleniyor")
        os.system("pip3 install base64")
        os.system("pip install base64")
        os.system("clear")
        print("Lütfen tekrar deneyin")
        usage()
def çık():
	print("çıkılıyor")
	sys.exit()
def usage():
	print("""
	 _                     _    _  _
	| |__   __ _ ___  ___ / /_ | || |
	| '_ \ / _` / __|/ _ \ '_ \| || |_
	| |_) | (_| \__ \  __/ (_) |__   _|
	|_.__/ \__,_|___/\___|\___/   |_|

         """)


	print(f'{sys.argv[0]} -e or --encode <"encode"> >>>> şifreler')
	print(f'{sys.argv[0]} -d or --decode <"decode"> >>>> şifreyi çözer')
	print(f"{sys.argv[0]} -fe or --fileencode <encode.txt> >>>> dosyadaki karakteri şifreler")
	print(f"{sys.argv[0]} -fd or --filedecode <decode.txt> >>>> dosyadaki şifreyi çözer")
	sys.exit(1)

if len(sys.argv) <3:
	usage()
	sys.argv(1)

elif sys.argv[1] in ["-e","--encode"]:
	karakter = sys.argv[2]
	çevir = karakter.encode("utf-8")
	göster = base64.b64encode(çevir)
	string = göster.decode("utf-8")	
	print(string)

elif sys.argv[1] in ["-d","--decode"]:
        karakter1 = base64.b64decode(sys.argv[2])
        print(karakter1.decode("utf-8"))

elif sys.argv[1] in ["-fe","--fileencode"]:
	try:
		dosya = open(sys.argv[2])
		aç = dosya.readlines()
		for oku in aç:
			karakter = oku.encode("utf-8")
			göster = base64.b64encode(karakter)
			string = göster.decode("utf-8")
			print(string)
	except FileNotFoundError:
		print("böyle bir dosya yok")
elif sys.argv[1] in ["-fd","--filedecode"]:
	try:
		dosya = open(sys.argv[2])
		aç = dosya.readlines()
		for oku in aç:
			karakter = base64.b64decode(oku)
			print(karakter.decode("utf-8"))
	except FileNotFoundError:
		print("böyle bir dosya yok")

else:
	print(f"Girdiğiniz panametre ({sys.argv[1]}) anlaşılmadı")
	usage()
	çık()

