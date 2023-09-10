import sys
import base64
import os
import argparse

class Base64EncoderDecoder:
    def __init__(self):
        try:
            import base64
        except ModuleNotFoundError:
            print("eksik modul yükleniyor")
            os.system("pip3 install base64")
            os.system("pip install base64")
            os.system("clear")
            print("Lütfen tekrar deneyin")
            self.usage()
    
    def exit(self):
        print("çıkılıyor")
        sys.exit()
    
    def usage(self):
        print("""
         _                     _    _  _
        | |__   __ _ ___  ___ / /_ | || |
        | '_ \ / _` / __|/ _ \ '_ \| || |_
        | |_) | (_| \__ \  __/ (_) |__   _|
        |_.__/ \__,_|___/\___|\___/   |_|

                 """)
        
    def encode_string(self, input_string):
        karakter = input_string.encode("utf-8")
        göster = base64.b64encode(karakter)
        return göster.decode("utf-8")

    def decode_string(self, encoded_string):
        karakter1 = base64.b64decode(encoded_string)
        return karakter1.decode("utf-8")

    def encode_file(self, file_path):
        try:
            with open(file_path, 'r') as dosya:
                for oku in dosya:
                    string = self.encode_string(oku)
                    print(string)
        except FileNotFoundError:
            print("böyle bir dosya yok")

    def decode_file(self, file_path):
        try:
            with open(file_path, 'r') as dosya:
                for oku in dosya:
                    string = self.decode_string(oku)
                    print(string)
        except FileNotFoundError:
            print("böyle bir dosya yok")

    def main(self):
        parser = argparse.ArgumentParser(description="Base64 Encoder/Decoder")
        parser.add_argument('-e', '--encode', type=str, help='Encode a string')
        parser.add_argument('-d', '--decode', type=str, help='Decode a string')
        parser.add_argument('-fe', '--fileencode', type=str, help='Encode a file')
        parser.add_argument('-fd', '--filedecode', type=str, help='Decode a file')

        args = parser.parse_args()

        if args.encode:
            encoded_string = self.encode_string(args.encode)
            print(encoded_string)
        elif args.decode:
            decoded_string = self.decode_string(args.decode)
            print(decoded_string)
        elif args.fileencode:
            self.encode_file(args.fileencode)
        elif args.filedecode:
            self.decode_file(args.filedecode)
        else:
            print(f"Girdiğiniz parametre ({sys.argv[1]}) anlaşılmadı")
            self.usage()
            self.exit()

if __name__ == "__main__":
    base64_tool = Base64EncoderDecoder()
    base64_tool.main()
