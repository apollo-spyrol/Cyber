from zipfile import ZipFile

# Function to attempt to extract the zip file with a given password
def attempt_extract(zf_handle, password):
    try:
        zf_handle.extractall(pwd=password.encode('utf-8'))
        print(f"[+] Password found: {password}")
        return True
    except:
        return False

def main():
    print("[+] Beginning bruteforce")
    with ZipFile('enc.zip') as zf:
        passwords = [
            "123456", "12345", "123456789", "password", "1234567", "rockyou", "12345678", "abc123",
            "nicole", "daniel", "monkey", "lovely", "jessica", "654321", "michael", "ashley",
            "qwerty", "111111", "iloveu", "000000", "michelle", "volleyball", "whatever",
            "dragon", "vanessa", "cookie", "naruto", "summer", "spongebob", "joseph",
            "junior", "softball", "taylor", "yellow", "daniela", "lauren", "mickey",
            "princesa", "alexandra", "alexis", "jesus", "estrella", "miguel",
            "william", "thomas", "angela", "poohbear", "patrick", "monica",
            "richard", "112233", "princess1", "555555", "diamond",
            "carolina", "steven", "rangers", "louise",
            "orange", "789456", "999999", "11111",
            "nathan", "heaven", "55555",
            "baseball", "martin",
            "greenday", "november",
            "alyssa","madison",
            "123321","123abc",
            "batman","september",
            "december","morgan",
            "mariposa","maria",
            "gabriela","SPONGEBOB",
            "sunshine","chocolate",
            'password1', 'soccer'
        ]

        for password in passwords:
            if attempt_extract(zf, password):
                break
    print("[+] Password not found in list")

if __name__ == "__main__":
    main()
