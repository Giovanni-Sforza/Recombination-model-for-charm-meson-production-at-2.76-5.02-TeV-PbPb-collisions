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


def plot(ptalice,y1,yerr,recomb,color1,color2,title1,title2):
    plt.scatter(ptalice,y1,color=color1,label=title1)
    plt.plot(recomb[:,0],recomb[:,5],color=color2,label=title2,lw = 3)
    plt.errorbar(ptalice,y1,yerr = yerr,color=color1,fmt='o', capsize=3)
    plt.yscale('log')
    plt.xlabel('pt')
    plt.ylabel('dN/2pipTdpT')

    #plt.xlim([0,16])
    #plt.ylim([10**-12,10**1])




#=======================D0 ==============================
ptaliceD0 = np.array([1.5 , 2.5, 3.5, 4.5, 5.5, 7, 10, 14])
y1D0 = np.array([0.057189676,0.012987043,0.002660161,0.000671988 ,0.000229472, 5.41127E-05,8.3238E-06,1.29598E-06])
yerr = np.array([0.2506,0.0722,0.02038,0.00701,0.003074,0.001099,0.0002545,0.0000683])
yerr = yerr/2/np.pi/ptaliceD0
yerr1 = np.abs(y1D0 - yerr)
yerr2 = np.abs(y1D0 + yerr)
yerr = np.array([yerr1,yerr2])
yerrD0 = np.reshape(yerr,(2,8))
xerrD0 = np.array([0.5,0.5,0.5,0.5,0.5,1,2,2])

recombD0 = openfile("dNptdpt_PbPb276_D0_c40.txt", (60, 6), 2)

plt.title('D0_2.76 y=-0.8~0.8')
plot(ptaliceD0,y1D0,yerrD0,recombD0,"purple","blue",'Alice 30-50% ','recombination 30-50%')

plt.xlim([0,16])
y_errorD0=[0.258,0.02728,0.004628571,0.001282222,0.0004,7.94286E-05,0.0000125,2.71429E-06,0.00000092]
y_errorD0 = np.array(y_errorD0)/2/np.pi
aliceD0 = openfile("data_D0_276.dat", (9, 2), 1)
recombinD0_25 = openfile("dNptdpt_PbPb276_D0_c025.txt",(60, 6), 2)
plot(aliceD0[:,0],aliceD0[:,1],y_errorD0,recombinD0_25,'orange','red','Alice 0-5% ',"recombination 0-5%")

plt.legend()
plt.show()
#========================Jpsi========================

plt.title('J/psi_2.76 y=2.5~4')
recombinJpsi = openfile("dNptdpt_PbPb276_Jpsi_c30.txt", (60, 6), 2)
aliceJpsi = openfile("data_Jpsi_276_30.dat", (13, 4), 1)
plot(aliceJpsi[:,0],aliceJpsi[:,2]*10**(-3),aliceJpsi[:,3]*10**(-3),recombinJpsi,"purple","blue","Alice 20-40% ",'recombination 20-40% ')

y_errorJpsi = np.array([0.001544,0.000649333,0.0004824,0.000288571,0.000178222,0.000114909,5.63077E-05,3.57333E-05,2.30588E-05,1.45263E-05,8.95238E-06,6.78261E-06,1.28571E-06])/2/np.pi
aliceJpsi25 = openfile("data_Jpsi_276 (1).dat",(13, 2),1)
recombinJpsi25 = openfile("dNptdpt_PbPb276_Jpsi_c025.txt",(60, 6),2)
plot(aliceJpsi25[:,0],aliceJpsi25[:,1],y_errorJpsi,recombinJpsi25,'orange','red','Alice 0-5% ',"recombination 0-5%")
plt.legend()
plt.show()


#=======================DS=============================
plt.title('Ds_2.76 y=-0.8~0.8')
recombinDS = openfile("dNptdpt_PbPb276_Ds_c35.txt", (60, 6), 2)
aliceDS = openfile("data_Ds_276_35.txt", (2, 4), 1)
plt.ylim([10**-12,10**1])

plot(aliceDS[:,0],aliceDS[:,2],np.array([np.abs(aliceDS[:,2]-aliceDS[:,3]),aliceDS[:,2]+aliceDS[:,3]]),recombinDS,"purple","blue","Alice 30-40% ",'recombination 20-50% ')

y_errorDS = np.array([0.00284,0.000281429,0.000021])/2/np.pi
aliceDs25 = openfile("data_Ds_276.dat",(3, 2),1)
recombinDS25 = openfile("dNptdpt_PbPb276_Ds_c025.txt",(60, 6),2)


plot(aliceDs25[:,0],aliceDs25[:,1],np.array([np.abs(aliceDs25[:,1]-y_errorDS ),aliceDs25[:,1]+y_errorDS ]),recombinDS25,'orange','red','Alice 0-10% ',"recombination 0-5%")
plt.legend()
plt.show()