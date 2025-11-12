import json
from pathlib import Path
from time import sleep
def hapus_game():

    lokasiFile = Path(__file__).resolve()
    folderSekarang = lokasiFile.parent
    folderUtama = folderSekarang.parent
    path_json = folderUtama / "DATA" / "DATA_GAME.json"

    try:
        with open(path_json, "r") as file:
            fileGame = json.load(file)
    except FileNotFoundError:
        print("File DATA_GAME.json tidak ditemukan.")
        return

    print("\nDaftar ID Game:")
    for id_game in fileGame:
        print(f"- {id_game} ({fileGame[id_game]['judul_game']})")

    id_hapus = input("\nMasukkan ID game yang ingin dihapus: ").upper()

    if id_hapus in fileGame:
        konfirmasi = input(f"Apakah kamu yakin ingin menghapus '{fileGame[id_hapus]['judul_game']}'? (y/n): ").lower()
        if konfirmasi == "y":
            del fileGame[id_hapus]
            with open(path_json, "w") as file:
                json.dump(fileGame, file, indent=4)
                sleep(2)
            print("Game berhasil dihapus.")
        else:
            sleep(2)
            print("Penghapusan dibatalkan.")
    else:
        sleep(2)
        print("ID game tidak ditemukan.")