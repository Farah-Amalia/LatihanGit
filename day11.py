# Pembahasan soal

# Soal no 1
def remove_outlier(data):
    from statistics import median
    data_sorted=sorted(data)
    mid=len(data)//2
    data1=data_sorted[0:mid]
    data3=data_sorted[mid:]
    # q1=data1[len(data1)//2] if len(data1)%2 != 0 else (data1[len(data1)//2] + data1[len(data1)//2-1])/2
    # q3=data3[len(data3)//2] if len(data3)%2 != 0 else (data3[len(data3)//2] + data3[len(data3)//2-1])/2
    q1=median(data1)
    q3=median(data3)
    iqr=q3-q1
    lower_limit=q1-(1.5*iqr)
    upper_limit=q3+(1.5*iqr)
    new_data=[]
    for item in data:
        if item > lower_limit and item < upper_limit:
            new_data.append(item)
    print('Data asli = ',data)
    print('Data setelah disort = ',data_sorted)
    print('Setengah data pertama = ',data1)
    print('Setengah data kedua = ',data3)
    print('Q1 adalah =',q1)
    print('Q2 adalah = ',q3)
    print('Lower limit adalah = ',lower_limit)
    print('Upper limit adalah = ',upper_limit)
    print('Data yang tidak outlier = ',new_data)

remove_outlier([71,70,73,70,70,69,70,72,71,300,71,69])

# Soal no 2
def count_vowels(data):
    counter_vowels = 0
    vowels=['a','i','u','e','o']
    for i in data.lower():
        if i in vowels:
            counter_vowels+=1
    print('Jumlah vowels = ',counter_vowels)

count_vowels('budi pergi ke pasar')
count_vowels('purwadhika')

# Soal no 3
def given(array):
    new_list=[]
    for i in array:
        for j in i:
            new_list.append(j)
    print(array,'->',sorted(new_list))
given([[3, 2, 1], [4, 6, 5], [], [9, 7, 8]]) 
given([[3,4,2,1] , [1,2,3] , [5,4,3,1]]) 

# Soal no 4
def count_words(words):
    word_list=words.split(' ')
    count = {}
    for i in word_list:
        if (i in count.keys()):
            count[i]+=1
        else:
            count[i]=1
    for key,value in count.items():
        print(f'Jumlah kata \'{key.capitalize()}\' adalah sebanyak {value}')
count_words('jangan jangan kamu adalah aku')