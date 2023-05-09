from models.user import User
import csv

class UserRepository:
    def create(self, user:User):
        with open('./repository/user.csv', "a") as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow([user.id, user.name, user.document, user.password])
        return user
    
    def get(self, document):
        with open('./repository/user.csv', "r") as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                if len(row) > 0 and row[2] == document:
                    return row
        return []