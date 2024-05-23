import csv
import json

def lecture_fihcier(fihcier_json):
    with open(fichier_json, "r") as f:
        data = json.load(f)

    return data

def ecriture_fichier(data, fichier_csv):
    with open(fichier_csv, "w", newline="") as f_2:
        ecriture_csv = csv.writer(f_2)
        ecriture_csv.writerow(["reel", "imaginaire"])

        for nbr_complexe in data:
            ecriture_csv.writerow(nbr_complexe)
