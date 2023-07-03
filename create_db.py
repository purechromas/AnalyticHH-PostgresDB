import psycopg2
from psycopg2.errors import DuplicateTable
from config import config

params = config()


def create_database() -> None:
    conn = psycopg2.connect(dbname='postgres', **params)
    conn.autocommit = True
    cur = conn.cursor()

    try:
        cur.execute("DROP DATABASE hh;")
    except Exception as e:
        print(f"DATABASE CAN'T BE DROPPED, SO WE ARE SKIPPING THAT | {e}")
    finally:
        cur.execute('CREATE DATABASE hh;')
        print("DATABASE WAS SUCCESSFULLY CREATED!")


def create_tables():
    conn = psycopg2.connect(dbname='hh', **params)
    conn.autocommit = True
    cur = conn.cursor()

    table_employers = """
                CREATE TABLE employers (
                id VARCHAR(255) PRIMARY KEY,
                name VARCHAR(255) NOT NULL UNIQUE,
                url VARCHAR(255) NOT NULL UNIQUE,
                open_vacancies INT);
                      """

    table_vacancies = """
                CREATE TABLE vacancies (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                salary_from INT,
                salary_to INT,
                area VARCHAR(255),
                employer_id VARCHAR(255) NOT NULL,
                url VARCHAR(255),
                FOREIGN KEY (employer_id) REFERENCES employers(id));
                """

    try:
        cur.execute(table_employers)
        cur.execute(table_vacancies)
        print("TABLES WAS SUCCESSFULLY CREATED!")
    except DuplicateTable as e:
        print("TABLES ALREADY EXIST. SKIPPING TABLE CREATION.")
    except Exception as e:
        print(f"AN ERROR OCCURRED WHILE CREATING THE TABLES: {e}")

    cur.close()
    conn.close()


create_database()
create_tables()
