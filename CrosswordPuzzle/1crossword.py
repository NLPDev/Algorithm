import random
import math
import sys
import re
import collections
import string
import heapq
import time

#### Nuha Mohammed
BLOCK, EMPTY= '#', '-'

def str_index(text,index,replacement):
    return '%s%s%s'%(text[:index],replacement,text[index+1:])

def makeboard(h,v, blocked, cword, file, l, w):
    bb=list()
    total=l*w
    cword= EMPTY*total
    if blocked%2 is 1:
        cword= str_index(cword,int(l*w/2),BLOCK)
        bb.append(int(l*w/2))
    for num in h:
        r= int(num[0:num.index('x')])
        c=int(num[num.index('x')+1:num.index(' ')])
        num = num[num.index(" ")+1:].upper()
        for i in range(len(num)):
            if num[i] is BLOCK: bb.append(r*w+c+i)
            cword= str_index(cword,r*w+c+i,num[i])
    for num in v:
        r= int(num[0:num.index('x')])
        c=int(num[num.index('x')+1:num.index(' ')])
        num = num[num.index(" ")+1:].upper()
        for i in range(len(num)):
            if num[i] is BLOCK: bb.append((r+i)*w+c)
            cword= str_index(cword,(r+i)*w+c, num[i])
    return cword

def printword(cword, l,w):
    for i in range(l):
        for j in range(w):
            print(cword[i*w+j]+" ", end =" ")
        print("\n")

def rotsym(n, l,w):
    r, c= int(n/w), n%w
    return l-r-1,w-c-1,(l-r-1)*w+w-c-1

def inlist(word, list):
    if word.lower() in list: return True, word.lower()
    if word.upper() in list: return True, word.upper()
    return False, ""

def checkdir(cword,r,c,l,w, dir,val):
    myblox=set()
    if dir is "H":
        if  ((c+2*val>=w and c+val<w) or (c+val>=0 and  c+2*val<0)) and cword[r*w+c+val]==EMPTY:
            cword= str_index(cword,r*w+c+val,BLOCK)
            a,b,n = rotsym(r*w+c+val, l, w)
            cword=str_index(cword,a*w+b,BLOCK)
            myblox.add((r, c+val))
            myblox.add((a,b))
        if  ((c+3*val>=w and c+val<w and c+2*val<w) or (c+3*val<0 and c+2*val>=0 and c+val>=0)) and r<l and r>=0 and cword[r*w+c+val]==EMPTY and cword[r*w+c+2*val]==EMPTY:
            cword= str_index(cword, r*w+c+2*val ,BLOCK)
            cword= str_index(cword, r*w+c+val ,BLOCK)
            a,b, n = rotsym(r*w+c+val, l, w)
            a1,b1, n1 = rotsym(r*w+c+2*val, l, w)
            cword= str_index(cword, n ,BLOCK)
            cword= str_index(cword, n1 ,BLOCK)
            myblox.add((r, c+val))
            myblox.add((r, c+2*val))
            myblox.add((a,b))
            myblox.add((a1,b1))
        if c+2*val<w and  c+2*val>=0 and cword[r*w+c+val]==EMPTY and cword[r*w+c+2*val]==BLOCK:
            cword= str_index(cword, r*w+c+val ,BLOCK)
            a,b, n = rotsym(r*w+c+val, l, w)
            cword= str_index(cword, n ,BLOCK)
            myblox.add((r, c+val))
            myblox.add((a,b))
        if c+3*val<w and c+3*val>=0 and c+2*val>=0 and c+2*val<w and cword[r*w+c+val]==EMPTY and cword[r*w+c+2*val]==EMPTY and cword[r*w+c+3*val]==BLOCK:
            cword= str_index(cword, r*w+c+val ,BLOCK)
            cword= str_index(cword, r*w+c+val*2 ,BLOCK)
            a,b, n= rotsym(r*w+c+val, l, w)
            a1,b1, n1= rotsym(r*w+c+2*val, l, w)
            cword= str_index(cword, n ,BLOCK)
            cword= str_index(cword, n1 ,BLOCK)
            myblox.add((r, c+val))
            myblox.add((r, c+2*val))
            myblox.add((a,b))
            myblox.add((a1,b1))
    else:
        if r+2*val<l and r+2*val>=0  and c<w and c>=0 and cword[(r+val)*w+c] is EMPTY and cword[(r+2*val)*w+c]==BLOCK:
            cword= str_index(cword, (r+val)*w+c ,BLOCK)
            a,b, n = rotsym((r+val)*w+c, l, w)
            cword= str_index(cword, n ,BLOCK)
            myblox.add((r+val, c))
            myblox.add((a,b))
        if r+3*val<l and r+3*val>=0  and c<w and c>=0 and cword[(r+val)*w+c]==EMPTY and cword[(r+2*val)*w+c]==EMPTY and cword[(r+3*val)*w+c]==BLOCK:
            cword= str_index(cword, (r+val)*w+c ,BLOCK)
            word= str_index(cword, (r+2*val)*w+c ,BLOCK)
            a,b, n= rotsym((r+val)*w+c, l, w)
            a1,b1, n1= rotsym((r+2*val)*w+c, l, w)
            cword= str_index(cword, n ,BLOCK)
            cword= str_index(cword, n1 ,BLOCK)
            myblox.add((r+2*val, c))
            myblox.add((r+val, c))
            myblox.add((a1,b1))
            myblox.add((a,b))
        if  ((r+2*val>=l and r+val<l) or (r+val>=0 and  r+2*val<0)) and cword[(r+val)*w+c]==EMPTY:
            cword= str_index(cword, (r+val)*w+c ,BLOCK)
            a,b, n= rotsym((r+val)*w+c, l, w)
            cword= str_index(cword, n ,BLOCK)
            myblox.add((r+val, c))
            myblox.add((a,b))
        if  ((r+3*val>=l and r+val<l and r+2*val<l) or (r+3*val<0 and r+2*val>=0 and r+val>=0)) and r<l and r>=0 and cword[(r+val)*w+c]==EMPTY and cword[(r+2*val)*w+c]==EMPTY:
            cword= str_index(cword, (r+2*val)*w+c ,BLOCK)
            cword= str_index(cword, (r+val)*w+c ,BLOCK)
            a,b, n= rotsym((r+val)*w+c, l, w)
            a1,b1, n1 = rotsym((r+2*val)*w+c, l, w)
            cword= str_index(cword, n ,BLOCK)
            cword= str_index(cword, n1 ,BLOCK)
            myblox.add((r+val, c))
            myblox.add((r+2*val, c))
            myblox.add((a,b))
            myblox.add((a1,b1))
    return cword, myblox


