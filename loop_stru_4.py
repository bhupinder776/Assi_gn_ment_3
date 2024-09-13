def main():
    # Initialize an empty list to store city names
    cities = []

    # Collect city names from the user
    for i in range(5):
        city = input(f"Enter the name of city {i + 1}: ")
        cities.append(city)

    # Print the names of the cities, one per line
    print("The cities you entered are:")
    for city in cities:
        print(city)

# Call the main function to run the program
main()
