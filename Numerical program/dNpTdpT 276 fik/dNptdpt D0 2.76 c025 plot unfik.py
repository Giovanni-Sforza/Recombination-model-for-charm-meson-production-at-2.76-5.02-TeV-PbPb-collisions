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
y_errorD0=[0.258,0.02728,0.004628571,0.001282222,0.0004,7.94286E-05,0.0000125,2.71429E-06]#,0.00000092
y_errorD0 = np.array(y_errorD0)/2/np.pi
xerrD0 = np.array([0.5,0.5,0.5,0.5,0.5,1,2,2])#,2

recombD0 = openfile("dNptdpt_PbPb276_D0_c05 unfik.txt", (60, 6), 2)
aliceD0 = openfile("data_D0_276.dat",(9,2),1)
plot(aliceD0[0:7,0],xerrD0[0:7],aliceD0[0:7,1],y_errorD0[0:7],recombD0[3:60,:],'D0_276 0-5% y=-0.5~0.5')

#========================Jpsi========================


y_errorJpsi = np.array([0.001544,0.000649333,0.0004824,0.000288571,0.000178222,0.000114909,5.63077E-05,3.57333E-05,2.30588E-05,1.45263E-05,8.95238E-06,6.78261E-06,1.28571E-06])/2/np.pi
recombinJpsi = openfile("dNptdpt_PbPb276_Jpsi_c05 unfik.txt", (60, 6), 2)
aliceJpsi = openfile("data_Jpsi_276 (1).dat", (13, 2), 1)
xerrJpsi = np.array([0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,2])/2
plot(aliceJpsi[:,0],xerrJpsi,aliceJpsi[:,1],y_errorJpsi,recombinJpsi[0:35,:],'J/psi_276 0-5% y=-0.9~0.9')

#=======================DS=============================
xerrDs = np.array([1,1,2])
y_errorDS = np.array([0.00284,0.000281429,0.000021])/2/np.pi
recombinDS = openfile("dNptdpt_PbPb276_Ds_c05 unfik.txt", (60, 6), 2)
aliceDS = openfile("data_Ds_276.dat", (3, 2), 1)
plot(aliceDS[0:3,0],xerrDs,aliceDS[0:3,1],y_errorDS,recombinDS[3:60,:],'Ds_276 0-5% y=-0.5~0.5')
#np.array([np.abs(aliceDS[:,2]-aliceDS[:,3]),aliceDS[:,2]+aliceDS[:,3]])





