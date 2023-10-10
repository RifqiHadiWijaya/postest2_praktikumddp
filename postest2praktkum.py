import os

os.system('cls')


from prettytable import PrettyTable
peralatanDapur = PrettyTable()

peralatanDapur.field_names = ['no barang', 'nama barang', 'harga']
peralatanDapur.add_row([1, 'sendok', 1000])
peralatanDapur.add_row([2, 'garpu', 1500])
peralatanDapur.add_row([3, 'pisau', 15000])
peralatanDapur.add_row([4, 'kompor', 200000])
peralatanDapur.add_row([5, 'panci', 90000])

hargaperalatan = [1000, 1500, 15000, 200000, 90000]

#memilih role admin atau pelanggan jika 1 admin dan jika 2 pelanggan
while True:
    print('pilih role 1. admin')
    print('           2. pelanggan')
    print('           3. keluar dari program')

    pilihrole = int(input('masukkan kode : '))
    if pilihrole == 1:
        print('selamat datang admin')
        username = input('masukkan username anda : ')

        #untuk read
        def read():
            print(peralatanDapur)
        read()

        #untuk create
        def create():
            tambahno = int(input('tambahkan no barang : '))
            tambahbarang = input('tambahkan barang baru : ')
            tambahharga = int(input('tambahkan harga barang : '))
            peralatanDapur.add_row([tambahno, tambahbarang, tambahharga])
            print(peralatanDapur)
            print('peralatan telah ditambahkan')

        #untuk update
        def update():
            tambahno = int(input('tambahkan no barang : '))
            tambahbarang = input('tambahkan barang baru : ')
            tambahharga = int(input('tambahkan harga barang : '))
            peralatanDapur.add_row([tambahno, tambahbarang, tambahharga])
            print(peralatanDapur)
            print('peralatan telah diupdate')

        # untuk delete
        def delete():
            delete = int(input("Masukkan index yang akan dihapus: "))
            peralatanDapur.del_row(delete)
            print('peralatan telah dihapus, silahkan ke menu read untuk melihatnya')


        #menu-menu admin
        def alat():
            while True:
                print('1. read')
                print('2. create')
                print('3. update')
                print('4. delete')
                print('5. exit')
            
                kode = input('pilih kode apa yang ingin anda lakukan : ')
                if kode == '1':
                    read()
                elif kode == '2':
                    create()
                elif kode == '3':
                    update()
                elif kode == '4':
                    delete()
                elif kode == '5':
                    break
        alat()
        

    #sebagai pelanggan
    elif pilihrole == 2:
        
        print('selamat belanja')
        nama_pelanggan = input("Masukkan Nama Pelanggan: ")
        print(peralatanDapur)
        kode_peralatan = int(input("Masukkan Kode Peralatan: "))
        

        if kode_peralatan == 1:
            peralatan = (peralatanDapur[0])
            print(f"harga yang harus anda bayar : {hargaperalatan[0]}")
        elif kode_peralatan == 2:
            peralatan = (peralatanDapur[1])
            print(f"harga yang harus anda bayar : {hargaperalatan[1]}")
        elif kode_peralatan == 3 :
            peralatan = (peralatanDapur[2])
            print(f"harga yang harus anda bayar : {hargaperalatan[2]}")
        elif kode_peralatan == 4:
            peralatan = (peralatanDapur[3])
            print(f"harga yang harus anda bayar : {hargaperalatan[3]}")
        elif kode_peralatan == 5:
            peralatan = (peralatanDapur[4])
            print(f"harga yang harus anda bayar : {hargaperalatan[4]}")
        else:
            print('kode yang anda masukkan salah')

    #untuk keluar dari program
    elif pilihrole == 3:
        break