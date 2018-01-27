'''
Created on 27 ene. 2018

@author: jorge
'''

if __name__ == '__main__':
    pass

def isprimo(n):
    print("Primos del 1 al 1000")
    for i in range(n):
        if (i>1):
            encontrado=False
            for j in range(i):
                if (j>1):
                    if(i%j==0):
                        encontrado=True
            if (encontrado==False): print(i)  
            

num=1000
primo=isprimo(num)
