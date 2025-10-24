from faker import Faker
import random
#object creation
fake = Faker()

#Function to create random user details
def random_user():
    return {
        'name': fake.name(),
        'email': fake.safe_email(),
        'address': fake.address(),
        'age': random.randint(18, 80),
    }

def random_query_params(n=3):
    return {fake.word(): fake.word() for _ in range(n)}

def random_uuid():
    return fake.uuid4()
