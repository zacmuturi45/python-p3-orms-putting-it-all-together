import sqlite3

CONN = sqlite3.connect('lib/dogs.db')
CURSOR = CONN.cursor()

class Dog:
    
    def __init__(self, name, breed):
        self.id = None
        self.name = name
        self.breed = breed
    
    @classmethod
    def create_table(cls):

        CURSOR.execute("CREATE TABLE IF NOT EXISTS dogs(id INTEGER PRIMARY KEY, name TEXT, breed TEXT)")
        CONN.commit()
    
    @classmethod
    def drop_table(self):

        CURSOR.execute("DROP TABLE IF EXISTS dogs")
    
    def save(self):
        cursor = CURSOR
        cursor.execute(
            'INSERT INTO dogs(name, breed) VALUES(?, ?)',
            (self.name, self.breed)
        )
        self.id = cursor.execute("SELECT last_insert_rowid() FROM dogs").fetchone()[0]
    
    @classmethod
    def create(cls, name, breed):
        dog = Dog(name, breed)
        dog.save()
        CONN.commit()
        return dog
    
    @classmethod
    def new_from_db(cls, row):
        dog = cls(row[1], row[2])
        dog.id = row[0]
        return dog
    
    @classmethod
    def get_all(cls):
        sql = 'SELECT * FROM dogs'
        all = CURSOR.execute(sql).fetchall()
        cls.all = [cls.new_from_db(row) for row in all]
        return cls.all
        
    
    @classmethod
    def find_by_name(cls, name):
        sql = 'SELECT * FROM dogs WHERE name = ? LIMIT 1'
        dog = CURSOR.execute(sql, (name,)).fetchone()
        if dog != None:
            return cls.new_from_db(dog)
        else:
            return None
    
    @classmethod
    def find_by_id(cls, id):
        sql = 'SELECT * FROM dogs WHERE id = ? LIMIT 1'
        dog = CURSOR.execute(sql, (id,)).fetchone()
        return cls.new_from_db(dog)

    @classmethod
    def find_or_create_by(cls, name, breed):
        cool = cls.create(name, breed)
        return cool
    
    @classmethod
    def update(cls):
        sql = 'UPDATE dogs SET name = "joseph" WHERE name = "joey"'
        CURSOR.execute(sql)
        CONN.commit()
        


        

