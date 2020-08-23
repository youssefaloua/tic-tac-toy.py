# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 13:09:38 2020

@author: HP
"""
from random import*
from tkinter import*
def nothing():
    x=1
    x=True
def avec_ami():
    test.append(0)
    print(test)
def avec_pc():
    test.append(1)
    print(test)
def win(liste,f):
    s1=0
    s2=0
    s3=0
    s4=0
    s5=6
    s6=0
    s7=0
    s8=0
    for i in range(3):
          s1=sum(liste[0])
          s2=sum(liste[1])
          s3=sum(liste[2])
          s4=liste[0][0]+liste[1][0]+liste[2][0]
          s5=liste[0][1]+liste[1][1]+liste[2][1]
          s6=liste[0][2]+liste[1][2]+liste[2][2]
          s7=liste[0][0]+liste[1][1]+liste[2][2]
          s8=liste[0][2]+liste[1][1]+liste[2][0]
    if ( s1==3*f or s2==3*f or s3==3*f or s4==3*f or s5==3*f or s6==3*f or s7==3*f or s8==3*f):
        print(s1 , s2 ,s3,s4,s5,s8,s7,s8)
        return True
    else:
        return False
def tao_x(i):
  if test[len(test)-1]==0:
    if vr[len(vr)-1]==1:
       if tab[len(tab)-1]=='o':
           b1.config(text="X",font=("impact",19),padx=12,pady=7,command=nothing)
           tab.append('x')
           winer[0][0]=-1
       else :
           b1.config(text="0",font=("impact",19),padx=12,pady=7,command=nothing)
           tab.append('o')
           winer[0][0]=1
    if vr[len(vr)-1]==2:
       if tab[len(tab)-1]=='o':
           b2.config(text="X",font=("impact",19),padx=12,pady=7,command=nothing)
           tab.append('x')
           winer[0][1]=-1
       else :
           b2.config(text="0",font=("impact",19),padx=12,pady=7,command=nothing)
           tab.append('o')
           winer[0][1]=1
    if vr[len(vr)-1]==3:
       if tab[len(tab)-1]=='o':
           b3.config(text="X",font=("impact",19),padx=12,pady=7,command=nothing)
           tab.append('x')
           winer[0][2]=-1
       else :
           b3.config(text="0",font=("impact",19),padx=12,pady=7,command=nothing)
           tab.append('o')
           winer[0][2]=1
    if vr[len(vr)-1]==4:
       if tab[len(tab)-1]=='o':
           b4.config(text="X",font=("impact",19),padx=12,pady=7,command=nothing)
           tab.append('x')
           winer[1][0]=-1
       else :
           b4.config(text="0",font=("impact",19),padx=12,pady=7,command=nothing)
           tab.append('o')
           winer[1][0]=1
    if vr[len(vr)-1]==5:
       if tab[len(tab)-1]=='o':
           b5.config(text="X",font=("impact",19),padx=12,pady=7,command=nothing)
           tab.append('x')
           winer[1][1]=-1
       else :
           b5.config(text="0",font=("impact",19),padx=12,pady=7,command=nothing)
           tab.append('o')
           winer[1][1]=1
    if vr[len(vr)-1]==6:
       if tab[len(tab)-1]=='o':
           b6.config(text="X",font=("impact",19),padx=12,pady=7,command=nothing)
           tab.append('x')
           winer[1][2]=-1
       else :
           b6.config(text="0",font=("impact",19),padx=12,pady=7,command=nothing)
           tab.append('o')
           winer[1][2]=1
    if vr[len(vr)-1]==7:
       if tab[len(tab)-1]=='o':
           b7.config(text="X",font=("impact",19),padx=12,pady=7,command=nothing)
           tab.append('x')
           winer[2][0]=-1
       else :
           b7.config(text="0",font=("impact",19),padx=12,pady=7,command=nothing)
           tab.append('o')
           winer[2][0]=1
    if vr[len(vr)-1]==8:
       if tab[len(tab)-1]=='o':
           b8.config(text="X",font=("impact",19),padx=12,pady=7,command=nothing)
           tab.append('x')
           winer[2][1]=-1
       else :
           b8.config(text="0",font=("impact",19),padx=12,pady=7,command=nothing)
           tab.append('o')
           winer[2][1]=1
    if vr[len(vr)-1]==9:
       if tab[len(tab)-1]=='o':
           b9.config(text="X",font=("impact",19),padx=12,pady=7,command=nothing)
           tab.append('x')
           winer[2][2]=-1
           print(winer)
       else :
           b9.config(text="0",font=("impact",19),padx=12,pady=7,command=nothing)
           tab.append('o')
           winer[2][2]=1
           print(winer)
    if win(winer,1)==1:
        print("le jour avec o gange")
        b9.config(command=nothing)
        b8.config(command=nothing)
        b7.config(command=nothing)
        b6.config(command=nothing)
        b5.config(command=nothing)
        b4.config(command=nothing)
        b3.config(command=nothing)
        b2.config(command=nothing)
        b1.config(command=nothing)
    if win(winer,-1)==1:
        print("le jour avec x gange")
        b9.config(command=nothing)
        b8.config(command=nothing)
        b7.config(command=nothing)
        b6.config(command=nothing)
        b5.config(command=nothing)
        b4.config(command=nothing)
        b3.config(command=nothing)
        b2.config(command=nothing)
        b1.config(command=nothing)
  if test[len(test)-1]==1:
    s1=0
    s2=0
    s3=0
    s4=0
    s5=6
    s6=0
    s7=0
    s8=0
    s1=sum(winer[0])
    s2=sum(winer[1])
    s3=sum(winer[2])
    s4=winer[0][0]+winer[1][0]+winer[2][0]
    s5=winer[0][1]+winer[1][1]+winer[2][1]
    s6=winer[0][2]+winer[1][2]+winer[2][2]
    s7=winer[0][0]+winer[1][1]+winer[2][2]
    s8=winer[0][2]+winer[1][1]+winer[2][0]
    S1=[winer[0][0],winer[1][0],winer[2][0]]
    S2=[winer[0][1],winer[1][1],winer[2][1]]
    S3=[winer[0][2],winer[1][2],winer[2][2]]
    S4=[winer[0][0],winer[1][1],winer[2][2]]
    S5=[winer[0][2],winer[1][1],winer[2][0]]
    print("s4 =",S4)
    print(S5)
    if vr[len(vr)-1]==1 and i[len(i)-1]==0:
           b1.config(text="X",font=("impact",19),padx=12,pady=7,command=nothing)
           tab.append('x')
           winer[0][0]=-1
           i.append(1)
           exit
    if vr[len(vr)-1]==2 and i[len(i)-1]==0:
           b2.config(text="X",font=("impact",19),padx=12,pady=7,command=nothing)
           tab.append('x')
           winer[0][1]=-1
           i.append(1)
    if vr[len(vr)-1]==3 and i[len(i)-1]==0:
           b3.config(text="X",font=("impact",19),padx=12,pady=7,command=nothing)
           tab.append('x')
           winer[0][2]=-1
           i.append(1)
    if vr[len(vr)-1]==4 and i[len(i)-1]==0:
           b4.config(text="X",font=("impact",19),padx=12,pady=7,command=nothing)
           tab.append('x')
           winer[1][0]=-1
           i.append(1)
           exit
    if vr[len(vr)-1]==5 and i[len(i)-1]==0:
           b5.config(text="X",font=("impact",19),padx=12,pady=7,command=nothing)
           tab.append('x')
           winer[1][1]=-1
           i.append(1)
           exit
    if vr[len(vr)-1]==6 and i[len(i)-1]==0:
           b6.config(text="X",font=("impact",19),padx=12,pady=7,command=nothing)
           winer[1][2]=-1
           i.append(1)
           exit
    if vr[len(vr)-1]==7 and i[len(i)-1]==0:
           b7.config(text="X",font=("impact",19),padx=12,pady=7,command=nothing)
           winer[2][0]=-1
           i.append(1)
           exit
    if vr[len(vr)-1]==8 and i[len(i)-1]==0:
           b8.config(text="X",font=("impact",19),padx=12,pady=7,command=nothing)
           winer[2][1]=-1
           i.append(1)
           exit
    if vr[len(vr)-1]==9 and i[len(i)-1]==0:
           b9.config(text="X",font=("impact",19),padx=12,pady=7,command=nothing)
           winer[2][2]=-1
           print(winer)
           i.append(1)
           print(i)
           exit
    s1=sum(winer[0])
    s2=sum(winer[1])
    s3=sum(winer[2])
    s4=winer[0][0]+winer[1][0]+winer[2][0]
    s5=winer[0][1]+winer[1][1]+winer[2][1]
    s6=winer[0][2]+winer[1][2]+winer[2][2]
    s7=winer[0][0]+winer[1][1]+winer[2][2]
    s8=winer[0][2]+winer[1][1]+winer[2][0]
    S1=[winer[0][0],winer[1][0],winer[2][0]]
    S2=[winer[0][1],winer[1][1],winer[2][1]]
    S3=[winer[0][2],winer[1][2],winer[2][2]]
    S4=[winer[0][0],winer[1][1],winer[2][2]]
    S5=[winer[0][2],winer[1][1],winer[2][0]]
    print("c est ton role")
    print("s4 =",S4)
    print(S5)
    if s1==2 or s2==2 or s3==2 or s4==2 or s5==2 or s6==2 or s7==2 or s8==2:
        if s1==2 and winer[0]==[1,1,0] and i[len(i)-1]==1:
           b3.config(text="O",font=("impact",19),padx=12,pady=7,command=nothing)
           winer[0][2]=1
           i.append(0)
        if s1==2 and winer[0]==[1,0,1] and i[len(i)-1]==1:
           b2.config(text="O",font=("impact",19),padx=12,pady=7,command=nothing)
           i.append(0)
           winer[0][1]=1
        if s1==2 and winer[0]==[0,1,1] and i[len(i)-1]==1:
           b1.config(text="O",font=("impact",19),padx=12,pady=7,command=nothing)
           i.append(0)
           winer[0][0]=1
        if s2==2 and winer[1]==[1,1,0] and i[len(i)-1]==1:
           b6.config(text="O",font=("impact",19),padx=12,pady=7,command=nothing)
           i.append(0)
           winer[1][2]=1
        if s2==2 and winer[1]==[1,0,1 and i[len(i)-1]==1]:
           b5.config(text="O",font=("impact",19),padx=12,pady=7,command=nothing)
           i.append(0)
           winer[1][1]=1
        if s2==2 and winer[1]==[0,1,1] and i[len(i)-1]==1:
           b4.config(text="O",font=("impact",19),padx=12,pady=7,command=nothing)
           i.append(0)
           winer[1][0]=1
        if s3==2 and winer[2]==[1,1,0] and i[len(i)-1]==1:
           b9.config(text="O",font=("impact",19),padx=12,pady=7,command=nothing)
           i.append(0)
           winer[2][2]=1
        if s3==2 and winer[2]==[1,0,1] and i[len(i)-1]==1:
           b8.config(text="O",font=("impact",19),padx=12,pady=7,command=nothing)
           i.append(0)
           winer[2][1]=1
        if s3==2 and winer[2]==[0,1,1] and i[len(i)-1]==1:
           b7.config(text="O",font=("impact",19),padx=12,pady=7,command=nothing)
           i.append(0)
           winer[2][0]=1
        if s4==2 and S1==[1,1,0] and i[len(i)-1]==1:
           b7.config(text="O",font=("impact",19),padx=12,pady=7,command=nothing)
           i.append(0)
           winer[2][0]=1
        if s4==2 and S1==[1,0,1] and i[len(i)-1]==1:
           b5.config(text="O",font=("impact",19),padx=12,pady=7,command=nothing)
           i.append(0)
           winer[1][1]=1
        if s4==2 and S1==[0,1,1] and i[len(i)-1]==1:
           b1.config(text="O",font=("impact",19),padx=12,pady=7,command=nothing)
           i.append(0)
           winer[0][0]=1
        if s5==2 and S2==[1,1,0] and i[len(i)-1]==1:
           b8.config(text="O",font=("impact",19),padx=12,pady=7,command=nothing)
           i.append(0)
           winer[2][1]=1
        if s5==2 and S2==[1,0,1 and i[len(i)-1]==1]:
           b5.config(text="O",font=("impact",19),padx=12,pady=7,command=nothing)
           i.append(0)
           winer[1][1]=1
        if s5==2 and S2==[0,1,1] and i[len(i)-1]==1:
           b2.config(text="O",font=("impact",19),padx=12,pady=7,command=nothing)
           i.append(0)
           winer[0][1]=1
        if s6==2 and S3==[1,1,0] and i[len(i)-1]==1:
           b9.config(text="O",font=("impact",19),padx=12,pady=7,command=nothing)
           i.append(0)
           winer[2][2]=1
        if s6==2 and S3==[1,0,1] and i[len(i)-1]==1:
           b6.config(text="O",font=("impact",19),padx=12,pady=7,command=nothing)
           i.append(0)
           winer[1][2]=1
        if s6==2 and S3==[0,1,1] and i[len(i)-1]==1:
           b3.config(text="O",font=("impact",19),padx=12,pady=7,command=nothing)
           i.append(0)
           winer[0][2]=1
        if s7==2 and S4==[1,1,0] and i[len(i)-1]==1:
           b9.config(text="O",font=("impact",19),padx=12,pady=7,command=nothing)
           i.append(0)
           winer[2][2]=1
        if s7==2 and S4==[1,0,1] and i[len(i)-1]==1:
           b5.config(text="O",font=("impact",19),padx=12,pady=7,command=nothing)
           i.append(0)
           winer[1][1]=1
        if s7==2 and S4==[0,1,1] and i[len(i)-1]==1:
           b1.config(text="O",font=("impact",19),padx=12,pady=7,command=nothing)
           i.append(0)
           winer[0][0]=1
        if s8==2 and S5==[1,1,0] and i[len(i)-1]==1:
           b7.config(text="O",font=("impact",19),padx=12,pady=7,command=nothing)
           i.append(0)
           winer[2][0]=1
        if s8==2 and S5==[1,0,1] and i[len(i)-1]==1:
           b5.config(text="O",font=("impact",19),padx=12,pady=7,command=nothing)
           i.append(0)
           winer[1][1]=1
        if s8==2 and S5==[0,1,1] and i[len(i)-1]==1:
           b3.config(text="O",font=("impact",19),padx=12,pady=7,command=nothing)
           i.append(0)
           winer[0][2]=1
    if winer[1][1]==0 and i[len(i)-1]==1:
        b5.config(text="O",font=("impact",19),padx=12,pady=7,command=nothing)
        tab.append('o')
        i.append(0)
        winer[1][1]=1
    if s1==-2:
        if winer[0][1]==-1 and winer[0][0]==-1 and i[len(i)-1]==1:
            b3.config(text="O",font=("impact",19),padx=12,pady=7,command=nothing)
            i.append(0)
            winer[0][2]=1
        if winer[0][1]==-1 and winer[0][2]==-1 and i[len(i)-1]==1:
            b1.config(text="O",font=("impact",19),padx=12,pady=7,command=nothing)
            i.append(0)
            winer[0][0]=1
        if winer[0][0]==-1 and winer[0][2]==-1 and i[len(i)-1]==1:
            b2.config(text="O",font=("impact",19),padx=12,pady=7,command=nothing)
            i.append(0)
            winer[0][1]=1
    if s2==-2:
        if winer[1][1]==-1 and winer[1][0]==-1 and i[len(i)-1]==1:
            b6.config(text="O",font=("impact",19),padx=12,pady=7,command=nothing)
            i.append(0)
            winer[1][2]=1
        if winer[1][1]==-1 and winer[1][2]==-1 and i[len(i)-1]==1:
            b4.config(text="O",font=("impact",19),padx=12,pady=7,command=nothing)
            i.append(0)
            winer[1][0]=1

        if winer[1][0]==-1 and winer[1][2]==-1 and i[len(i)-1]==1:
            b5.config(text="O",font=("impact",19),padx=12,pady=7,command=nothing)
            i.append(0)
            winer[1][1]=1
    if s3==-2:
        if winer[2][1]==-1 and winer[2][0]==-1 and i[len(i)-1]==1:
            b9.config(text="O",font=("impact",19),padx=12,pady=7,command=nothing)
            i.append(0)
            winer[2][2]=1
        if winer[2][1]==-1 and winer[2][2]==-1 and i[len(i)-1]==1:
            b7.config(text="O",font=("impact",19),padx=12,pady=7,command=nothing)
            i.append(0)
            winer[2][0]=1
        if winer[2][0]==-1 and winer[2][2]==-1 and i[len(i)-1]==1:
            b8.config(text="O",font=("impact",19),padx=12,pady=7,command=nothing)
            i.append(0)
            winer[2][1]=1
    if s4== -2:
        if winer[0][0]==-1 and winer[1][0]==-1 and i[len(i)-1]==1:
            b7.config(text="O",font=("impact",19),padx=12,pady=7,command=nothing)
            i.append(0)
            winer[2][0]=1

        if winer[1][0]==-1 and winer[2][0]==-1 and i[len(i)-1]==1:
            b1.config(text="O",font=("impact",19),padx=12,pady=7,command=nothing)
            i.append(0)
            winer[0][0]=1
        if winer[0][0]==-1 and winer[2][0]==-1 and i[len(i)-1]==1:
            b4.config(text="O",font=("impact",19),padx=12,pady=7,command=nothing)
            i.append(0)
            winer[1][0]=1
    if s5==-2:
        if winer[0][1]==-1 and winer[1][1]==-1 and i[len(i)-1]==1:
            b8.config(text="O",font=("impact",19),padx=12,pady=7,command=nothing)
            i.append(0)
            winer[2][1]=1
        if winer[1][1]==-1 and winer[2][1]==-1 and i[len(i)-1]==1:
            b2.config(text="O",font=("impact",19),padx=12,pady=7,command=nothing)
            i.append(0)
            winer[2][1]=1
        if winer[0][1]==-1 and winer[2][1]==-1 and i[len(i)-1]==1:
            b5.config(text="O",font=("impact",19),padx=12,pady=7,command=nothing)
            i.append(0)
            winer[1][1]=1
    if s6==-2:
        if winer[0][2]==-1 and winer[1][2]==-1 and i[len(i)-1]==1:
            b9.config(text="O",font=("impact",19),padx=12,pady=7,command=nothing)
            i.append(0)
            winer[2][2]=1

        if winer[1][2]==-1 and winer[2][2]==-1 and i[len(i)-1]==1:
            b3.config(text="O",font=("impact",19),padx=12,pady=7,command=nothing)
            i.append(0)
            winer[0][2]=1
        if winer[0][2]==-1 and winer[2][2]==-1 and i[len(i)-1]==1  :
            b6.config(text="O",font=("impact",19),padx=12,pady=7,command=nothing)
            i.append(0)
            winer[1][2]=1
    if s7==-2:
       if winer[0][0]==-1 and winer[1][1]==-1 and i[len(i)-1]==1:
           b9.config(text="O",font=("impact",19),padx=12,pady=7,command=nothing)
           i.append(0)
           winer[2][2]=1
       if winer[1][1]==-1 and winer[2][2]==-1 and i[len(i)-1]==1:
           b1.config(text="O",font=("impact",19),padx=12,pady=7,command=nothing)
           i.append(0)
           winer[0][0]=1
       if winer[0][0]==-1 and winer[2][2]==-1 and i[len(i)-1]==1:
           b5.config(text="O",font=("impact",19),padx=12,pady=7,command=nothing)
           i.append(0)
           winer[1][1]=1
    if s8==-2:
       if winer[0][2]==-1 and winer[1][1]==-1 and i[len(i)-1]==1:
           b7.config(text="O",font=("impact",19),padx=12,pady=7,command=nothing)
           i.append(0)
           winer[2][0]=1
       if winer[1][1]==-1 and winer[2][0]==-1 and i[len(i)-1]==1:
           b3.config(text="O",font=("impact",19),padx=12,pady=7,command=nothing)
           i.append(0)
           winer[0][2]=1
       if winer[2][0]==-1 and winer[0][2]==-1 and i[len(i)-1]==1:
           b5.config(text="O",font=("impact",19),padx=12,pady=7,command=nothing)
           i.append(0)
           winer[1][1]=1
    if s1== 0 and i[len(i)-1]==1 :
         if winer[0]==[0,0,0]:
           b3.config(text="O",font=("impact",19),padx=12,pady=7,command=nothing)
           i.append(0)
           winer[0][2]=1
         if winer[0]==[-1,0,1]:
           b2.config(text="O",font=("impact",19),padx=12,pady=7,command=nothing)
           i.append(0)
           winer[0][1]=1
         if winer[0]==[0,-1,1]:
           b1.config(text="O",font=("impact",19),padx=12,pady=7,command=nothing)
           i.append(0)
           winer[0][0]=1
         if winer[0]==[1,-1,0]:
           b4.config(text="O",font=("impact",19),padx=12,pady=7,command=nothing)
           i.append(0)
           winer[1][0]=1
    if s2== 0 and i[len(i)-1]==1 :
         if winer[1]==[0,0,0]:
           b4.config(text="O",font=("impact",19),padx=12,pady=7,command=nothing)
           i.append(0)
           winer[1][0]=1
    if s3== 0 and i[len(i)-1]==1 :
         if winer[2]==[0,0,0]:
           b7.config(text="O",font=("impact",19),padx=12,pady=7,command=nothing)
           i.append(0)
           winer[2][0]=1
         if winer[2]==[-1,0,1]:
           b8.config(text="O",font=("impact",19),padx=12,pady=7,command=nothing)
           i.append(0)
           winer[2][1]=1
         if winer[2]==[0,-1,1]:
           b7.config(text="O",font=("impact",19),padx=12,pady=7,command=nothing)
           i.append(0)
           winer[2][0]=1
         if winer[0]==[1,-1,0]:
           b9.config(text="O",font=("impact",19),padx=12,pady=7,command=nothing)
           i.append(0)
           winer[2][2]=1
    if s6== 1 and i[len(i)-1]==1 :
         if winer[2]==[0,-1,0]:
           b9.config(text="O",font=("impact",19),padx=12,pady=7,command=nothing)
           i.append(0)
           winer[2][2]=1
    if s5== 1 and i[len(i)-1]==1 :
         if winer[2]==[0,0,-1]:
           b8.config(text="O",font=("impact",19),padx=12,pady=7,command=nothing)
           i.append(0)
           winer[2][1]=1
    if winer[1]==[1,1,-1] or winer[1]==[-1,-1,1] or winer[1]==[1,-1,1]:
        if i[len[i]-1]==1:
         if winer[0]==[-1,0,1]:
           b2.config(text="O",font=("impact",19),padx=12,pady=7,command=nothing)
           i.append(0)
           winer[0][1]=1
         if winer[0]==[0,-1,1]:
           b1.config(text="O",font=("impact",19),padx=12,pady=7,command=nothing)
           i.append(0)
           winer[0][0]=1
         if winer[0]==[1,-1,0]:
           b4.config(text="O",font=("impact",19),padx=12,pady=7,command=nothing)
           i.append(0)
           winer[1][0]=1
         else:
          if winer[2]==[-1,0,1]:
           b8.config(text="O",font=("impact",19),padx=12,pady=7,command=nothing)
           i.append(0)
           winer[2][1]=1
          if winer[2]==[0,-1,1]:
           b7.config(text="O",font=("impact",19),padx=12,pady=7,command=nothing)
           i.append(0)
           winer[2][0]=1
          if winer[0]==[1,-1,0]:
           b9.config(text="O",font=("impact",19),padx=12,pady=7,command=nothing)
           i.append(0)
           winer[2][2]=1
    if win(winer,1)==1:
        print("le jour avec o gange")
        b9.config(command=nothing)
        b8.config(command=nothing)
        b7.config(command=nothing)
        b6.config(command=nothing)
        b5.config(command=nothing)
        b4.config(command=nothing)
        b3.config(command=nothing)
        b2.config(command=nothing)
        b1.config(command=nothing)
    if win(winer,-1)==1:
        print("le jour avec x gange")
        b9.config(command=nothing)
        b8.config(command=nothing)
        b7.config(command=nothing)
        b6.config(command=nothing)
        b5.config(command=nothing)
        b4.config(command=nothing)
        b3.config(command=nothing)
        b2.config(command=nothing)
        b1.config(command=nothing)
def scan_1():
    vr.append(1)
    tic.after(100,tao_x(i))
def scan_2() :
    vr.append(2)
    tic.after(100,tao_x(i))
def scan_3():
    vr.append(3)
    tic.after(100,tao_x(i))
def scan_4():
    vr.append(4)
    tic.after(100,tao_x(i))
def scan_5():
    vr.append(5)
    tic.after(100,tao_x(i))
def scan_6():
    vr.append(6)
    tic.after(100,tao_x(i))
def scan_7():
    vr.append(7)
    tic.after(100,tao_x(i))
def scan_8():
    vr.append(8)
    tic.after(100,tao_x(i))
def scan_9():
    vr.append(9)
    tic.after(100,tao_x(i))



tic=Tk()
test=[-1]
tab=['o']
vr=[0]
i=[0]
winer=[[0,0,0],[0,0,0],[0,0,0]]
tic.title("tic tac toy")
tic.geometry("300x250+150+0")
tic.minsize(300,250)
tic.maxsize(300,250)
canvas=Canvas(tic,width=450,height=700,bd=2,bg="red")
canvas.grid(row=0,column=0,sticky="W")
c1=Canvas(canvas,width=50,height=50,bd=2)
c1.grid(row=0,column=0)
c2=Canvas(canvas,width=50,height=50,bd=2)
c2.grid(row=0,column=1)
c3=Canvas(canvas,width=50,height=50,bd=2)
c3.grid(row=0,column=2)
c4=Canvas(canvas,width=50,height=50,bd=2)
c4.grid(row=1,column=0)
c5=Canvas(canvas,width=50,height=50,bd=2)
c5.grid(row=1,column=1)
c6=Canvas(canvas,width=50,height=50,bd=2)
c6.grid(row=1,column=2)
c7=Canvas(canvas,width=50,height=50,bd=2)
c7.grid(row=2,column=0)
c8=Canvas(canvas,width=50,height=50,bd=2)
c8.grid(row=2,column=1)
c9=Canvas(canvas,width=50,height=50,bd=2)
c9.grid(row=2,column=2)
b1=Button(c1,padx=21,pady=20,bg="red",command=scan_1)
b1.grid(row=0,column=0)
b2=Button(c2,padx=21,pady=20,bg="red",command=scan_2)
b2.grid(row=0,column=1)
b3=Button(c3,padx=21,pady=20,bg="red",command=scan_3)
b3.grid(row=0,column=2)
b4=Button(c4,padx=21,pady=20,bg="red",command=scan_4)
b4.grid(row=0,column=0)
b5=Button(c5,padx=21,pady=20,bg="red",command=scan_5)
b5.grid(row=0,column=1)
b6=Button(c6,padx=21,pady=20,bg="red",command=scan_6)
b6.grid(row=0,column=2)
b7=Button(c7,padx=21,pady=20,bg="red",command=scan_7)
b7.grid(row=0,column=0)
b8=Button(c8,padx=21,pady=20,bg="red",command=scan_8)
b8.grid(row=0,column=1)
b9=Button(c9,padx=21,pady=20,bg="red",command=scan_9)
b9.grid(row=0,column=2)
BJ=Button(canvas,text="   JEUER AVEC UN AMI ",command=avec_ami)
BJ.grid(row=18,column=18,sticky="S")
BJ=Button(canvas,text="JOUER AVEC RDINNATEUR",command=avec_pc)
BJ.grid(row=19,column=18,sticky="S")
tic.mainloop()