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

    plt.yscale('log')
    plt.xlabel('pt')
    plt.ylabel('dN/2pipTdpT')

    #plt.xlim([0,16])
    #plt.ylim([10**-12,10**1])
    plt.legend()
    plt.show()




#=======================D0 ==============================
ptaliceD0 = np.array([1.5,2.5,3.5,4.5,5.5,7,10,14])
y1D0 = np.array([0.057218684,0.012993631,0.00266151,0.000672328,0.000229589,5.41401E-05,8.32803E-06,1.29663E-06])
yerr = np.array([0.2506,0.0722,0.02038,0.00701,0.003074,0.001099,0.0002545,0.0000683])
yerr = yerr/2/np.pi/ptaliceD0
yerr1 = np.abs(y1D0 - yerr)
yerr2 = np.abs(y1D0 + yerr)
yerr = np.array([yerr1,yerr2])
yerrD0 = np.reshape(yerr,(2,8))
xerrD0 = np.array([0.5,0.5,0.5,0.5,0.5,1,2,2])

recombD0 = openfile("dNptdpt_PbPb276_D0_c40 2.txt", (60, 6), 2)
plot(ptaliceD0[0:7],xerrD0[0:7],y1D0[0:7],yerrD0[:,0:7],recombD0[3:60,:],'D0_2.76 30-50% y=-0.8~0.8')

#========================Jpsi========================

recombinJpsi = openfile("dNptdpt_PbPb276_Jpsi_c30 2.txt", (60, 6), 2)
aliceJpsi = openfile("data_Jpsi_276_30.txt", (13, 4), 1)
plot(aliceJpsi[:,0],aliceJpsi[:,1]/2,aliceJpsi[:,2]*10**(-3),aliceJpsi[:,3]*10**(-3),recombinJpsi[0:35,:],'J/psi_2.76 20-40% y=2.5~4')

#=======================DS=============================

recombinDS = openfile("dNptdpt_PbPb276_Ds_c35 2.txt", (60, 6), 2)
aliceDS = openfile("data_Ds_276_35.txt", (2, 4), 1)
plot(aliceDS[:,0],aliceDS[:,1],aliceDS[:,2],np.array([np.abs(aliceDS[:,2]-aliceDS[:,3]),aliceDS[:,2]+aliceDS[:,3]]),recombinDS[3:60,:],'Ds_2.76 30-40% y=-0.8~0.8')



