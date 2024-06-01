from texttable import Texttable

List_Product = []


def Add_Product(new_product):
  # Cek id agar tidak ada duplikasi
  for product in List_Product:
    if new_product[0] == product[0]:
      return False

  # Jika tidak ada id yang sama
  List_Product.append(new_product)
  return True


def Get_All_Product():
  return List_Product


def Get_Product_By_ID(id_product):
  for product in List_Product:
    if id_product == product[0]:
      return product

  return None


def Update_Product(updated_product):
  for product in List_Product:
    if updated_product[0] == product[0]:
      product[1] = updated_product[1]
      product[2] = updated_product[2]
      return True

  return False


def Delete_Product(id_product):
  for product in List_Product:
    if id_product == product[0]:
      List_Product.remove(product)
      return True

  return False


def View_Get_All_Data():
  print("""==================================
DATA PRODUK
""")

  table_data = [["No", "ID", "Nama", "Harga"]]

  for index, product in enumerate(List_Product):
    table_data.append([(index + 1), *product])

  table = Texttable()
  table.set_cols_align(["r", "l", "l", "r"])
  table.add_rows(table_data)
  print(table.draw())
  print("")


def View_Get_Product_By_ID():
  print("""==================================
DATA PRODUK BERDASARKAN ID
""")

  id_product = input("ID Product : ")
  r_product = Get_Product_By_ID(id_product)

  if r_product == None:
    print("ID Tidak Ditemukan")
    print("")
    return

  table_data = [["ID", "Nama", "Harga"]]
  table_data.append(r_product)

  table = Texttable()
  table.set_cols_align(["l", "l", "r"])
  table.add_rows(table_data)
  print(table.draw())
  print("")


def View_Add_Product():
  print("""==================================
TAMBAH DATA PRODUK
""")

  id_product = input("ID Product : ")
  name = input("Nama : ")
  price = int(input("Harga : "))

  res = Add_Product([id_product, name, price])

  if res:
    print("Berhasil Menambahkan Data Produk")
  else:
    print("Gagal Menambahkan Data Produk")


def View_Update_Product():
  print("""==================================
UBAH DATA PRODUK
""")

  id_product = input("ID Product : ")
  name = input("Nama : ")
  price = int(input("Harga : "))

  res = Update_Product([id_product, name, price])

  if res:
    print("Berhasil Mengubah Data Produk")
  else:
    print("Gagal Mengubah Data Produk")


def View_Delete_Product():
  print("""==================================
HAPUS DATA PRODUK
""")

  id_product = input("ID Product : ")

  res = Delete_Product(id_product)

  if res:
    print("Berhasil Menghapus Data Produk")
  else:
    print("Gagal Menghapus Data Produk")


def View_Menu():
  print("""==================================
WARUNG ABC - CRUD DATA PRODUK

1. Lihat Semua Data
2. Lihat Data Berdasarkan ID
3. Tambah Data
4. Ubah Data
5. Hapus Data

0. Keluar
""")

  menu = int(input("Menu >> "))

  if menu == 1:
    View_Get_All_Data()
  elif menu == 2:
    View_Get_Product_By_ID()
  elif menu == 3:
    View_Add_Product()
  elif menu == 4:
    View_Update_Product()
  elif menu == 5:
    View_Delete_Product()
  elif menu == 0:
    return True
  else:
    print("Inputan Tidak Valid")

  return False


def main():
  while True:
    exit_status = View_Menu()
    if exit_status:
      break


main()
