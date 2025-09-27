import pandas as pd
import sqlite3

def main():
    # Read sqlite query results into a pandas DataFrame
    conn = sqlite3.connect("social_media.db")
    
    ## this connection could be any other, such as mysql.
    df = pd.read_sql_query("SELECT * FROM users ", conn) 

    # Verify that result of SQL query is stored in the dataframe
    print(df)
    result = df.query(f'age == {df["age"].max()}')
    print(result)
    
    ## Replace the table with a new content by adding full_name field.
    df['full_name'] = df['name'].str.capitalize() + ', ' + df['surname'].str.capitalize()
    df.to_sql('users', 
              con=conn, 
              if_exists="replace", 
              index=False)
    print(df)
    
    conn.close()

if __name__ == '__main__':
    main()