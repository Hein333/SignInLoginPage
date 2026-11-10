def app():
    return True

def apple():
    app()
    return app()

print(apple())

database = [('hein@gmail.com', 'Hein', '1234'), 
            ('heinhtet@gmail.com', 'HeinHtet', '1234'), 
            ('htet@gmail.com', 'hein', '333'),
              ('aung@gmail.com', 'htet', '323')]