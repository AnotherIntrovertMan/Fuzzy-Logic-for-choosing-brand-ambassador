#fuzzy logic tupro 3 AI
#NaufalZahidYogaP_1301170345
#IF4106

#defuzzifikasi model sugeno

import csv
import numpy

def convert_csv(file):#convert csv kedalam bentuk array
    num = []
    follower = []
    eng = []
    with open(file) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        next(csvReader)
        for row in csvReader:
            num.append(int(row[0]))
            follower.append(int(row[1]))
            eng.append(float(row[2]))
    return num,follower,eng

def fuzz_low_foll(x):#value fuzzifikasi follower(low)
    if (x>40000):
        hasil = 0
    elif (x<=20000):
        hasil = 1
    else:
        hasil = (40000-x)/(40000-20000)
    return hasil

def fuzz_high_foll(x):#value fuzzifikasi follower(high)
    if (x>55000):
        hasil = 1
    elif (x<=35000):
        hasil = 0
    else:
        hasil = (x-35000)/(55000-35000)
    return hasil

def fuzz_mid_foll(x):#value fuzzifikasi follower(mid)
    if (x>60000 or x<=22000):
        hasil = 0
    elif (26000<x and x<=52000):
        hasil = 1
    elif(41000<x and x<=55000):
        hasil = (x-22000)/(26000-22000)
    else:
        hasil = (60000-x)/(60000-52000)
    return hasil

def fuzz_low_eng(x):#value fuzzifikasi engagement(low)
    if (x>4):
        hasil = 0
    elif (x<=2):
        hasil = 1
    else:
        hasil = (4-x)/(4-2)
    return hasil

def fuzz_high_eng(x):#value fuzzifikasi engagement(high)
    if (x>5):
        hasil = 1
    elif (x<=2.8):
        hasil = 0
    else:
        hasil = (x-2.8)/(5-2.8)
    return hasil

def fuzz_mid_eng(x):#value fuzzifikasi engagement(mid)
    if (x>3.9 or x<=2):
        hasil = 0
    elif (2.7<x and x<=3.5):
        hasil = 1
    elif(2<x and x<=2.7):
        hasil = (x-2)/(2.7-2)
    else:
        hasil = (3.9-x)/(3.9-3.5)
    return hasil

def pick_lowest(a,b): #ambil bilangan terendah
    hasil = 0
    if (a > b):
        hasil = b
    elif (a < b):
        hasil = a
    else:
        hasil = a
    return hasil

def pick_highest(arr = []):
    hasil = 0
    if (arr[0]>=arr[1] and arr[0]>=arr[2]):
        hasil = arr[0]
    elif (arr[1]>=arr[0] and arr[1]>=arr[2]):
        hasil = arr[1]
    elif (arr[2]>=arr[0] and arr[2]>=arr[1]):
        hasil = arr[2]
    return hasil

def fuzzifikasi_func(arr_foll = [], arr_eng = []): #input array follower dan engagemet
    fuzz_follower = []
    fuzz_engagement = []

    fuzzi_foll = [] #fuzzifikasi follower (low,mid,high)
    fuzzi_eng = [] #fuzzifikasi membership (low,mid,high)

    arr_follower = arr_foll.copy() #isi array follower
    arr_engagement = arr_eng.copy() #isi array engagement


    i = 0
    while (i < 100): #fuzzifikasi follower
        fuzz_follower.append(fuzz_low_foll(arr_follower[i]))
        fuzz_follower.append(fuzz_mid_foll(arr_follower[i]))
        fuzz_follower.append(fuzz_high_foll(arr_follower[i]))
        fuzzi_foll.append(fuzz_follower)
        fuzz_follower = []
        i = i + 1

    i = 0
    while (i < 100): #fuzzifikasi engagement
        fuzz_engagement.append(fuzz_low_eng(arr_engagement[i]))
        fuzz_engagement.append(fuzz_mid_eng(arr_engagement[i]))
        fuzz_engagement.append(fuzz_high_eng(arr_engagement[i]))
        fuzzi_eng.append(fuzz_engagement)
        fuzz_engagement = []
        i = i + 1

    hasil_fuzzifikasi = [fuzzi_foll,fuzzi_eng]

    #return hasil fuzzifikasi semua data
    return hasil_fuzzifikasi

