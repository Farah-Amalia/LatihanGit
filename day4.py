# a = 10
# while (a<=10):
#     print('lanjut')

# for item in range(5):
#     print(item)

#Nested loop
# for i in range(5):
#     for j in range(5):
#         print(i)
# range(j)

# for i in range(5,0,-1):
#     print(i)

#Solve it 2
# z=''
# for i in range(5,0,-1):
#     if (i>1):
#         for j in range(0,i):
#             z+=' * '
#         z+='\n'
#     elif (i==1):
#         for k in range(0,5):
#             for l in range(0,k+1):
#                 z+=' * '
#             z+='\n'
# print(z)

#Solve it 3
# z=''
# for i in range (0,10,1) :
#     for j in range (0,21) :
#         if j >= 10-i and j <= 10+i:
#             z += ' * '
#         else:
#             z += '   '
#     z += '\n'
# print(z)
# z=''
# for i in range (0,10):
#     print('   '*(10-i-1)+' * '*(i*2+1)+'   '*(10-i-1))

#Solve it 4
# z=''
# for i in range (9,-1,-1) :
#     for j in range (0,20) :
#         if j >= 10-i and j <= 10+i:
#             z += ' * '
#         else:
#             z += '   '
#     z += '\n'
# print(z)

# Solve it 5
# z=''
# for i in range (4,-5,-1):
#     print('   '*(5-abs(i)-1)+' * '*(abs(i)*2+1)+'   '*(5-abs(i)-1))
# z=''
# for i in range (0,11,) :
#     if (i<10):
#         for j in range (0,21) :
#             if j >= 10-i and j <= 10+i:
#                 z += ' * '
#             else:
#                 z += '   '
#         z += '\n'
#     else:
#         for k in range (11,-1,-1) :
#             for l in range(0,21):
#                 if l >= 10-k and l <= 10+k:
#                     z += ' * '
#                 else:
#                     z += '   '
#             z += '\n'
# print(z)

# Soal pattern size
# size=int(input('Masukkan size: '))
# z=''
# for i in range(size) :
#     for j in range(size-i-1) :
#         print(end=' ')
#     for j in range(i+1):
#         print('.',end=' ')
#     print()
    # else:
    #     for k in range(0,size) :
    #         for l in range(0,size):
    #             if l >= size-k and l <= size+k:
    #                 z += ' *'
    #             else: 
    #                 z += '  '
    #         z += '\n'
# print(z)

size=int(input('Masukkan size: '))
z=1
for i in range (0,size) :
    for j in range (0,size-i) :
        if(z<10):
            print(str(z),end='   ')
            z+=2
        elif(z<100):
            print(str(z),end='  ')
            z+=2
        else:
            print(str(z),end=' ')
            z+=2
    print(end='\n')
