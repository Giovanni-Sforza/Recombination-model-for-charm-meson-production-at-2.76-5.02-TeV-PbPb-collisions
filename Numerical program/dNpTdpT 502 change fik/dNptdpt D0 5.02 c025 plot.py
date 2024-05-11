import numpy as np
import matplotlib.pyplot as plt

def openfile(filename,size,biginrow):
    file = open(filename, "r")  # 以只读模式打开文件
    lines = file.readlines()  # 获取所有行并保存到lines列表中
    data = []
    # 指定开始读取的行
    for line in lines[int(biginrow) - 1:]:  # 读取指定的所有行
        line = line.strip('\n')  # 去掉换行符
        line = line.split()
        data = np.hstack((data,line)) # 去掉空格
    file.close()  # 关闭文件
    data = np.array(data,dtype=float)
    data = np.reshape(data,size)
    return data
def plot(ptalice,xerr,y1,yerr,recomb,title):
    plt.title(title)
    plt.scatter(ptalice,y1,color='black',label='alice')
    plt.plot(recomb[:,0],recomb[:,1],ls = '-.',label='TT')
    plt.plot(recomb[:,0],recomb[:,2],ls = '--',color = 'blue',label='TS')
    plt.plot(recomb[:,0],recomb[:,3],label='SS1j')
    plt.plot(recomb[:,0],recomb[:,4],color = 'red',label='SS2j')
    plt.plot(recomb[:,0],recomb[:,5],color='black',label='total',lw = 3)
    plt.errorbar(ptalice,y1,xerr = xerr,yerr = yerr,fmt='o', capsize=3)

    #plt.xlim([0,20])
    #plt.ylim([10**(-14),10**(-0)])
    plt.yscale('log')
    plt.xlabel('pt')
    plt.ylabel('dN/2pipTdpT')

    #plt.xlim([0,16])
    #plt.ylim([10**-12,10**1])
    plt.legend()
    plt.show()


#=======================D0==============================

recombD0 = openfile("dNptdpt_PbPb502_D0_c05   c.txt", (60, 6), 2)
aliceD0 = openfile("alice D0 502 5.txt",(22,4),1)
plot(aliceD0[0:18,0],aliceD0[0:18,1]/2,aliceD0[0:18,2],aliceD0[0:18,3],recombD0[:,:],'D0_5.02 0-10% y=-0.5~0.5')

#========================Jpsi========================

recombinJpsi = openfile("dNptdpt_PbPb502_Jpsi_c05   c.txt", (60, 6), 2)
aliceJpsi = openfile("alice Jpsi 502 10.txt", (8, 4), 1)
plot(aliceJpsi[:,0],aliceJpsi[:,1]/2,aliceJpsi[:,2],aliceJpsi[:,3],recombinJpsi[:,:],'J/psi_5.02 0-10% y=-0.9~0.9')

#=======================DS=============================
recombinDS = openfile("dNptdpt_PbPb502_Ds_c05   c.txt", (60, 6), 2)
aliceDS = openfile("alice Ds 502 5.txt", (10, 4), 1)
plot(aliceDS[0:7,0],aliceDS[0:7,1]/2,aliceDS[0:7,2],aliceDS[0:7,3],recombinDS[:,:],'Ds_5.02 0-10% y=-0.5~0.5')
np.array([np.abs(aliceDS[:,2]-aliceDS[:,3]),aliceDS[:,2]+aliceDS[:,3]])





