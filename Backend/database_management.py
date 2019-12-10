import redis

from google.cloud import storage

buckets = [
        "submitted-photos-1",
        "submitted-photos-2"
        ]

databases = [
        "10.107.212.83",
        "10.168.194.187"
        ]

def determine_shard(value):
    """
    determines the physical shard that the data belongs to
    """
    return value % 2

def connect_to_db(host, port):
    """
    connect to the database given the host and the port
    """
    r = redis.Redis(host=host, port=port, db=0)
    return r

def add_photo_data(database, photo_hash):
    if database.exists(photo_hash) == 1:
        print("exists")
        print(database.hgetall(photo_hash))
    else:
        database.hmset(photo_hash,{ "approved": "False", "Date": "Today", "image": "N/A"})
        print(database.hget(photo_hash))


def edit_photo_approval(database, photo_hash, value):
    """
    Set the approval of the photo
    """
    if database.exists(photo_hash) == 1:
        print("exists")
        print(database.hgetall(photo_hash))
        database.hmset(photo_hash, {"approved": value})
        print(database.hgetall(photo_hash))
    else:
        print("does not exist")

def photo_exists(database, photo_hash):
    """
    checks if the photo exists in the database
    """
    return database.exists(photo_hash)

def add_photo_to_user(database, photo_hash, user):
    return database.lpush(user, photo_hash)

if __name__ == "__main__":
    r = connect_to_db("10.107.212.83", 6379)
    #add_photo_data(r, "10")
    #edit_photo_approval(r, "10", "TRUE")
    list_buckets()
