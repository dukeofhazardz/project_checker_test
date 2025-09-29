# Step 1: Create a set of visited cities
visited_cities = {"New York", "London", "Tokyo", "Paris", "Sydney"}

# Step 2: Try adding a duplicate city
visited_cities.add("Tokyo")

# Step 3: Add a new city
visited_cities.add("Berlin")

# Step 4: Remove an existing city
visited_cities.discard("Sydney")

# Step 5: Print all visited cities
print("Cities visited:")

for city in visited_cities:
    print(city)

# Step 6: Check if 'Paris' is in the set
if "Paris" in visited_cities:
    print("\nYou've been to Paris!")
else:
    print("\nYou haven't been to Paris yet.")