import csv
import random
import string

# List of dummy names
names = ['John', 'Jane', 'Bob', 'Alice', 'Tom', 'Emma', 'Michael', 'Sophia', 'David', 'Olivia']

# List of dummy email domains
email_domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'example.com']

# Function to generate a random string for profile_pic URL
def random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

# Open a CSV file for writing
with open('users.csv', 'w', newline='') as csvfile:
    fieldnames = ['name', 'profile_pic', 'email']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write the header row
    writer.writeheader()

    # Generate and write dummy data
    for i in range(100):
        name = random.choice(names)
        profile_pic = f"https://example.com/profile_pics/{random_string(10)}.jpg"
        email = f"{name.lower()}@{random.choice(email_domains)}"

        writer.writerow({'name': name, 'profile_pic': profile_pic, 'email': email})

print("Dummy data generated in users.csv")