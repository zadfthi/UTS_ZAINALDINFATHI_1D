inputanBb = 0
inputanTb = 0


inputanBb = float(input('Masukkan Berat Badan (Kg): '))
inputanTb = float(input('Masukkan Tinggi Badan (M): '))

hasilTimbang = inputanBb % inputanTb

if hasilTimbang < 18.5:
    tipe = hasilTimbang < 18.5
    print('Berat Badan Kurang')

elif 18.5 <= hasilTimbang < 24.9 :

        tipe = 18.5 <= hasilTimbang < 24.9 
        print('Berat Badan Normal')

elif 25 <= hasilTimbang < 29.9 :
        tipe = 25 <= hasilTimbang < 29.9 
        print('Berat Badan Kelebihan')

elif hasilTimbang >= 30:
        tipe = hasilTimbang >= 30 
        print('Anda Obesitas.')

print(f'Berat Badan : {inputanBb}')
print(f'Tinggi Badan : {inputanTb}')
print(f'Nilai BMI anda : {hasilTimbang}')
print(f'Kategori BMI : {tipe}')