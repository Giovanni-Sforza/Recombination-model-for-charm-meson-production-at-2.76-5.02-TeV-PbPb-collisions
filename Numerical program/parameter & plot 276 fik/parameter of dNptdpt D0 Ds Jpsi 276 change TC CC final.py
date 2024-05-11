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



N = 20
dataDS1 = openfile("err of dNptdpt_PbPb276_Ds_c35 final.txt", (N,N))
dataD01 = openfile("err of dNptdpt_PbPb276_D0_c40 final.txt", (N,N))


#dataDS1 = np.sqrt(dataDS1/(dataDS1[0,0]-100))
#dataD01 = np.sqrt(dataD01/(dataD01[0,0]-100))


dataDS2 = openfile("err of dNptdpt_PbPb276_Ds_c025 final.txt", (N,N))
dataD02 = openfile("err of dNptdpt_PbPb276_D0_c025 final.txt", (N,N))


#dataDS2 = np.sqrt(dataDS2/(dataDS2[N,N]-100))
#dataD02 = np.sqrt(dataD02/(dataD02[N,N]-100))


"""set an initial error"""
minerr = 500
times = 0

dataerr1 = dataD01 + dataDS1
dataerr2 = dataD02 + dataDS2


for i in range(N):
    for j in range(N):
        dataerr =np.reshape(dataerr2[:,j],(N))+ np.reshape(dataerr1[:,i],(N))

        indexi = np.argmin(dataerr)
        #indexi = 24
        if dataerr[indexi]<minerr:
            times +=1
            print(indexi,times)
            minerr = dataerr[indexi]
            TCi = indexi
            CCi1 = i
            CCi2 = j


CC1 =  0.25+ (1+CCi1) * 0.02
CC2 = 0.5 + (1+CCi2) * 0.02
TC = 0.5 +(TCi +1)* 0.02

print("CC1(30_50) = ",CC1)
print("CC2(0_10) = ",CC2)
print("TC = ",TC)
print("err = ",minerr)
#print("recombin / Alice 10 =",dataJpsi1[TCi,CCi1])
#print("recombin / Alice 025 =",dataJpsi2[TCi,CCi2])

"""for plot"""

i = np.arange(N)
j = np.arange(N)
cc = 0 + (1 + i) * 0.1
tc = 0.5+ (j + 1) * 0.1
CC, TC = np.meshgrid(cc, tc)
def plot1():
    plt.pcolor(CC,TC,  np.log(dataerr1))
    plt.colorbar()
    plt.scatter( cc[CCi1],tc[TCi], marker='*', lw=2, color='red')
    plt.title('total err of D0 + Ds + Jpsi 5.02TeV c=30%')
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



plot1()
plot2()
