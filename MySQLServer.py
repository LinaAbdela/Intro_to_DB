import mysql.connector

try:
    # Connect to MySQL server (root with blank password)
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password=''  # blank password
    )

    if connection.is_connected():
        cursor = connection.cursor()

        # Create the database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as e:
    print("Error while connecting to MySQL:", e)

finally:
    # Close cursor and connection safely
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
