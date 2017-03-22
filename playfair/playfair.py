# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 12:44:51 2017

@author: gong
"""
from collections import OrderedDict
import sys
#reload(sys)
#sys.setdefaultencoding('utf8')
#==============================================================================
# 文件读写与表格初始化
#==============================================================================
def check_contain_chinese(check_str):
    for ch in check_str.decode('utf-8'):
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False
    
init_table=[[chr(i)] for i in range(65,91)]
#print init_table
for u in init_table:
    if u[0]=='J':
        init_table.remove(u)
    if u[0]=='I':
        u.append('J')
#print init_table,'\n',len(init_table)

fin=open(sys.argv[1]+'.txt','r')
ctext=''.join(fin.readlines()).strip()

keyword=''.join(sys.argv[2:])   

if check_contain_chinese(keyword)==True:
    print 'keyword error'
    exit(0)
for l in ctext:
    if check_contain_chinese(l)==True:
        print 'ciphertext error'
        exit(0)
keyword=''.join(OrderedDict.fromkeys(keyword)).upper()
ctext=''.join([l.strip() for l in ctext]).upper()
print 'keyword:',keyword
print 'ctext:',ctext
fin.close()
#==============================================================================
# 进入playfair算法：(重复字母间加‘x’，结尾补充符为‘o’)
#==============================================================================
real_table=[]
'''for alpha in keyword:
    print alpha,type(alpha)'''
for alpha in keyword:
    for u in init_table:
        flag=False
        for x in u:
            if alpha==x:
                flag=True
                break
        if flag==True:
            real_table.append(u)
            break
real_table=real_table+[i for i in init_table if i not in real_table]
real_table0=[]
for x in real_table:
    if len(x)==2:
        x=[x[1]]
        real_table0.append(x)
    else:
        real_table0.append(x)
print real_table,len(real_table)
print ':',real_table0,len(real_table0)
index=[]
for i,char in enumerate(ctext[:len(ctext)-1]):
    if char==ctext[i+1]:
        index.append(i)
ctext=list(ctext)
for x in index[::-1]:
    ctext.insert(x+1,'X')
ctext=''.join(ctext)
format_table=[[real_table[i-4+a] for a in range(5)] for i,x in enumerate(real_table) if i%5==4]
format_table0=[[real_table0[i-4+a] for a in range(5)] for i,x in enumerate(real_table0) if i%5==4]

print format_table,len(format_table)
if len(ctext)%2!=0:
    ctext=ctext+'O'
print ctext
dtext=[]
for i,c in enumerate(ctext):
    unit=[]
    if i%2==1:
        unit.append(ctext[i-1])
        unit.append(c)
        dtext.append(unit)
print 'dtext:',dtext,len(dtext)
itext=[]
for u in dtext:
    dunit=[]
    #print u
    for x in u:
        unit=[]
        #print x
        for i,a in enumerate(format_table):
            for j,b in enumerate(a):
                if x==b[0]:
                   unit.append(j)
                   #print j
                   break
                if len(b)==2:
                    if x==b[1]:
                        unit.append(j)
                        #print j
                        break
            if unit!=[]:
                unit.append(i)
                #print i
                break
        #print unit
        dunit.append(unit)
    itext.append(dunit)
itext=[i[::-1] for x in itext for i in x]
#print itext
ciphertext=[]
for i,x in enumerate(itext):
    if i%2==1:
        if x[0]==itext[i-1][0]:
            ciphertext.append(format_table0[x[0]][(itext[i-1][1]+1)%5])
            ciphertext.append(format_table0[x[0]][(x[1]+1)%5])
            
        elif x[1]==itext[i-1][1]:
            ciphertext.append(format_table0[(itext[i-1][0]+1)%5][x[1]])
            ciphertext.append(format_table0[(x[0]+1)%5][x[1]])
            
        else:
            ciphertext.append(format_table0[itext[i-1][0]][x[1]])
            ciphertext.append(format_table0[x[0]][itext[i-1][1]])
            
print '***********************'

ciphertext=''.join([u for x in ciphertext for u in x])
print ciphertext
fo=open('output.txt','w')
fo.writelines(ciphertext)
fo.close()
















































