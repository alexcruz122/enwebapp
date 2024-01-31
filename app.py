from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

# Function to save data to a text file
def save_to_file(amount, category):
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    with open('records.txt', 'a') as file:
        file.write(f"Timestamp: {timestamp}, Amount: {amount}, Category: {category}\n")

# Function to read records from the text file
def read_records():
    try:
        with open('records.txt', 'r') as file:
            records = file.readlines()
        return records
    except FileNotFoundError:
        return []

@app.route('/')
def index():
    # Read records when loading the page
    records = read_records()
    return render_template('index.html', records=records)

@app.route('/submit_form', methods=['POST'])
def submit_form():
    amount = request.form.get('amount')
    category = request.form.get('category')

    # Save data to a file
    save_to_file(amount, category)

    # Read updated records
    records = read_records()

    # Render the updated records on the same page
    return render_template('index.html', records=records)

if __name__ == '__main__':
    app.run(debug=True)