def inferensi_func(arr_fuzzifikasi = []): #input hasil fuzzifikasi semua data
    fuzz_follower = arr_fuzzifikasi[0] #fuzzifikasi follower
    fuzz_engagement = arr_fuzzifikasi[1] #fuzzifikasi engagement

    arr_inferensi = [] #menyimpan inferensi data ke-n, indeks array berjumlah 9, 3x3 = 9
    hasil_inferensi = [] #hasil akhir inferensi semua data

    i = 0
    while (i < 100):
        j = 0
        while (j < 3):
            k = 0
            while (k < 3):
                lowest1 = fuzz_follower[i][j]
                lowest2 = fuzz_engagement[i][k]
                lowest = pick_lowest(lowest1,lowest2)
                arr_inferensi.append(lowest)
                k = k + 1
            j = j + 1
        hasil_inferensi.append(arr_inferensi)
        arr_inferensi = []
        i = i + 1

    return hasil_inferensi


def hasil_inferensi_func(arr_inferensi = []): #input array inferensi, output hasil inferensi semua data
    inf = []
    hasil_inf = []

    i = 0
    while (i < 100):
        acc = arr_inferensi[i][5], arr_inferensi[i][7], arr_inferensi[i][8] #accept
        high_acc = pick_highest(acc)
        inf.append(high_acc)
        cons = arr_inferensi[i][2], arr_inferensi[i][4], arr_inferensi[i][6] #consider
        high_cons = pick_highest(cons)
        inf.append(high_cons)
        rej = arr_inferensi[i][0], arr_inferensi[i][1], arr_inferensi[i][3] #reject
        high_rej = pick_highest(rej)
        inf.append(high_rej)

        hasil_inf.append(inf)
        inf = []
        i = i + 1
    return hasil_inf #hasil inferense = [accept,consider,reject]

def defuzzifikasi_func(arr_inf = []): #menggunakan model sugeno, input hasil inferensi setiap data
    hasil_def = []

    i = 0
    while (i < 100):
        output_def = ((arr_inf[i][0] * 80)+(arr_inf[i][1] * 60)+(arr_inf[i][2]*40)) / (arr_inf[i][0] + arr_inf[i][1] + arr_inf[i][2])
        hasil_def.append(output_def)
        i = i + 1
    return hasil_def

def sort_defuzzifikasi(arr_def = [],nomor = []): #sorting hasil defuzzi utk ambil 20 influencers terbaik
    arr = arr_def.copy() #array defuzzifikasi
    num = nomor.copy() #array nomor baris dalam tabel influencers

    for i in range(1,len(arr)):
        curr = arr[i]
        curr_num = num[i]
        j = i-1
        while j >= 0 and curr > arr[j]:
            arr[j + 1] = arr[j]
            num[j+1] = num[j]
            j -= 1
        arr[j + 1] = curr
        num[j+1] = curr_num
    return arr,num

if __name__ == "__main__":
    inf = convert_csv("influencers.csv")#convert csv kedalam array, baca file
    print("-------------------------------------------------------------------------------------------")
    print(inf)
    nomor = inf[0]
    follower = inf[1]
    engagement = inf[2]
    print("nomor :",nomor) #array untuk nomor
    print("follower :",follower) #array untuk follower
    print("engagement rate",engagement) #array untuk engagement rate
    print("---------------------------------Output per-fungsi------------------------------------------")
    fuzzifikasi = fuzzifikasi_func(follower,engagement)
    print("Hasil Fuzzifikasi: ",fuzzifikasi)
    inferensi = inferensi_func(fuzzifikasi)
    print("Inferensi: ",inferensi)
    hasil_inferensi = hasil_inferensi_func(inferensi)
    print("Hasil Inferensi [Accept,Consider,Rejected]: ",hasil_inferensi)
    defuzzifikasi = defuzzifikasi_func(hasil_inferensi)
    print("Hasil Defuzzifikasi: ",defuzzifikasi)
    sorting_def = sort_defuzzifikasi(defuzzifikasi,nomor)
    terbaik = sorting_def[0]
    nomor = sorting_def[1] #nomor record terpilih
    print("Hasil defuzzifikasi 20 data terpilih: ",terbaik[0:20])
    print("Nomor record: ",nomor[0:20])

    arr_nomor = nomor[0:20] #20 influencers terbaik
    conv = numpy.asarray(arr_nomor)
    numpy.savetxt("choosen.csv",conv.astype(int),delimiter=",",fmt="%i") #convert array 20 influencers terbaik kedalam csv
