import pandas as pd

# Nama file CSV
# file_path = "combined_result2.csv"
file_path = "D:/Semester 7/TA/Dataset/simple-scraping-with-beautifulsoup/combined/combined_results.csv"

# Membaca file CSV
data = pd.read_csv(file_path)

# Menghapus kolom "No" jika ada
# if 'No' in data.columns:
#     data = data.drop(columns=['No'])
#     print("\nKolom 'No' berhasil dihapus.")
# else:
#     print("\nKolom 'No' tidak ditemukan dalam dataset.")

# Menampilkan informasi dataset
print("Informasi Dataset:")
print(data.info())

# Menampilkan beberapa baris pertama
print("\nContoh Data:")
print(data)


