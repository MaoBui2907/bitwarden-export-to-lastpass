import csv
from tqdm import tqdm
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--src", default="inp.csv")
parser.add_argument("--dest", default="out.csv")

args = parser.parse_args()

src_headers = ["folder", "favorite", "type", "name", "notes", "fields",
               "login_uri", "login_username", "login_password", "login_totp"]

items = []
with open(args.src, 'r') as f:
    csv_reader = csv.reader(f, delimiter=",")
    line = 0
    for row in tqdm(csv_reader):
        if line == 0:
            src_headers = row
            line += 1
        else:
            item = dict()
            for i in range(len(src_headers)):
                item[src_headers[i]] = row[i]
            items.append(item)
            line += 1

dest_headers = ["url", "username", "password",
                "extra", "name", "grouping", "fav"]

with open(args.dest, 'w') as f:
    csv_writer = csv.writer(f, delimiter=",")
    csv_writer.writerow(dest_headers)
    for item in tqdm(items):
        row = [item.get("login_uri"), item.get("login_username"),
               item.get("login_password"), "", item.get("name"), "Imported", 0]
        csv_writer.writerow(row)