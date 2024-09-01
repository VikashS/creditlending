import pandas as pd
from faker import Faker

# Initialize Faker to generate fake data
fake = Faker()

# Number of rows of fake data to generate
num_rows = 100

# Generating the data
data = {
    "Profile_ID": [i + 1 for i in range(num_rows)],
    "Name": [fake.name() for _ in range(num_rows)],
    "Address": [fake.address().replace("\n", ", ") for _ in range(num_rows)],
    "Phone Number": [fake.phone_number() for _ in range(num_rows)],
    "Email": [fake.email() for _ in range(num_rows)],
    "Corporate Information": [f"{fake.job()}, {fake.random_int(min=1, max=30)} years" for _ in range(num_rows)],
    "Company Name": [fake.company() for _ in range(num_rows)]
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Saving to a CSV file
df.to_csv("../data/Clients2.csv", index=False)

print("data has been generated.")
