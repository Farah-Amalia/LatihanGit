x={
    'nama' : 'antonio',
    'umur' : 17,
    'hobi' : 'memasak',
    'makafa' : 'bakso goreng'
}

# for i,j in x.items():
#     space=10-len(i)
#     print(i,space*' ',j)

for i in range(len(x)):
    print(x[i])

# def lima():
#     return 5

# a = lambda x : x * lima()

# print(a(10))

# def add(n):
#     return n + n
# numbers = (1,2,3,4)
# result = map(add,numbers)
# print(list(result))

# def duplicate_map(function,iteration):
#     tempat=list(range(len(iteration)))
#     for i in range(len(iteration)):
#         tempat[i]=function(iteration[i])
#     return tempat

# def fungsiku(angka):
#     return angka * 5

# listku=['farah','fajrina','amalia',['farah','fajrina','amalia']]

# print(list(duplicate_map(list, listku)))
# print(list(map(list, listku)))

# def duplicate_map(function,iteration):
#     tempat=[]
#     for i in iteration:
#         tempat.append(function(i))
#     return tempat

# def fungsiku(angka1,angka2):
#     return angka1 * angka2

# list1=[1,2,3,4,5]
# list2=[1,2,3,4,5]

# listku=(list1,list2)
# print(listku)
# print(list(duplicate_map(fungsiku, listku)))

# tahun = list(range(1995,2021))
# tahun_kabisat = filter(lambda tahun : tahun % 4 == 0, tahun)
# print(list(tahun_kabisat))

# def duplicate_filter(function, iteration):
#     tempat=[]
#     for i in iteration:
#         if function(i):
#             tempat.append(i)
#     return tempat

# tahun_kabisat = duplicate_filter(lambda tahun : tahun % 4 == 0, tahun)
# print(list(tahun_kabisat))