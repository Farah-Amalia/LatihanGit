# def remove(word,char):
#     print(word.replace(char,''))

# remove('Farah','a')

# def mainsuit(pemain1,pemain2):
#     winner=''
#     check=True
#     pemain1=pemain1.lower()
#     pemain2=pemain2.lower()
#     if (pemain1=='gunting'):
#         if(pemain2=='batu'):
#             winner='2'
#         elif(pemain2=='kertas'):
#             winner='1'
#         elif(pemain2==pemain1):
#             winner=''
#         else:
#             print('INPUT SALAH')
#             check=False
#     elif (pemain1=='batu'):
#         if(pemain2=='gunting'):
#             winner='1'
#         elif(pemain2=='kertas'):
#             winner='2'
#         elif(pemain2==pemain1):
#             winner=''
#         else:
#             print('INPUT SALAH')
#             check=False
#     elif (pemain1=='kertas'):
#         if(pemain2=='gunting'):
#             winner='2'
#         elif(pemain2=='batu'):
#             winner='1'
#         elif(pemain2==pemain1):
#             winner=''
#         else:
#             print('INPUT SALAH')
#             check=False
#     else:
#         check=False
#     if check==True:
#         if(winner==''):
#             hasil1='Player 1 {0}, player 2 {1}, hasil seri!'
#             print(hasil1.format(pemain1,pemain2))
#         else:
#             hasil='Player 1 {0}, player 2 {1}, player {2} menang!'
#             print(hasil.format(pemain1,pemain2,winner))
#     else:
#         print('INPUT SALAH')

# mainsuit(input('Masukkan player 1: '),input('Masukkan player 2: '))


# def perkalian(angka1=5,angka2=10):
#     return angka1*angka2
# print(perkalian())
# print(perkalian(angka1=2))
# print(perkalian(angka2=5))
# print(perkalian(angka1=15,angka2=30))

# def perkalian(x):
#     if x<3:
#         return 4
#     else:
#         return(x*tujuh())

# def tujuh():
#     return 7

# print(perkalian(9))

# def alay_generator(word):
#     vowels=['a','i','u','e','o','A','I','U','E','O']
#     angka=['4','1','u','3','0','4','1','U','3','0']
#     for i in range(len(vowels)):
#         word=word.replace(vowels[i],angka[i])
#     print(word)

# alay_generator(input('Masukkan kalimat: '))

# def remove_vowels(word):
#     vowels=['a','i','u','e','o','A','I','U','E','O']
#     for i in vowels:
#         word=word.replace(i,'')
#     print(word)

# remove_vowels(input('Masukkan kalimat: '))

# List
# buah=['Jeruk','Apel','Semangka','Pear','Pisang']
# print(buah)
# buah[2]='Durian'
# print(buah)
# buah.append('Melon')
# print(buah)
# buah.pop(3)
# print(buah)
# buah.insert(2,'Rambutan')
# print(buah)

# list_aku=[2,'Hello',[1,5,'Hai',[9,False]]]
# print(list_aku[2][3][0])

def check_nama(name,alphabet):
    print(alphabet.lower() in name.lower())

check_nama(input('Masukkan nama: '), input('Masukkan karakter: '))