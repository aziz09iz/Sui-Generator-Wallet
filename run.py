from bip_utils import Bip39SeedGenerator, Bip44Coins, Bip44
from bech32 import bech32_encode, convertbits
from mnemonic import Mnemonic
import pandas as pd

class Suiwallet:
    def __init__(self, mnemonic: str, password='') -> None:
        self.mnemonic: str = mnemonic.strip()
        self.password = password
        self.pk_prefix = 'suiprivkey'
        self.ed25519_schema = '00'

    def get_address_pk(self, pk_with_prefix=True):
        seed_bytes = Bip39SeedGenerator(self.mnemonic).Generate(self.password)
        bip44_mst_ctx = Bip44.FromSeed(seed_bytes, Bip44Coins.SUI).DeriveDefaultPath()
        address = bip44_mst_ctx.PublicKey().ToAddress()
        pk = bip44_mst_ctx.PrivateKey().Raw().ToHex()

        if pk_with_prefix:
            pk_bytes_with_schema = bytes.fromhex(f'{self.ed25519_schema}{pk}')
            pk_bit_arr = convertbits(pk_bytes_with_schema, 8, 5)
            pk = bech32_encode(self.pk_prefix, pk_bit_arr)

        return address, pk

def display_welcome_message():
    logo = r"""
██     ██ ██ ███    ██ ███████ ███    ██ ██ ██████  
██     ██ ██ ████   ██ ██      ████   ██ ██ ██   ██ 
██  █  ██ ██ ██ ██  ██ ███████ ██ ██  ██ ██ ██████  
██ ███ ██ ██ ██  ██ ██      ██ ██  ██ ██ ██ ██      
 ███ ███  ██ ██   ████ ███████ ██   ████ ██ ██      
"""
    print(logo)
    print("SuiWallet Generator")
    print("Join our Telegram channel: https://t.me/winsnip")

if __name__ == '__main__':
    display_welcome_message()
    while True:
        try:
            num_wallets = int(input("Berapa banyak wallet yang ingin dihasilkan? "))
            if num_wallets <= 0:
                print("Harap masukkan angka positif.")
                continue
            break
        except ValueError:
            print("Silakan masukkan angka yang valid.")

    wallet_data = []
    with open("wallet.txt", 'a', encoding='utf-8') as f, open("suipk.txt", 'a', encoding='utf-8') as pk_file:
        for i in range(num_wallets):
            m = Mnemonic(language='english')
            mnc = m.generate()
            sw = Suiwallet(mnc)
            add, pk = sw.get_address_pk()
            print(f'mnemonic: {mnc}')
            print(f'address: {add}')
            print(f'pk: {pk}')
            f.write(f'{add},{pk},{mnc}\n')
            pk_file.write(f'"{pk}",\n')

            wallet_data.append({'Mnemonic': mnc, 'Address': add, 'Private Key': pk})

    df = pd.DataFrame(wallet_data)
    try:
        df.to_excel("wallets.xlsx", index=False)
        print("Data wallet berhasil diekspor ke wallets.xlsx.")
    except ImportError:
        df.to_csv("wallets.csv", index=False)
        print("openpyxl tidak ditemukan, data wallet diekspor ke wallets.csv.")
