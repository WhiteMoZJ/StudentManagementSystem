import asc
import random
import math

#生成密钥串（使用RSA加密）
def Key():
    p = random.randint(1, 999)
    q = random.randint(1,999)
    N = p * q
    L = math.lcm((p-1),(q-1))
    for i in range(2,L):
        if math.gcd(i,L) == 1:
            E = i
            break
    for j in range(2,L):
        if (E*j)%L == 1:
            D = j
            break
    return E,D,N

#加密密码字符（密钥串，密码字符）
def Encrypt(E,D,N,a):
    b = asc.len(a) #字符串长度，用作循环
    n = [] #加密前的字符串转ASCII
    ecp = [] #加密后的ASCII组成的列表
    key = [E,D,N] #密钥串
    for i in range(b):
        num = asc.str2asc(i,a)
        n.append(num)
        ecp.append((n[i]**key[1])%key[3])
    ecpwd = (ecp,key)
    #输出格式[加密后的整数列表]+[密钥串]
    print(ecpwd)

a = str(input())
E,D,N = Key()
Encrypt(E,D,N,a)