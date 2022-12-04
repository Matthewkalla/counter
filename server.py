from flask import Flask, render_template,  request, redirect, session  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = 'not really secret'


@app.route('/')          # The "@" decorator associates this route with the function immediately following;
def count_times():
    print("got post info")
    session['Click'] += 1
    if 'Click' in session:
        print('key exists!')
    else:
        print("key 'key_name' does NOT exist")


    return render_template("index.html", click=session['Click'])
    # Return the string 'Hello World!' as a response

@app.route('/count')
def add_two():
    session['Click'] += 1
    return redirect('/')


@app.route('/destroy_session')
def erase_cookies():
    session['Click'] = 0
    return redirect('/')
# @app.route('/destroy_session')
# def

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True, host='0.0.0.0')    # Run the app in debug mode.