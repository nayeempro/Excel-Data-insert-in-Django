import pandas as pd
import random

# Sample data
names = ['Nayeem', 'Rahim', 'Karim', 'Ayesha', 'Sabbir', 'Fatima', 'Jamil', 'Rina', 'Tariq', 'Sadia']
cities = ['Dhaka', 'Chattogram', 'Khulna', 'Sylhet', 'Rajshahi', 'Barishal', 'Rangpur']
courses = ['Python', 'Data Science', 'Web Development', 'Machine Learning', 'AI', 'Database', 'Cloud Computing']

# Generate 100 random records
data = []
for _ in range(90):  # 90 unique records
    name = random.choice(names)
    age = random.randint(20, 30)
    city = random.choice(cities)
    course = random.choice(courses)
    price = random.randint(100, 500)
    email = f"{name.lower()}{random.randint(1,100)}@example.com"
    data.append([name, age, city, course, price, email])

# Add some duplicates (10 rows)
duplicates = random.sample(data, 10)
data.extend(duplicates)

# Create DataFrame
df = pd.DataFrame(data, columns=['Name', 'Age', 'City', 'Course', 'Price', 'Email'])

# Shuffle rows
df = df.sample(frac=1).reset_index(drop=True)

print(df.head())  # Show first 15 rows
print(f"\nTotal records: {len(df)}")

# Check duplicates
print("\nDuplicate rows:")
print(df[df.duplicated()])

# duplicates count
dup_num = df.duplicated().sum()
print(f"total duplicates num is : {dup_num}")

df_unique = df.drop_duplicates().reset_index(drop=True)
dup_num_unique = df_unique.duplicated().sum()
print(f"total duplicates num is : {dup_num_unique}")

dup_num_unique.describe()






