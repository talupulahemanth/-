import sqlite3

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn

def get_user_preferences():
    print("Welcome to our Smart Menu Recommendation System!")
    print("Veg = Vegetarian Non-Veg = Non Vegetarian")

    # Get user preferences for dish type, dish category, and allergens
    dish_type = input("Kindly choose the dish type (Veg/Non-Veg): ").strip().capitalize()
    dish_category = input("Kindly choose the category (Bites/Mains/Sides/Desserts): ").strip().capitalize()
    allergens_input = input("Kindly mention your allergens which should be eliminated or enter 'none' if none: ").strip().lower()
    allergens = [allergen.strip() for allergen in allergens_input.split(',')]

    return dish_type, dish_category, allergens

def get_recommendations(conn, dish_type, dish_category, allergens):
    # Build the basic query without allergens
    query = f"""
        SELECT dish_name, dish_type, dish_category
        FROM items
        WHERE LOWER(dish_type) = LOWER('{dish_type}') AND LOWER(dish_category) = LOWER('{dish_category}')
    """

    # If allergens are specified, exclude dishes containing those allergens
    if allergens and allergens[0] != 'none':
        allergen_conditions = " AND ".join([f"LOWER(allergens) NOT LIKE '%{allergen}%'" for allergen in allergens])
        query += f" AND ({allergen_conditions})"

    try:
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows
    except sqlite3.Error as e:
        print(e)
    return []


def main():
    database = r"C:\Users\heman\OneDrive - University of Hertfordshire\HOTEL_BASED_AI_CHATBOT_PROJECT\hotel-based-ai-chatbot\Hotel Database\sqlite-tools-win32-x86-3430200\savoy.database.db"

    while True:
        # Get user preferences
        dish_type, dish_category, allergens = get_user_preferences()

        # Create a database connection
        conn = create_connection(database)
        if conn:
            # Get recommendations
            recommendations = get_recommendations(conn, dish_type, dish_category, allergens)

            # Print recommendations
            print("\nRecommended Dishes:")
            if recommendations:
                for dish in recommendations:
                    print(dish)
            else:
                print("No recommended dishes found based on your preferences.")
            conn.close()

if __name__ == '__main__':
    main()
