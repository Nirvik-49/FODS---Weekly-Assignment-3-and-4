def find_city_index(cities, city_to_search):
    """Return the index of the city in the list, or a message if not found."""
    
    if city_to_search in cities:
        return cities.index(city_to_search)
    else:
        return f"The city '{city_to_search}' is not available in the list."

# Test the function

if __name__ == "__main__":

    # Example list of cities
    
    city_list = ["New York", "Kathmandu", "Mumbai", "Sydney", "London"]
    
    # City to search for
    search_city = "Kathmandu"
    
    # Find the index of the city
    result = find_city_index(city_list, search_city)
    
    # Display the result
    print(result)

    # Test with a city that is not in the list
    search_city_not_found = "Tokyo"
    result_not_found = find_city_index(city_list, search_city_not_found)
    print(result_not_found)
