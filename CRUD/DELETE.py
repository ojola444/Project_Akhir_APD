import json
from pathlib import Path

def hapus_game():
    # Tentukan path ke file JSON
    lokasiFile = Path(__file__).resolve()
    folderSekarang = lokasiFile.parent
    folderUtama = folderSekarang.parent
    path_json = folderUtama / "DATA" / "DATA_GAME.json"

    # Load data game
    try:
        with open(path_json, "r") as file:
            fileGame = json.load(file)
    except FileNotFoundError:
        print("File DATA_GAME.json tidak ditemukan.")
        return

    # Tampilkan daftar ID game yang tersedia
    print("\nDaftar ID Game:")
    for id_game in fileGame:
        print(f"- {id_game} ({fileGame[id_game]['judul_game']})")

    # Input ID game yang ingin dihapus
    id_hapus = input("\nMasukkan ID game yang ingin dihapus: ").upper()

    # Validasi dan konfirmasi
    if id_hapus in fileGame:
        konfirmasi = input(f"Apakah kamu yakin ingin menghapus '{fileGame[id_hapus]['judul_game']}'? (y/n): ").lower()
        if konfirmasi == "y":
            del fileGame[id_hapus]
            with open(path_json, "w") as file:
                json.dump(fileGame, file, indent=4)
            print("Game berhasil dihapus.")
        else:
            print("Penghapusan dibatalkan.")
    else:
        print("ID game tidak ditemukan.")