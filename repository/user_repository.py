from models.user import User
import csv
import databaseConector

class UserRepository:
    def create(self, user:User):
        # with open('./repository/user.csv', "a") as csvfile:
        #     writer = csv.writer(csvfile, delimiter=',')
        #     writer.writerow([user.id, user.name, user.document, user.password])
        # return user
        connection = databaseConector.mysqlconnection("xxx", "xxx", "xxxx", "xxx")
        query = '''
            INSERT INTO user (Name, Document, Password)
            VALUES ({name}, {document}, {password}) 
        '''.format(name = str(user.name), document = str(user.document), password = str(user.password))
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        return user

    
    def get(self, document):
        with open('./repository/user.csv', "r") as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                if len(row) > 0 and row[2] == document:
                    return row
        return []