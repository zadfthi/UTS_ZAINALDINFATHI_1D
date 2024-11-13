while True:
    inputTahun = int(input('Masukkan Tahun: '))

    if inputTahun % 400 == 0 or inputTahun % 4 == 0 and 100 != 0:
        print(f'Tahun {inputTahun} merupakan Tahun Kabiset')

    else:
        print(f'Tahun {inputTahun} bukan Tahun Kabiset')