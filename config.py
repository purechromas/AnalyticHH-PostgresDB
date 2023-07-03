from configparser import ConfigParser


def config() -> dict:
    parser = ConfigParser()
    parser.read("database.ini")
    items = parser.items("postgresql")
    db = {}
    for item in items:
        db[item[0]] = item[1]
    return db
