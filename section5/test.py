import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor() # select, start, store. Excecute the querys and store the results.

# CREATE table -------------------------------------------------------------------------------
create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

# insert data - one by time

# INSERT data --------------------------------------------------------------------------------

# create INSERT query.
insert_query = "INSERT INTO users VALUES (?, ?, ?)"

# create user to insert
user = (1, 'rodrigo', 'asdf')

# execute query
cursor.execute(insert_query, user)


# create many users to insert
users = [
        (2, 'chris', 'asdfg'),
        (3, 'camy', 'asdfgh'),
        (4, 'bosco', 'asdfghi')
    ]

# insert many
cursor.executemany(insert_query, users)

# QUERY data -----------------------------------------------------------------------------------
select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)

# COMMIT changes ------------------------------------------------------------------------------
connection.commit()

# CLOSE db ------------------------------------------------------------------------------------
connection.close()
