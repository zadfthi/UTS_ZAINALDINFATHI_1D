import modul_soal_1

while True:
    print('Silahkan Pilih Aritmatika yang Ingin Dilakukan!')
    print('')
    print('1. Penjumlahan ')
    print('2. Pengurangan')
    print('3. Perkalian ')
    print('4. Keluar Program')

    pilih = str(input('Masukkan Operasi Aritmatik yang ingin dilakukan! (1/2/3): '))

    a = int(input('Masukkan Nilai Pertama : '))
    b = int(input('Masukkan Nilai Kedua : '))

    if pilih == '1':
        modul_soal_1.penjumlahan(a,b)

    elif pilih == '2':
        modul_soal_1.pengurangan(a,b)

    elif pilih == '3':
        modul_soal_1.perkalian(a,b)

    else:
        break

print('Terimakasih telah menggunakan program')