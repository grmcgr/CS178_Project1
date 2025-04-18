
from flask import Flask, render_template, request, redirect, url_for, flash, session
import cred
from dbCode import * # import helper functions from dbCode.py
import pymysql
import dbCode


app = Flask(__name__)
app.secret_key = 'grace-mcgrane'

# site that is the default
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        username = request.form['Username']
        dob = request.form['DOB']
        # does your username and DOB match our database? 
        # now you can look at the movies database
        if dbCode.user_exists(username):
            user = dbCode.get_user(username)
            if user.get('DOB') == dob:
                session['user'] = username
                flash(f'Welcome back, {username}!', 'success')
                return redirect(url_for('movies'))  # GO TO MOVIE PAGE
            # if your entry doesn't match, try again
            else:
                flash('DOB does not match our records.', 'danger')
                return redirect(url_for('home'))
        # if you're not in it, then add yourself
        else:
            flash('User not found. Please create an account.', 'warning')
            return redirect(url_for('add_user'))     
    return render_template('home.html') 

# add user to gain access
@app.route('/add-user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        # Extract form data
        username = request.form['Username']
        dob = request.form['DOB']
        
        # Check for duplicate username
        if dbCode.user_exists(username):
            flash('Username already taken. Please choose another one.', 'danger')
            return redirect(url_for('add_user'))
        
        # Process the data (e.g., add it to a database)
        dbCode.add_user_to_dynamo(username, dob)
        
        flash('User added successfully!', 'success')  # 'success' is a category; makes a green banner at the top
        # Redirect to home page or another page upon successful submission
        return redirect(url_for('home'))
    else:
        # Render the form page if the request method is GET
        return render_template('add_user.html')

# delete a username
@app.route('/delete-user', methods=['GET', 'POST'])
def delete_user():
    if request.method == 'POST':
        # Extract form data
        username = request.form['Username']
        
        # Process the data (e.g., delete it to a database)
        dbCode.delete_user_from_dynamo(username)
        # For now, let's just print it to the console
        print("User to delete:", username)
        
        flash('User deleted successfully!', 'warning')  # 'success' is a category; makes a green banner at the top
        # Redirect to home page or another page upon successful submission
        return redirect(url_for('home'))
    else:
        # Render the form page if the request method is GET
        return render_template('delete_user.html')

# enter in a username and then update the DOB
@app.route('/update-user', methods=['GET', 'POST'])
def update_user():
    if request.method == 'POST':
        username = request.form['Username']
        new_dob = request.form['DOB']

        if dbCode.user_exists(username):
            dbCode.update_user_dob(username, new_dob)
            flash(f'DOB updated for {username}', 'success')
        else:
            flash(f'User {username} not found.', 'danger')

        return redirect(url_for('update_user'))
    else:
        return render_template('update_user.html')

# show me all the users in the list
@app.route('/display-users')
def display_users():
    # hard code a value to the users_list;
    users_list = dbCode.get_all_users()
    # note that this could have been a result from an SQL query :) 
    return render_template('display_users.html', users=users_list)

# show me genres of movies 
@app.route('/movies')
def movies():
    data = dbCode.get_movie_genres()
    return render_template('movies.html', results=data)

# make special queries and list them 
# make an html for each of them

# show me all movies ranked by popularity
@app.route('/movies/all-movies')
def show_all_movies():
    data = dbCode.show_me_movies()
    return render_template('all_movies.html', results=data)

# Fetch all genres for the dropdown list
# data returns in a table after you pick and submit
@app.route('/movies/select-genre', methods=['GET', 'POST'])
def select_genre():
    genres = dbCode.get_all_genres()
    selected_genre = None
    movies = []

    if request.method == 'POST':
        selected_genre = request.form.get('genre')
        movies = dbCode.get_top_movies_by_genre(selected_genre)

    return render_template(
        'select_genre.html',
        genres=genres,
        movies=movies,
        selected_genre=int(selected_genre) if selected_genre else None
    )


# these two lines of code should always be the last in the file
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

