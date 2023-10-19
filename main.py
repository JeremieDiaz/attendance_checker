from frontend import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

#run the program here. it is connected to the init.py in the frontend