import numpy as np
import matplotlib.pyplot as plt

def openfile(filename,size):
    file = open(filename, "r")  # 以只读模式打开文件
    lines = file.readlines()  # 获取所有行并保存到lines列表中
    data = []
    row = 1 # 指定开始读取的行
    for line in lines[row - 1:]:  # 读取指定的所有行
        line = line.strip('\n')  # 去掉换行符
        line = line.split()
        data = np.hstack((data,line)) # 去掉空格
    file.close()  # 关闭文件
    data = np.array(data,dtype=float)
    data = np.reshape(data,size)
    return data

dataDS = openfile("err of dNptdpt_PbPb502_Ds_c40.txt", (30))
dataD0 = openfile("err of dNptdpt_PbPb502_D0_c40.txt", (30))
dataJpsi = openfile("err of dNptdpt_PbPb502_Jpsi_c30.txt",(30))

dataDS = np.sqrt(dataDS/9)
dataD0 = np.sqrt(dataD0/22)
dataJpsi = np.sqrt(dataJpsi/8)
#dataDS = (np.max(dataDS)-dataDS)/(np.max(dataDS)-np.min(dataDS))
#dataD0 = (np.max(dataD0)-dataD0)/(np.max(dataD0)-np.min(dataD0))

"""set an initial error"""
minerr = 100
times = 0

dataerr = dataDS +dataD0 + dataJpsi
CCi = np.argmin(dataerr)
CC = 0.000001 + (1+CCi) * 0.02
print(CC)

"""for plot"""
def plot():
    i = np.arange(30)
    cc = 0.000001 + ( 1 + i )*0.02

    plt.plot(cc,dataerr)
    plt.scatter(cc[CCi],dataerr[CCi],marker = '*',lw = 2, color ='red')
    plt.yscale('log')
    plt.title('err due to CC ( errD0 + errDS )')
    plt.legend()
    plt.show()

    plt.plot(cc, dataD0)
    plt.scatter(cc[CCi], dataD0[CCi], marker='*', lw=2, color='red')
    plt.title('err of D0 5.02TeV c=40%')
    plt.legend()
    plt.show()

    plt.plot(cc, dataDS)
    plt.scatter(cc[CCi], dataDS[CCi], marker='*', lw=2, color='red')
    plt.title('err of DS 5.02TeV c=40%')
    plt.legend()
    plt.show()

    plt.plot(cc, dataJpsi)
    plt.scatter(cc[CCi], dataJpsi[CCi], marker='*', lw=2, color='red')
    plt.title('err of Jpsi 5.02TeV c=30%')
    plt.legend()
    plt.show()




plot()

