import matplotlib.pyplot as plt
import requests
import os


def loadData(path):
    #readfile blpck
    f = open(path, 'r')
    data = f.readlines()
    f.close()
    for i in range(len(data)):
        data[i] = data[i].strip()
    #download block
    
    for i in data:
        req = requests.get(f"https://www.uniprot.org/uniprot/{i}.fasta")
        f = open('dwnload\\'+i+'.fasta', 'w')
        f.write(req.text)
        f.close()

def stats():
    #getfiles block
    data = []
    f = os.listdir(os.getcwd()+'\\dwnload')
    for i in f:
        f1 = open('dwnload\\'+i, 'r')
        data.append(len(f1.read().strip()))
        f1.close()
    #make grafik
    plt.plot(data)
    plt.show()

def main():
    path = input('выберите файл  (дефолт - list.txt)    ')
    if path == '':
        path = 'list.txt'

    s = input('вывести статистику? (y/n) (дефолт - y)       ')
    if s in ['N', 'n', 'no', 'NO', "н", "Н"] == True:
        s = False
    else:
        s = True
    
    loadData(path)
    if s == True:
        stats()

main()