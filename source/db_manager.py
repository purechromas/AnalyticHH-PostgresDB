import psycopg2
from config import config


class DBManager:
    _params = config()
    _connection = psycopg2.connect(dbname='hh', **_params)

    def _cursor_execute(self, query: str) -> list:
        """Making cursor, witch can execute SELECT querys and return objects"""
        with self._connection.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()

    def disconnect(self):
        """Disconnecting from database"""
        self._connection.close()

    def get_companies_and_vacancies_count(self):
        query = """
            SELECT name, open_vacancies
            FROM employers
        """

        return self._cursor_execute(query=query)

    def get_all_vacancies(self):
        query = """
            SELECT e.name, v.name, v.salary_from, v.url
            FROM vacancies v 
            JOIN employers e ON v.employer_id = e.id
        """

        return self._cursor_execute(query=query)

    def get_avg_salary(self):
        query = """
            SELECT ROUND(AVG(salary_from)), ROUND(AVG(salary_to))
            FROM vacancies;
        """

        return self._cursor_execute(query=query)

    def get_vacancies_with_higher_salary(self):
        query = """
            SELECT *
            FROM vacancies
            WHERE salary_from > (SELECT AVG(salary_from) FROM vacancies)
        """

        return self._cursor_execute(query=query)

    def get_vacancies_with_key_word(self, key_word: str):
        query = f"""
            SELECT *
            FROM vacancies
            WHERE name LIKE '%{key_word}%'
        """

        return self._cursor_execute(query=query)
