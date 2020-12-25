import sqlite3
class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        '''
        by username retrieve User.
        '''

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor() 
        query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(query,(username,))
        row = result.fetchone()

        if row:
            #user = cls(row[0], row[1], row[2])
            user = cls(*row) # *row = set of positional args

        else:
            user = None

        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        '''
        by _id retrieve User.
        '''
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor() 
        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query,(_id,))
        row = result.fetchone()

        if row:
            #user = cls(row[0], row[1], row[2])
            user = cls(*row) # *row = set of positional args

        else:
            row = None

        connection.close()
        return user

