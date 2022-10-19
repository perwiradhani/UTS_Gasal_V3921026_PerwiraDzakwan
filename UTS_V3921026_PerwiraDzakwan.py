# CAESAR CIPHER
def encrypt_caesar(text,shift):
    encryption = ("")
    for x in text:
        if x.isupper(): #cek apakah huruf kapital
        # mencari posisi karakter
            char_unicode = ord(x)
            char_index = char_unicode - ord("A")
        # melakukan pergeseran
            new_index = (char_index + shift) % 26
        # konversi ke karakter baru
            new_unicode = new_index + ord("A")
            new_character = chr(new_unicode)
        # menambahkan ke string yang sudah dienkripsi
            encryption = encryption + new_character
        else:
        # karena karakter bukan huruf kapital, biarkan saja
            encryption += x
        
    print("Plain text : ",text)
    print("Ciphertext : ",encryption)


def decrypt_caesar(text,shift):
    decryption = ("")
    for x in text:
        if x.isupper():  #cek apakah huruf kapital
        # menemukan posisi dari karakter
            char_unicode = ord(x)
            char_index = char_unicode - ord("A")
        # melakukan pergeseran
            new_index = (char_index - shift) % 26
        # konversi ke karakter baru
            new_unicode = new_index + ord("A")
            new_character = chr(new_unicode)
        # menambahkan ke string yang sudah didekripsi
            decryption = decryption + new_character
        else:
        # karena karakter bukan huruf kapital, biarkan saja
            decryption += x

    print("Ciphertext: ",text)
    print("Plain Text : ",decryption)


# VIGNERE CIPHER
def generateKey(string, key): 
  key = list(key) 
  if len(string) == len(key): 
    return(key) 
  else: 
    for i in range(len(string) -len(key)): 
      key.append(key[i % len(key)]) 
  return("" . join(key)) 
  
def encrypt_vignere(string, key): 
  encrypt_text = [] 
  for i in range(len(string)): 
    x = (ord(string[i]) + ord(key[i])) % 26
    x += ord('A') 
    encrypt_text.append(chr(x)) 
  return("" . join(encrypt_text)) 

def decrypt_vignere(encrypt_text, key): 
  orig_text = [] 
  for i in range(len(encrypt_text)): 
    x = (ord(encrypt_text[i]) - ord(key[i]) + 26) % 26
    x += ord('A') 
    orig_text.append(chr(x)) 
  return("" . join(orig_text)) 

# MAIN
def main():
  print("-------------------- Caesar Cipher & Vignere Cipher --------------------")
  print("1. Enkripsi")
  print("2. Dekripsi")
  print("3. Exit")
  pilihan = int(input("Silahkan pilih menu : "))

  if pilihan == 1:
    print("-------------------- Caesar Cipher --------------------")
    text = input("Masukkan pesan : ").upper()
    shift = int(input("Masukkan kunci geser : "))
    encrypt_caesar(text,shift)
    print("-------------------- Vignere Cipher --------------------")
    string = input("Masukkan ciphertext diatas : ")
    keyword = input("Masukkan keyword : ")
    key = generateKey(string, keyword) 
    encrypt_text = encrypt_vignere(string,key)
    print("Ciphertext : ", encrypt_text)
  elif pilihan == 2:
    print("-------------------- Vignere Cipher --------------------")
    string = input("Masukkan ciphertext : ")
    keyword = input("Masukkan keyword : ")
    key = generateKey(string, keyword) 
    decrypt_text = decrypt_vignere(string, key)
    print("Plain Text : ", decrypt_text)
    print("-------------------- Caesar Cipher --------------------")
    text = input("Masukkan ciphertext diatas : ").upper()
    shift = int(input("Masukkan kunci geser : "))
    decrypt_caesar(text,shift)
  elif pilihan == 3:
    exit()
    
          
if __name__ == "__main__":
    main()