# Decision['testing'][2][1]('Hello',3)[2][1]()(True)
# def function(a,b):
#     return {'Ada apa' : [1,[1,[]],3]}
# Decision={'testing' : [1,3,[1,[1,function('Hello',3)]]]}
# Decision={'testing' : ['Hai','Halo',['Satu',['One',{'Ada apa':['Ya',['Ayam', 'Bebek']]}]]]}
# print(Decision['testing'][2][1][1]['Ada apa'][1][0])

# from math import floor, pow, sqrt, ceil

# a=[1,42,2,4,1,2,4,23,23,5,1,2,4,2,53,2,1,4,23,5,1,2,4,2,3,9,7,5,35,4,2,3]

# def bubble_sort(data):
#     for i in range(len(data), 0, -1) : 
#         for j in range(0,i-1) : 
#             if (data[j] > data[j+1]) : 
#                 data[j], data[j+1] = data[j+1], data[j]
#     return data

# def get_mean(data):
#     return round(sum(data)/len(data),3)

# def get_median(data):
#     data=bubble_sort(data)
#     median = 0
#     if len(data) % 2 != 0 : 
#         median = data[(len(data) // 2)]
#     else : 
#         median = (data[(int(len(data) / 2)) - 1] + data[int(len(data) / 2)]) / 2
#     return median

# def get_mode(data):
#     ind=set(data)
#     counter = {}
#     modus = []
#     for i in ind:
#         z = 0
#         for j in data:
#             if i==j:
#                 z += 1
#         counter[i] = z
#     max_count = max(counter.values())
#     for k in counter:
#         if counter[k]==max_count:
#             modus.append(k)
#     if len(modus)==len(ind):
#         modus='None'
#     if len(modus)==1:
#         modus=modus[0]
#     return modus

# def get_variance(data):
#     sum=0
#     for i in data:
#         sum+=((i-get_mean(data))**2)
#     return round(sum/(len(data)-1),3)

# def get_stdev(data):
#     return round(sqrt(get_variance(data)),3)

# def sample_statistic(data,type='mean'):
#     if type == 'mean':
#         return get_mean(data)
#     elif type == 'median':
#         return get_median(data)
#     elif type == 'mode':
#         return get_mode(data)
#     elif type == 'variance':
#         return get_variance(data)
#     elif type == 'stdev':
#         return get_stdev(data)
#     else:
#         print('Input tidak sesuai')

# list=['mean','median','mode','variance','stdev']
# for i in list:
#     space=10-len(i)
#     print(i.capitalize()+space*' '+': '+str(sample_statistic(a,i)))


#coba
# def get_square(angka):
#     angka=str(angka)
#     hasil=''
#     for i in angka:
#         hasil+=str(int(i)**2)
#     return hasil

# print(get_square(242))

# website

def domain_name(input):
    list_domain = input.split('.')
    if len(list_domain)==3:
        print(list_domain[1])
    elif len(list_domain)==2:
        print(list_domain[0].split('//')[1])

domain_name('http://www.zombie-bites.com/apapun')