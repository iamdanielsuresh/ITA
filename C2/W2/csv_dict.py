import csv

with open("software.csv") as software:
    reader = csv.DictReader(software)
    for row in reader:
        print(("{} has {} users").format(row['name'], row['users']))

users = [{"name" : "Ashvin Sibi", "username" : "sibi"}, 
         {"name": "Goutham Manikandan", "username" : "mani"},
         {"name": "Daniel Suresh","username": "dani"}]
keys = ["name", "username"] 
with open("user_info.csv", 'w') as user_info:
    writer = csv.DictWriter(user_info, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)
