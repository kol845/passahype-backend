from app import app
if __name__ == '__main__':
    # app.run(host='0.0.0.0',port=80, debug=True) # This line caused privelege error, so i removed it
    app.run(debug=True)