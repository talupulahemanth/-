import sqlite3

# Function to query menu items based on user preferences and allergen filtering
def query_menu_items(database_path, dish_type, category, allergens_to_avoid):
    # Connect to the SQLite database
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    # Construct the SQL query to fetch menu items with the specified dish type and category
    if category.lower() == 'all':
        sql_query = "SELECT name, type, category FROM dishes WHERE type = ?"
        query_params = [dish_type]
    else:
        sql_query = "SELECT name, type, category FROM dishes WHERE type = ? AND category = ?"
        query_params = [dish_type, category]

    # Execute the SQL query
    cursor.execute(sql_query, tuple(query_params))
    results = cursor.fetchall()

    # Filter out menu items with allergens the user wants to avoid
    filtered_results = []
    for item in results:
        dish_name = item[0]

        # Fetch allergens associated with the dish
        cursor.execute("SELECT a.name FROM dish_allergens da JOIN allergens a ON da.allergen_id = a.id WHERE da.dish_id = (SELECT id FROM dishes WHERE name = ?)", (dish_name,))
        allergens_associated_with_dish = set(a[0] for a in cursor.fetchall())

        # Check if any of the user-specified allergens are associated with the dish
        if not allergens_associated_with_dish.intersection(allergens_to_avoid):
            filtered_results.append(item)

    # Close the database connection
    conn.close()

    return filtered_results

# Define the path to your SQLite database file
database_path = r'C:\Users\heman\OneDrive - University of Hertfordshire\HOTEL_BASED_AI_CHATBOT_PROJECT\hotel-based-ai-chatbot\Hotel Database\sqlite-tools-win32-x86-3430200\savoy.database.db'

while True:
    # Get user preferences (dish type, category, and allergens)
    user_dish_type = input("Enter dish type (Veg/Non-Veg): ").strip().title()  # Convert to title case
    user_category = input("Enter category (or 'all' for all categories): ").strip().title()  # Convert to title case
    user_allergens = input("Enter allergens to avoid (comma-separated), or 'none': ").strip().lower().split(",")

    if "none" in user_allergens:
        user_allergens = set()
    else:
        user_allergens = set(user_allergens)

    # Call the query function
    menu_items = query_menu_items(database_path, user_dish_type, user_category, user_allergens)

    if menu_items:
        # Display the results
        print("Recommended Menu Items:")
        for item in menu_items:
            print("Dish:", item[0])
            print("Type:", item[1])
            print("Category:", item[2])
            print("\n")
        break
    else:
        print("No matching menu items. Please try again.")
