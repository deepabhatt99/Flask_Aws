# Import Flask and other necessary modules
from flask import Flask, render_template, request, redirect, url_for
import re

# Create a Flask app instance
app = Flask(__name__)

# Define a route for the home page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        test_string = request.form['test_string']
        regex_pattern = request.form['regex_pattern']
        
        # Validate the email using regex
        if re.match(regex_pattern, test_string):
            # If the email is valid, redirect to regex.com page
            return redirect(url_for('regex_page'))
        else:
            # If the email is not valid, render the same page with an error message
            error_message = "Invalid email address see if it is @ or .gmail.com is missing"
            return render_template('index.html', error_message=error_message)
    else:
        return render_template('index.html')

# Define a route for the regex.com page
@app.route('/regex_page')
def regex_page():
    # Render the regex.com page template
    return render_template('regex_page.html')

# Define a route for the email validation page
@app.route('/validate_email')
def validate_email_page():
    return render_template('validate_email.html')

@app.route('/validate_email', methods=['POST'])
def validate_email():
    email = request.form['email']
    # Add your email validation logic here using regex or any other method
    # For demonstration purposes, let's check if the email contains '@'
    if '@' 'gmail.com' in email:
        # If the email is valid, redirect to the regex.com page
        return redirect(url_for('regex_page'))
    else:
        # If the email is not valid, render the same page with an error message
        error_message = "Invalid email address see if it is @ or .gmail.com is missing"
        return render_template('validate_email.html', error_message=error_message)

@app.route('/results', methods=['GET', 'POST'])
def results():
    error_message = None
    valid_urls = None

    if request.method == 'POST':
        regex_pattern = request.form['regex_pattern']
        input_urls = request.form['input_urls']

        # Split input URLs by comma and remove any leading or trailing whitespace
        urls_list = [url.strip() for url in input_urls.split(',')]

        # Compile the regex pattern
        pattern = re.compile(regex_pattern)

        # Filter valid URLs based on the regex pattern
        valid_urls = [url for url in urls_list if pattern.match(url)]

        if not valid_urls:
            error_message = 'No valid URLs found.'

    return render_template('regex_page.html', valid_urls=valid_urls, error_message=error_message)




if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
