from datetime import datetime
nama_pelanggan = input("nama pelanggan : ")
alamat = input("alamat : ")
no_telp = input("no telp : ")
tanggal = datetime.now()
harga_per_barang = input("harga per barang : ")
print("="*10)
print(f"Nama : {nama_pelanggan}")
print(f"Alamat : {alamat}")
print(f"no telp : {no_telp}")
print(f"tanggal : {tanggal}")
print (f"harga/barang : {harga_per_barang}")