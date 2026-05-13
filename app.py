from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Flask Demo App</h1>
    <p>Navigate to the <strong>test</strong> route and begin the assignment</p>
    """

@app.route("/test")
def test():
    data = requests.get("https://jsonplaceholder.typicode.com/todos/")
    return data.json()


@app.route("/patch")
def patch():

    """
    BEGIN THE PATCHES IN THIS FUNCTION
    PRINT THE DATA TYPES OF ALL THE ATTRIBUTES
    CHANGE THE TYPE OF USER-ID TO FLOAT FROM INTEGER
    AND RETURN THE NEW JSON AS RESPONSE
    :return:
    """
    data = requests.get("https://jsonplaceholder.typicode.com/todos/")
    # BEGIN THE ASSIGNMENT FROM HERE
    todos = data.json()
    for todo in todos:
        print(f"Original userId type: {type(todo['userId'])}")
        todo['userId'] = float(todo['userId'])
        print(f"Converted userId type: {type(todo['userId'])}")

    
    return todos


if __name__ == "__main__":
    app.run(debug=True)
