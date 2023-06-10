import csv
f = open("csv_file.csv")
csv_f = csv.reader(f)
for row in csv_f:
    name,phone,role = row
    print("Name : {}, Phone :{}, Role:{}".format(name,phone,role))

f.close()

