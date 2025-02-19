import pandas as pd  # Import pandas

# Step 1: Create sample data
data = {
    "Name": ["John", "Alice", "Bob", "Emma", "David", "Sophia", "Michael", "Olivia", "James", "Emily", 
             "Daniel", "Grace", "Matthew", "Lily", "Joseph", "Ava", "Ethan", "Mia", "William", "Charlotte"],
    "Age": [25, 30, 22, 28, 35, 27, 40, 32, 29, 24, 
            33, 31, 26, 23, 45, 38, 34, 29, 37, 36],
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "San Francisco", "Boston", "Seattle", "Miami", "Denver", "Dallas",
             "Atlanta", "San Diego", "Austin", "Las Vegas", "Philadelphia", "Phoenix", "Portland", "Detroit", "Nashville", "Washington"],
    "Occupation": ["Engineer", "Doctor", "Artist", "Designer", "Manager", "Lawyer", "Teacher", "Nurse", "Architect", "Photographer",
                   "Developer", "Writer", "Data Scientist", "Chef", "Entrepreneur", "Marketing", "Consultant", "Pilot", "Psychologist", "Musician"],
    "Salary": [75000, 95000, 60000, 70000, 85000, 110000, 65000, 72000, 80000, 55000,
               90000, 50000, 97000, 58000, 120000, 67000, 88000, 94000, 75000, 77000]
}

# Step 2: Convert data to a DataFrame
df = pd.DataFrame(data)

# Step 3: Save DataFrame as a CSV file
df.to_csv("data.csv", index=False)

print("CSV file created successfully with more data!")
