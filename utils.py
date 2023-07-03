import psycopg2


def save_employers_to_db(employers: list, params: dict) -> None:
    conn = psycopg2.connect(dbname="hh", **params)

    with conn.cursor() as cur:
        query = """
        INSERT INTO employers (id, name, url, open_vacancies) VALUES (%s, %s, %s, %s)
        """

        for employer in employers:
            cur.execute(query, (employer.get("id"), employer.get("name"), employer.get("url"), employer.get("open_vacancies")))

    conn.commit()
    conn.close()


def save_vacancies_to_db(vacancies: list, params: dict) -> None:
    conn = psycopg2.connect(dbname="hh", **params)

    with conn.cursor() as cur:
        query = """
        INSERT INTO  vacancies (name, salary_from, salary_to, area, employer_id, url) VALUES (%s, %s, %s, %s, %s, %s)
        """

        for vacancy in vacancies:
            cur.execute(query,
                        (vacancy.get("name"),
                         vacancy.get("salary_from"),
                         vacancy.get("salary_to"),
                         vacancy.get("area"),
                         vacancy.get("employer_id"),
                         vacancy.get("url")))

    conn.commit()
    conn.close()
