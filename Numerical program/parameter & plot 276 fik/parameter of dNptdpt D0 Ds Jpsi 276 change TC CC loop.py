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


def quenchJpsi(data,maxerr):
    """this function can transform the dataJpsi to the search condition,
    which means only allow such situations that the data calculated by recombination models is larger tha the experiment data"""
    if data>maxerr:
        result = 1
    else:
        result = 10000000
    return  result

quenchJpsi = np.vectorize(quenchJpsi)


dataDS1 = openfile("err of dNptdpt_PbPb276_Ds_c35.txt", (30,30))
dataD01 = openfile("err of dNptdpt_PbPb276_D0_c40.txt", (30,30))
dataJpsi1 = openfile("err of dNptdpt_PbPb276_Jpsi_c30.txt",(30,30))

dataDS1 = np.sqrt(dataDS1/3)
dataD01 = np.sqrt(dataD01/7)
dataJpsi1 = dataJpsi1/13

dataDS2 = openfile("err of dNptdpt_PbPb276_Ds_c025.txt", (30,30))
dataD02 = openfile("err of dNptdpt_PbPb276_D0_c025.txt", (30,30))
dataJpsi2 = openfile("err of dNptdpt_PbPb276_Jpsi_c025.txt",(30,30))

dataDS2 = np.sqrt(dataDS2/2)
dataD02 = np.sqrt(dataD02/7)
dataJpsi2 = dataJpsi2/13

dataerr1 = dataD01 + dataDS1
dataerr2 = dataD02 + dataDS2



"""set an initial error"""
Jpsierr = 9
times = 0
minerri = 6
for k1 in range(10):
    for k2 in range(10):




        quench1 = quenchJpsi(dataJpsi1,10-minerri)
        quench2 = quenchJpsi(dataJpsi2,10-minerri)
        times += 1

        for i in range(30):
            for j in range(30):
                dataerr =np.reshape(dataerr2[:,j],(30))*np.reshape(quench2[:,j],(30)) + np.reshape(dataerr1[:,i],(30))*np.reshape(quench1[:,i],(30))

                indexi = np.argmin(dataerr)
                #indexi = 24
                if dataerr[indexi]<minerri:
                    print(times)
                    minerri = dataerr[indexi]
                    TCi = indexi
                    CCi1 = i
                    CCi2 = j








CC1 = 0.000001 + (1+CCi1) * 0.05
CC2 = 0.000001 + (1+CCi2) * 0.05
TC = 0.000001 +(TCi +1)* 0.05
print("CC1(30_50) = ",CC1)
print("CC2(0_10) = ",CC2)
print("TC = ",TC)
print("err = ",minerri)
print("recombin / Alice 30 =",dataJpsi1[TCi,CCi1])
print("recombin / Alice 025 =",dataJpsi2[TCi,CCi2])



"""for plot"""

i = np.arange(30)
j = np.arange(30)
cc = 0.000001 + (1 + i) * 0.05
tc = 0.000001 + (j + 1) * 0.05
CC, TC = np.meshgrid(cc, tc)
def plot1():
    plt.pcolor(CC,TC,  np.log(dataerr1))
    plt.colorbar()
    plt.scatter( cc[CCi1],tc[TCi], marker='*', lw=2, color='red')
    plt.title('total err of D0 + Ds + Jpsi 5.02TeV c=30%')
    plt.legend()
    plt.show()

    plt.pcolor(CC,TC,quench1)
    plt.colorbar()
    plt.scatter(cc[CCi1],tc[TCi],marker = '*',lw = 2, color ='red')
    plt.title('err of Jpsi 5.02TeV c=40%')
    plt.legend()
    plt.show()

    plt.pcolor(CC,TC,np.log(dataD01))
    plt.colorbar()
    plt.scatter(cc[CCi1],tc[TCi],marker = '*',lw = 2, color ='red')
    plt.title('err of D0 5.02TeV c=40%')
    plt.legend()
    plt.show()



    plt.pcolor(CC,TC,np.log(dataDS1))
    plt.colorbar()
    plt.scatter(cc[CCi1],tc[TCi],marker = '*',lw = 2, color ='red')
    plt.title('err of Ds 5.02TeV c=40%')
    plt.legend()
    plt.show()

def plot2():
    ############+===============================================
    plt.pcolor(CC, TC, np.log(dataerr2))
    plt.colorbar()
    plt.scatter(cc[CCi2], tc[TCi], marker='*', lw=2, color='red')
    plt.title('total err of D0 + Ds + Jpsi 5.02TeV c=0.25%')
    plt.legend()
    plt.show()

    plt.pcolor(CC,TC,quench2)
    plt.colorbar()
    plt.scatter(cc[CCi2],tc[TCi],marker = '*',lw = 2, color ='red')
    plt.title('err of Jpsi 5.02TeV c=40%')
    plt.legend()
    plt.show()


    plt.pcolor(CC, TC, np.log(dataD02))
    plt.colorbar()
    plt.scatter(cc[CCi2], tc[TCi], marker='*', lw=2, color='red')
    plt.title('err of D0 5.02TeV c=0.25%')
    plt.legend()
    plt.show()

    plt.pcolor(CC, TC, np.log(dataDS2))
    plt.colorbar()
    plt.scatter(cc[CCi2], tc[TCi], marker='*', lw=2, color='red')
    plt.title('err of Ds 5.02TeV c=0.25%')
    plt.legend()
    plt.show()



#plot1()
#plot2()
