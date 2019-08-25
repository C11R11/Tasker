from jobs_api import flask_app 

if __name__ == "__main__":
    print ("#### runApi main ####")
    flask_app.run(debug=True, host='0.0.0.0')