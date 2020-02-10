# Contoh list dalam function

# def hello():
#     print('Hello')

# def function():
#     return [1,2,hello]

# function()[2]()

# Print tidak memiliki value karena langsung execute print
# Return menghasilkan sebuah value di mana value tersebut dapat diambil atau dipanggil kapanpun

# Important from list
# Cara ambil dari sebuah list, cara mengganti list, setelah diganti lalu diambil dalam sebuah list

# Matriks dua dimensi
# produk = [ 
#     ['Jeruk', 2000],
#     ['Apel', 3000],
#     ['Pear', 4000],
#     ['Cilok', 5000]
# ]
# print(produk[0][0],produk[2][1])

# cart=[
#     [0,3],
#     [1,4],
#     [2,5],
#     [3,6]
# ]

# # Proses pemanggilan produk untuk dikalikan dengan cart
# out=''
# for i in range(len(produk)):
#     out += str(i+1) + '. ' + produk[i][0] + ' Rp' + str(produk[i][1]) + ' x ' + str(cart[i][1]) + ' = Rp' + str(produk[i][1]*cart[i][1])+'\n'
# print(out)

# Dictionary
# nama = {
#     'depan' : 'Farah',
#     'belakang' : 'Amalia'
# }

# # print(nama['depan'])
# # print(nama['belakang'])

# nama['depan']='Antonio'
# print(nama['depan'],nama['belakang'])

# variable_tuple=(1,2,3,4,5,6,7,8,9)
# print(variable_tuple[1])
# acakadut=('Farah',[1,True],{'Antonio':'Mancing'})
# acakadut[1].append('Bebek goreng')
# acakadut[2]['Frederico']='Kobam'
# acakadut[2]['Roberto']='Wedokan'
# acakadut[2]['Paulo']='Tidur'
# print(acakadut)

# Set
# beset={'antonio','frederico','roberto','paulo','paulo','roberto'}
# print(beset)
# beset.add('rosalinda')
# beset.add('belinda')
# beset.add('pedro')
# print(beset)

# List comprehension
# list_num=[1,2,3,4,5]
# print(list_num)
# list_num=[item*2 for item in list_num]
# print(list_num)

# def perkalian(num):
#     return num*2

# list_num=[perkalian(item) for item in list_num]
# print(list_num)

# Lambda
# num_2=lambda num : num*2
# x=[1,2,3,4,5]
# y=list(range(len(x)))
# for i in range(len(x)):
#     y[i]=num_2(x[i])
# print(y)

def dikali(n):
    return lambda a : a * n

dikali2 = dikali(2)
dikali3 = dikali(3)

print(dikali2(11))
print(dikali3(11))