def failure(cword,l,w, dictwords):
    used=set()
    finall=list()
    new_dict =dictwords
    for i in range(l): #rows
        myrow=cword[w*i:w*(i+1)]
        for match in re.finditer(r"(?<=#)[^#]+(?=#)?|(?<=#)?[^#]+(?=#)|^(\w*-+)+$", myrow, re.I):
            mym= match.group(0)
            if EMPTY not in mym:
                if mym not in dictwords: return True, None, dictwords
                if mym in used: return True, None, dictwords
                used.add(mym)
            finall.append((i, mym, "H"))
            regex = r"^"+mym.replace(EMPTY, '\w')+"$"
            r = re.compile(regex)
            newlist = list(filter(r.match, new_dict))
            if len(newlist)==0: return True, None, dictwords
    
    for j in range(w):
        col=str()
        for i in range(l): #cols
            col+=cword[i*w+j]
        for match in re.finditer(r"(?<=#)[^#]+(?=#)?|(?<=#)?[^#]+(?=#)|^(\w*-+)+$", col, re.I):
            mym= match.group(0)
            if EMPTY not in mym:
                if mym not in dictwords: return True, None, dictwords
                if mym in used: return True, None, dictwords
                used.add(mym)
            finall.append((j, mym, "V"))
            regex = r"^"+mym.replace(EMPTY, '\w')+"$"
            r = re.compile(regex)
            newlist = list(filter(r.match, dictwords))
            if len(newlist)==0: return True, None, dictwords

    return False, finall, new_dict

def wordstrategy(cword, l,w, dictwords, t):
    printword(cword,l,w)
    fail, spaces, new_dict = failure(cword,l,w,dictwords)
    if fail: return None
    elif cword.count(EMPTY)==0: return cword
    check=list()
    for val in spaces:
        index, word, dir= val
        scorr= (len(word)-word.count(EMPTY))/len(word)
        word=word.upper()
        if dir is "H":
            myline= cword[index*w:(index+1)*w]
            myline=myline.upper()
            j = myline.index(word)
            heapq.heappush(check,(-scorr, word, index*w+j, "H"))
        else:
            myline=str()
            for x in range(l):
                myline+=cword[x*w+index]
            i=  myline.index(word)
            heapq.heappush(check,(-scorr, word, i*w+index, "V"))

    s, bestspot, abcd , dir = heapq.heappop(check)
    regex= r"^"+bestspot.replace(EMPTY, "\w")+"$"
    r = re.compile(regex)
    newlist = list(filter(r.match, dictwords))
    fringe=list()
    for word in newlist: heapq.heappush(fringe, (-score(word), word))
    new_dict=dictwords
    while len(fringe) > 0:
        sc, word = heapq.heappop(fringe)
        b, word= inlist(word,dictwords)
        if b: new_dict.remove(word)
        new_cword=cword
        if dir is "H":
            for i in range(len(word)):
                new_cword= str_index(new_cword, abcd+i, word[i])
                print(cword)
        else:
            for i in range(len(word)):
                new_cword= str_index(new_cword, abcd+i*w, word[i])
                print(cword)
        new_cword=  wordstrategy(new_cword,l,w, new_dict, t)
        if new_cword: return new_cword
        else: continue
    return None

