def app():
    return True

def apple():
    app()
    return app()

print(apple())