import csv
import pandas as pd

def read_csv_with_csv_module(file_path):
    """Membaca file CSV menggunakan modul csv"""
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)  # Menampilkan setiap baris sebagai dictionary

def read_csv_with_pandas(file_path):
    """Membaca file CSV menggunakan pandas"""
    df = pd.read_csv(file_path)
    print(df.head())  # Menampilkan beberapa baris pertama

# Contoh penggunaan
file_path = 'data.csv'  # Ganti dengan path file CSV yang sesuai
read_csv_with_csv_module(file_path)
read_csv_with_pandas(file_path)
