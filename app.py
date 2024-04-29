from website import create_app

app = create_app()


if __name__ == '__main__':
    app.run(debug=True)  # debug=True means that every time we change the code, the server get a refresh,
    # so we don't have to rerun manually
