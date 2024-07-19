from termcolor import colored
import hashlib

def tryOpen(wordlist):
    try:
        pass_file = open(wordlist, "r")
        return pass_file
    except FileNotFoundError:
        print("[!!] No Such File At That Path!")
        quit()

def main():
    pass_hash = input("[*] Enter MD5 Hash Value: ")
    wordlist = input("[*] Enter Path To The Password File: ")

    pass_file = tryOpen(wordlist)

    for word in pass_file:
        print(colored("[-] Trying: " + word.strip("\n"), 'red'))
        enc_wrd = word.strip("\n").encode('utf-8')
        md5digest = hashlib.md5(enc_wrd).hexdigest()
        if md5digest == pass_hash:
            print(colored("[+] Password Found: " + word.strip("\n"), 'green'))
            exit(0)
    
    print("[!!] Password Not In List!")
    pass_file.close()

if __name__ == '__main__':
    main()
