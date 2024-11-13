jumlahBarang = int(input('Masukkan Jumlah Barang: '))
storeBarang = 0

for i in range(1, jumlahBarang + 1):
    jumlahBarang = 0
    hargaBarang = int(input(f'Masukkan harga Barang ke {i}: '))
    storeBarang += hargaBarang
    penggabungan = storeBarang + jumlahBarang 

print(f'Total Belanjaan : Rp.{penggabungan}')

    
