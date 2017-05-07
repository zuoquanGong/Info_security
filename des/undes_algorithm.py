# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 16:39:58 2017

@author: fff
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 21:54:12 2017

@author: zuoquan gong
"""
#==============================================================================
# 数据载入：ip,ip-1,s1~s8,p,pc_1,pc_2,lsi
#==============================================================================
ip=[58, 50, 42, 34, 26, 18, 10, 2,
60, 52, 44, 36, 28, 20, 12, 4,
62, 54, 46, 38, 30, 22, 14, 6,
64, 56, 48, 40, 32, 24, 16, 8,
57, 49, 41, 33, 25, 17, 9, 1,
59, 51, 43, 35, 27, 19, 11, 3,
61, 53, 45, 37, 29, 21, 13, 5,
63, 55, 47, 39, 31, 23, 15, 7,]
ipinv=[40, 8, 48, 16, 56, 24, 64, 32,
39, 7, 47, 15, 55, 23, 63, 31,
38, 6, 46, 14, 54, 22, 62, 30,
37, 5, 45, 13, 53, 21, 61, 29,
36, 4, 44, 12, 52, 20, 60, 28,
35, 3, 43, 11, 51, 19, 59, 27,
34, 2, 42, 10, 50, 18, 58, 26,
33, 1, 41, 9, 49, 17, 57, 25]
ex=[32,1,2,3,4,5,4,5,6,7,8,9,8,9,10,11,
12,13,12,13,14,15,16,17,16,17,18,19,20,21,20,21,
22,23,24,25,24,25,26,27,28,29,28,29,30,31,32,1,]
s1=[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13,]
s2=[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9,]
s3=[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12,]
s4=[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14,]
s5=[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3,]
s6=[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13,]
s7=[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12,]
s8=[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
p=[16,7,20,21,29,12,28,17,1,15,23,26,5,18,31,10,
2,8,24,14,32,27,3,9,19,13,30,6,22,11,4,25,]
pc_1=[57, 49, 41, 33, 25, 17, 9,
1, 58, 50, 42, 34, 26, 18,
10, 2, 59, 51, 43, 35, 27,
19, 11, 3, 60, 52, 44, 36,
63, 55, 47, 39, 31, 23, 15,
7, 62, 54, 46, 38, 30, 22,
14, 6, 61, 53, 45, 37, 29,
21, 13, 5, 28, 20, 12, 4]
pc_2=[14, 17, 11, 24, 1, 5,
3, 28, 15, 6, 21, 10,
23, 19,12, 4, 26, 8,
16, 7, 27,20, 13, 2,
41, 52, 31, 37,47, 55,
30, 40, 51, 45, 33,48,
44, 49, 39, 56, 34, 53,
46, 42, 50, 36, 29, 32]
lsi=[1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]
s=[s1,s2,s3,s4,s5,s6,s7,s8]
#==============================================================================
# des-algorithm
#==============================================================================
def encode(s):
    return ''.join([bin(ord(c)).replace('0b', '') for c in s])
def decode(s):
    return ''.join([chr(i) for i in [int(b, 2) for b in s.split(' ')]])
def bin2dec(declist):
    s=0
    for i in range(len(declist)):
        s+=declist[::-1][i]*(2**i)
    return s
def dec2bin(dec):
    l=[]
    map(l.append,list(bin(dec)[2:]))
    return l
def replace(origin,replacetable):
    #print replacetable
    #print len(origin)
    return [origin[x] for x in replacetable]

def key_replace(key):
    return [key[x] for x in [i-1 for i in pc_1[:28]]],[key[x] for x in [i-1 for i in pc_1[28:]]] 

def xor(part,key):
    result=[]
    for i in range(len(part)):
        if part[i]==key[i]:
            result.append(0)
        else:
            result.append(1)
    return result
def s_convert(six,s):
    row=bin2dec([six[0],six[5]])
    column=bin2dec(six[1:5])
    #print row,column
    result=dec2bin(s[row*16+column])
    if len(result)<4:
        for x in range(4-len(result)):
            result.insert(0,0)
    return result
def str2bin(text):
    bincode=''
    for x in text:
        bincode+=x
    bintable=[]
    for x in bincode:
        bintable.append(int(x))
    return bintable
def key_op(c0,d0,i):
    if lsi[i]==1:
        return c0[1:]+c0[:1],d0[1:]+d0[:1]
    else:
        return c0[2:]+c0[:2],d0[2:]+d0[:2]

def text_op(lpart,rpart,i):
    nextlpart=rpart
    rpart=replace(rpart,[x-1 for x in ex])
    rpart=xor(rpart,key[i])
    l=[]
    for a in range(8):
        l+=s_convert(rpart[(a*6):(a*6+6)],s[a])
    l=map(int,l)
    #print l
    #print type(rpart[0])
    rpart=replace(l,[x-1 for x in p])
    #print type(rpart[0])
    rpart=xor(rpart,lpart)
    return nextlpart,rpart

fin=open('data/ciphertext.txt','r')
#fin=open('data/cluster.pkl','rb')
text=[]
for x in fin.readline():
    text.append(x)
#print text
fin.close()
fkey=open('data/key.txt','rb')
key=[]
while True:
    c=fkey.read(1)
    if len(c)==0:
        break
    key.append(encode(c))
    #print encode(c)
key=str2bin(key)[:64]
c0,d0=key_replace(key)
key=[]
for i in range(16):
    c0,d0=key_op(c0,d0,i)
    key.append(replace(c0+d0,[i-1 for i in pc_2]))

key=key[::-1]
#print key
'''for k in key:
    print len(k)'''
bindepart=[]
unit=[]
for x in str2bin(text):
    unit.append(x)
    if len(unit)==64:
        bindepart.append(unit)
        unit=[]
#print unit
#unit中保留多余部分


for i,part in enumerate(bindepart):
    part=replace(part,[x-1 for x in ipinv])
    lpart=part[:32]
    rpart=part[32:]
    for a in range(16):
        lpart,rpart=text_op(lpart,rpart,a)
    bindepart[i]=replace(rpart+lpart,[x-1 for x in ip])
    
ciphertext=[]
for part in bindepart:
    ciphertext+=part
ciphertext+=unit
#print len(ciphertext)
fo=open('data/cleartext.txt','w')
for x in ciphertext:
    fo.write(str(x))
fo.close()

