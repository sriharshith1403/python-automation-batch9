import json
import csv

def save_to_json (filename,data):
    with open (filename, "w", encoding= "utf-8") as f:
        json.dump(data,f,indent=4)

def save_to_csv(filename,data):
    with open(filename,"w",newline="", encoding="utf-8") as f:
        fieldnames = ["id","name","email"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for row in data :
            filtered_row ={key: row[key] for key in fieldnames}
            writer.writerow(filtered_row)


