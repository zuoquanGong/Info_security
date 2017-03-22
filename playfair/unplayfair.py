import sys
from collections import OrderedDict
def check_contain_chinese(check_str):
    for ch in check_str.decode('utf-8'):
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False
fin=open('output.txt','r')
ctext=''.join(fin.readlines()).strip()

init_table=[[chr(i)] for i in range(65,91)]
for u in init_table:
    if u[0]=='J':
        init_table.remove(u)
    if u[0]=='I':
        u.append('J')
keyword=''.join(sys.argv[1:])   
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
#print real_table,len(real_table)
format_table=[[real_table[i-4+a] for a in range(5)] for i,x in enumerate(real_table) if i%5==4]
print format_table,len(format_table)
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
print itext
ciphertext=[]
for i,x in enumerate(itext):
    if i%2==1:
        if x[0]==itext[i-1][0]:
            ciphertext.append(format_table[x[0]][(itext[i-1][1]-1)%5])
            ciphertext.append(format_table[x[0]][(x[1]-1)%5])
            
        elif x[1]==itext[i-1][1]:
            ciphertext.append(format_table[(itext[i-1][0]-1)%5][x[1]])
            ciphertext.append(format_table[(x[0]-1)%5][x[1]])
            
        else:
            ciphertext.append(format_table[itext[i-1][0]][x[1]])
            ciphertext.append(format_table[x[0]][itext[i-1][1]])
            
print '***********************'

ciphertext=''.join([u for x in ciphertext for u in x])
print ciphertext.lower()
fo=open('cleartext.txt','w')
fo.writelines(ciphertext.lower())
fo.close()




























