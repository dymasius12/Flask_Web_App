from website import create_app
# The reason we can do this because we put __init__.py in our folder making it a python package
app = create_app()

# Only if we want this file that we will execute thhis file
if __name__ == '__main__':
    app.run(debug=True)
    