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
def plot(ptalice,xerr,y1,yerr,recomb,color1,color2,title1,title2):
    plt.scatter(ptalice,y1,color=color1,label=title1)
    plt.plot(recomb[:,0],recomb[:,5],color=color2,label=title2,lw = 3)
    plt.errorbar(ptalice,y1,xerr = xerr,yerr = yerr,color=color1,fmt='o', capsize=3)
    plt.yscale('log')
    plt.xlabel('pt')
    plt.ylabel('dN/2pipTdpT')

def plot_D0():
#=======================D0==============================
    plt.title('D0_5.02y=-0.5~0.5')
    recombD040 = openfile("dNptdpt_PbPb502_D0_c40.txt", (60, 6), 2)
    aliceD040 = openfile("alice D0 502 40.txt",(22,4),1)
    recombD00 = openfile("dNptdpt_PbPb502_D0_c025_2.txt",(60,6),2)
    aliceD00  = openfile("alice D0 502 5.txt",(22,4),1)
    plot(aliceD040[0:19,0],aliceD040[0:19,1],aliceD040[0:19,2],aliceD040[0:19,3],recombD040[0:50,:],"purple","blue",'Alice 30-50% ','recombination 30-50%')
    plot(aliceD00[0:19,0],aliceD00[0:19,1],aliceD00[0:19,2],aliceD00[0:19,3],recombD00[:,:],'orange','red','Alice 0-5% ',"recombination 0-10%")
    plt.legend()
    plt.show()

#========================Jpsi========================
def plot_Jpsi():
    plt.title('J/psi_5.02 y=-0.9~0.9')
    recombinJpsi40 = openfile("dNptdpt_PbPb502_Jpsi_c40.txt", (60, 6), 2)
    aliceJpsi40 = openfile("alice Jpsi 502 30.txt", (6, 4), 1)
    recombinJpsi0 = openfile("dNptdpt_PbPb502_Jpsi_c025_2.txt",(60,6),2)
    aliceJpsi0 = openfile("alice Jpsi 502 10.txt",(8,4),1)
    plot(aliceJpsi40[:,0],aliceJpsi40[:,1]/2,aliceJpsi40[:,2],aliceJpsi40[:,3],recombinJpsi40[:,:],"purple","blue","Alice 20-40% ",'recombination 20-40% ')
    plot(aliceJpsi0[:,0],aliceJpsi0[:,1]/2,aliceJpsi0[:,2],aliceJpsi0[:,3],recombinJpsi0[:,:],'orange','red','Alice 0-5% ',"recombination 0-5%")
    plt.legend()
    plt.show()

#=======================DS=============================
def plot_DS():
    plt.title('Ds_5.02 y=-0.5~0.5')
    recombinDS40 = openfile("dNptdpt_PbPb502_Ds_c40.txt", (60, 6), 2)
    aliceDS40 = openfile("alice Ds 502 40.txt", (9, 4), 1)
    recombinDS0 = openfile("dNptdpt_PbPb502_Ds_c025_2.txt",(60,6),2)
    aliceDS0 = openfile("alice Ds 502 5.txt",(10,4),1)
    plot(aliceDS40[0:7,0],aliceDS40[0:7,1],aliceDS40[0:7,2],aliceDS40[0:7,3],recombinDS40[0:50,:],"purple","blue","Alice 30-40% ",'recombination 20-50% ')
    plot(aliceDS0[0:7,0],aliceDS0[0:7,1],aliceDS0[0:7,2],aliceDS0[0:7,3],recombinDS0[:,:],"orange","red","Alice 0-5% ",'recombination 0-5%')
    #np.array([np.abs(aliceDS[:,2]-aliceDS[:,3]),aliceDS[:,2]+aliceDS[:,3]])
    plt.legend()
    plt.show()



plot_D0()
plot_Jpsi()
plot_DS()