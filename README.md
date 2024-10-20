# SuiWallet Generator

SuiWallet Generator adalah aplikasi Python yang digunakan untuk menghasilkan wallet Sui berdasarkan mnemonic. Aplikasi ini menggunakan BIP39 dan BIP44 untuk menghasilkan alamat dan kunci privat.

## Fitur

- Menghasilkan beberapa wallet Sui dengan menggunakan mnemonic.
- Mengekspor data wallet ke dalam format Excel atau CSV.
- Menyimpan alamat, kunci privat, dan mnemonic dalam file teks.

## Prasyarat

Sebelum menjalankan aplikasi ini, pastikan Anda telah menginstal:
- Python 3
- pip

Anda juga perlu menginstal beberapa pustaka yang diperlukan. 

## Instalasi

1. **Clone atau Unduh Repositori**:
```bash
git clone https://github.com/winsnip/Sui-Generator-Wallet.git 
cd Sui-Generator-Wallet
```
2. **Install**:
```bash
pip install -r requirements.txt
```
or 

```bash
pip install bip-utils bech32 mnemonic pandas openpyxl
```
3. **Run**:
```bash
python run.py
```
