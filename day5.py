# out=''
# for i in range(3):
#     for j in range(3):
#         out += str(j)+' '
#     out += '\n'
# print(out)

def pertambahan(x,y):
    total=x+y
    return total
print(pertambahan(7,5))

def lima():
    return 5

def kali(x):
    if(x<3):
        return 1
    else:
        return(x*lima())

print(kali(5))
