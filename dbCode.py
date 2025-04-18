# check the slides for information to add to this - from labs 

# dbCode.py

import pymysql
import cred as creds

def get_all_movies():
    conn = pymysql.connect(
        host=creds.host,
        user=creds.user,
        password=creds.password,
        db=creds.db,
        #cursorclass=pymysql.cursors.DictCursor
    )
    return conn

def execute_query(query, args=()):
    cur = get_all_movies().cursor(pymysql.cursors.DictCursor)
    cur.execute(query, args)
    rows = cur.fetchall()
    cur.close()
    return rows

def get_movie_genres():
    query = "SELECT genre_name " \
            "FROM genre " \
            "ORDER BY genre_name;"
    return execute_query(query)

def show_me_movies():
    query = "SELECT m.title, " \
        " GROUP_CONCAT(g.genre_name ORDER BY g.genre_name SEPARATOR ', ') AS genre, " \
        " CONCAT('$', FORMAT(m.budget, 0)) AS budget, " \
        " CONCAT('$', FORMAT(m.revenue, 0)) AS revenue, " \
        " ROUND(m.popularity,0) AS popularity, " \
        " m.overview " \
        " FROM movie m " \
        " JOIN movie_genres mg " \
        " ON m.movie_id = mg.movie_id " \
        " JOIN genre g " \
        " ON mg.genre_id = g.genre_id " \
        " GROUP BY m.movie_id, m.title, m.budget, " \
        " m.revenue, m.popularity, m.overview " \
        " ORDER BY m.popularity DESC;" 
    return execute_query(query)


import boto3

# Set up DynamoDB connection (assuming same region and table name)
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('Users')  

# show me all the uesrs in our system with access
def get_all_users():
    response = table.scan()
    items = response.get('Items', [])
    
    # Convert items to a list of [username, DOB] for template rendering
    users_list = []
    for item in items:
        username = item.get('Username', 'N/A')
        dob = item.get('DOB', 'N/A')
        users_list.append([username, dob])
    
    return users_list

# prove to me that the user you just entered exists
def get_user(username):
    response = table.get_item(Key={'Username': username})
    return response.get('Item')

# check does your username exist already?
def user_exists(username):
    response = table.get_item(Key={'Username': username})
    return 'Item' in response

# add in the user to the system so they can get access
def add_user_to_dynamo(username, dob):
    table.put_item(
        Item={
            'Username': username,
            'DOB': dob
        }
    )

# delete the user with the username you added
def delete_user_from_dynamo(username):
    table.delete_item(Key={'Username': username})

# using the username you entered you can change DOB
def update_user_dob(username, dob):
    table.update_item(
        Key={'Username': username},
        UpdateExpression='SET DOB = :d',
        ExpressionAttributeValues={':d': dob}
    )

# show me all the genres i can pick from
def get_all_genres():
    query = "SELECT genre_id, genre_name" \
            " FROM genre " \
            " ORDER BY genre_name;"
    return execute_query(query)

# show me the top 25 movies by the genre picked by the user
def get_top_movies_by_genre(genre_id):
    query = """
    SELECT 
        m.title, 
        g.genre_name, 
        CONCAT('$', FORMAT(m.budget, 0)) AS budget, 
        CONCAT('$', FORMAT(m.revenue, 0)) AS revenue, 
        ROUND(m.popularity,0) AS popularity, 
        m.overview 
    FROM movie m
    JOIN movie_genres mg ON m.movie_id = mg.movie_id
    JOIN genre g ON mg.genre_id = g.genre_id
    WHERE g.genre_id = %s
    ORDER BY m.popularity DESC
    LIMIT 25;
    """
    return execute_query(query, (genre_id,))




if __name__ == "__main__":
    get_all_movies()



