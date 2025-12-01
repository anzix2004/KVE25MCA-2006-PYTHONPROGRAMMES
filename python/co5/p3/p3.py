import csv

# --- Step 1: Write Data to CSV ---
with open("data.csv", "w", newline='') as f:
    w = csv.writer(f)
    w.writerow(["Name", "Age"])
    w.writerow(["Aju", 22])
    w.writerow(["Remya", 25])

# --- Step 2: Read All Data ---
with open("data.csv", "r") as f:
    reader = csv.reader(f)
    
    for row in reader:
        print(row)