import csv
import os
import qrcode

def main():
    os.makedirs("qr_codes", exist_ok=True)
    with open("urls.csv", newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    for row in rows:
        slug, name, url = row["slug"], row["name"], row["url"]
        img = qrcode.make(url, box_size=10, border=2)
        safe_name = name.replace(" ", "_")
        out_path = os.path.join("qr_codes", f"{slug}_{safe_name}.png")
        img.save(out_path)

    print(f"Generated {len(rows)} QR codes in ./qr_codes")

if __name__ == "__main__":
    main()