def score(word):
    eng_freq = [.0817, .0149, .0278, .0425, .1270, .0223, .0202, .0609, .0697, .0015, .0077, .0403, .0241, .0675, .0751,
                .0193, .0010, .0599, .0633, .0906, .0276, .0098, .0236, .0015, .0197, .0007]
    alphanum=dict(zip(string.ascii_lowercase, range(1,27)))
    myscore=0
    word=word.strip()
    for w in word.lower():
        myscore+= eng_freq[alphanum[w]-1]
    return myscore

def impliedblox(cword, l, w, blockb):
    q= blockb
    seen=set()
    while len(q) > 0:
        r, c = q.pop()
        seen.add((r,c))
        cword, a1 = checkdir(cword, r, c,l,w,"H", 1)
        cword, b1= checkdir(cword, r, c,l,w ,"H",-1)
        cword, c1= checkdir(cword, r, c,l,w,"V",1)
        cword, d1= checkdir(cword, r, c,l,w,"V",-1)
        myset= a1.union(b1).union(c1).union(d1)
        blockb+= collections.deque(myset)
        for r1, c1 in set(blockb):
            if (r1, c1) in seen: continue
            else: q.append((r1, c1))
    return cword


def placeextrablocks(cword, target, l,w):
    numb= cword.count(BLOCK)
    if numb>target:return None
    if numb is target: return cword
    for index in getpossibleblox(cword,l,w):
        bbb=collections.deque()
        bbb.append((int(index/w),index%w))
        new_cword = str_index(cword, index, BLOCK)
        a1,b1,n1= rotsym(index,l, w)
        bbb.append((a1,b1))
        new_cword= str_index(new_cword, n1, BLOCK)
        new_cword= impliedblox(new_cword, l, w, bbb)
        new_cword= placeextrablocks(new_cword, target, l, w)
        if new_cword: return new_cword
        else: continue

def getpossibleblox(cword, l, w):
    return [i for i,val in enumerate(cword) if val is EMPTY]

if __name__ == "__main__":
    """testcases = ["4x4 0 scrabble.txt",
                 "5x5 0 scrabble.txt V0x0Imbue",
                 "7x7 11 scrabble.txt",
                 "9x13 19 scrabble.txt V0x1Dog",
                 "9x15 24 scrabble.txt V0x7con V6x7rum",
                 "13x13 32 scrabble.txt V2x4# V1x9# V3x2# h8x2#moo# v5x5#two# h6x4#ten# v3x7#own# h4x6#orb# h0x5Easy",
                 "15x15 42 scrabble.txt H0x0# V0x7### H3x3# H3x8# H3x13## H4x4# H4x10## H5x5# H5x9## H6x0### H6x6# H6x10# H7x0##",
                 "15x15 42 scrabble.txt H0x0#MUFFIN#BRIOCHE V0x7## H3x3# H3x8# H3x13## H4x4# H4x10## H5x5# H5x9## H6x0### H6x6# H6x10# H7x0## H14x0BISCUIT#DANISH",
                 "13x13 28 scrabble.txt"
                 ]"""
    h=list()
    v=list()
    length = len(sys.argv)
    size = sys.argv[1]
    blocknum = int(sys.argv[2])
    file=sys.argv[3]
    i=4
    wh =list()
    while i<length:
        word=sys.argv[i]
        i+=1
        for match in re.finditer(r"\d*x\d*", word, re.I):
            mym= match.group(0)
        if word[0] is 'H' or word[0] is 'h': h.append(mym+" "+word[word.index(mym)+len(mym):])
        else: v.append(mym+" "+word[word.index(mym)+len(mym):])
    cword=dict()
    l,w=int(size[0:size.index('x')]), int(size[size.index('x')+1:])
    cword= makeboard(h,v,blocknum,cword, file, l, w)
    
    aaa=set()
    with open(file, 'r') as f:
        lines = f.readlines()
    lines= [x.strip() for x in lines]
    for x in range(len(cword)):
        if cword[x] is BLOCK:
            a,b, n= rotsym(x,l,w)
            cword= str_index(cword,n, BLOCK)
            aaa.add((int(x/w), x%w))
            aaa.add((a,b))
    bbb=collections.deque(aaa)
    cword= impliedblox(cword, l, w, bbb)
    bn= cword.count(BLOCK)
    if bn<blocknum: cword= placeextrablocks(cword, blocknum ,l,w)
    printword(cword,l,w)
    cword= wordstrategy(cword,l,w, lines, time.time())
    printword(cword,l,w)






