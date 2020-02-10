# menu=input('Pilih menu yang anda inginkan: \n 1. Belanja \n 2. Belajar \n 3. Exit \n Pilih menu: ')
# if(menu.isdigit()==True):
#     if(int(menu)>0 and int(menu)<=3) : 
#         check=True
#     else :
#         print('Input salah, masukkan pilihan 1-3')
# else :
#     print('Input salah, masukkan pilihan 1-3')
    
# angka = 0
# while angka <= 10 :
#     print(angka)
#     angka += 1

# # range(start,stop,step)
# list_item = list(range(1,10,2))
# print(list_item)

# list_item = [1,2,3,4,5,6,7,8,9]
# print(list_item[6])

# list_makanan = ['ayam','tahu','tempe']
# for item in list_makanan : 
#     print(item)

# for item in list(range(2,10,2)):
#     print(item)

# for i in range(1,11) : 
#     print('Nomor urut '+str(i))
#     i+=1

z=''
for i in range (5) :
    for j in range(5) :
        z+=' * '
    z+='\n'
print(z)