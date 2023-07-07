from source.hh_api import HHApi
from utils import save_employers_to_db, save_vacancies_to_db
from config import config
from source.db_manager import DBManager


def main() -> None:
    hh = HHApi()
    employers_data: list = hh.get_employers()
    vacancies_data: list = hh.get_vacancies()
    params_db = config()
    save_employers_to_db(employers_data, params=params_db)
    save_vacancies_to_db(vacancies_data, params=params_db)
    dbm = DBManager()
    print(dbm.get_all_vacancies())
    print(dbm.get_vacancies_with_higher_salary())
    print(dbm.get_vacancies_with_key_word(key_word='Менеджер по продажам'))
    print(dbm.get_avg_salary())
    print(dbm.get_companies_and_vacancies_count())
    dbm.disconnect()


if __name__ == '__main__':
    main()
