'''Mengakses file
fungsi open() => filename,mode
mode yang sering digunakan
1. r - read (default) membuka file dgn mode baca
2. a - append membuka file dgn mode tambah konten
3. w - write dengan menulis'''

from asyncore import read



file = open('C:\Reza\Kuliah\Semester 1\Algo\\file teks.txt', "r") #Untuk Membuka file
listtest = [] #List kosong untuk menambahkan strung didalam file 
for i in file : #Looping berguna untuk memasukkan string yang berada dalam file ke dalam list kosong
    listtest.append(i)
print(listtest)
x1 = 'Matakuliah favoritnya adalah "Algo"\n'
x2 = 'Mereka selalu semangat dan hebat'
listtest.pop(2) #Menghapus string yang tidak digunakan untuk mereplace dengang string yang baru kedalam list
listtest.append(x1)
listtest.append(x2) #Menambahkan string baru yang diminta
print(listtest)

file = open('C:\Reza\Kuliah\Semester 1\Algo\\file teks.txt', "w") #Melakukan overwrite agar dapat di inputkan isi yang baru

file = open('C:\Reza\Kuliah\Semester 1\Algo\\file teks.txt', "a") #Menggunakan method append untuk menambakan isi kedalam file yang telah kosong
for i in listtest : #Membuat perulangan agar semua isi dari list diatas dimasukkan kedalam file yang kosong
    file.write(i) 
file.close() #CLose untuk menutup file