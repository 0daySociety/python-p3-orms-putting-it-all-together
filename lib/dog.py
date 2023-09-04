import sqlite3

CONN = sqlite3.connect('dogs.db')
CURSOR = CONN.cursor()

class Dog:
    all=[]
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed
        self.id=None

    @classmethod
    def create_table(cls):
        sql='''
              CREATE TABLE IF NOT EXISTS dogs(
              id INTEGER PRIMARY KEY ,
              name TEXT,
              breed TEXT
              
              )
            '''  
        return CURSOR.execute(sql)
    @classmethod
    def drop_table(cls):
        sql ="""
              DROP TABLE IF EXISTS dogs  

         """
        return CURSOR.execute(sql)
    
    def save(self):
        sql= '''
               INSERT INTO dogs(name, breed)
                 VALUES(?,?)

           '''
        CURSOR.execute(sql,(self.name,self.breed))
        # CONN.commit()
        self.id=CURSOR.execute("SELECT last_insert_rowid() FROM dogs").fetchone()[0]

    @classmethod
    def create(cls,name,dreed):
        dog=Dog(name,dreed)
        dog.save() 
        return dog   
    
    @classmethod
    def new_from_db(cls,db_data):
        dog=cls(name=db_data[1],breed=db_data[2])
        if db_data[0] !=None:
            id=db_data[0]
        return dog    
    

    @classmethod
    def get_all(cls):
        sql='''
              SELECT * FROM dogs 
        '''
        all=CURSOR.execute(sql).fetchall()
        return all

    @classmethod
    def find_by_name(cls,name):
        sql="""
        SELECT * 
        FROM dogs 
        WHERE name=?
        LIMIT 1
        
        """
        dog =CURSOR.execute(sql,(name,)).fetchone
        return dog
    
    @classmethod
    def find_by_id(cls,id):
        sql ="""
            SELECT * FROM dogs 
            WHERE id=?
            LIMIT 1
            
            """
        dog_id=CURSOR.execute(sql,(id,)).fetchone()
        return dog_id




 


Dog.create_table()
pet =Dog.create("puppy","rotwailer")
pet2 =Dog.create("scobby","rotwailer")
finder =pet2.find_by_name("puppy")

print(pet.id)
print(finder)


# dogs=CURSOR.execute("SELECT * FROM dogs")
# for dog in dogs:
#     print(dog)




# dogs=CURSOR.execute("SELECT * FROM dogs")
# for dog in dogs:
#     print(dog)










    

    
    
