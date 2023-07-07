import requests


class HHApi:
    vacancies_url = "https://api.hh.ru/vacancies?"
    employers_url = "https://api.hh.ru/employers/"
    employers = {"YANDEX": 1740,
                 "VK": 15478,
                 "SBERBANK": 829010,
                 "ALFABANK": 80,
                 "ASTON": 6093775,
                 "LANIT": 733,
                 "CARPRICE": 1532045,
                 "USETECH": 681672,
                 "EVROPLAN": 1329,
                 "KOTELOV": 843093}

    @classmethod
    def get_vacancies(cls) -> list[dict[str:int or str or None]]:
        """Parsing HH.RU for specific vacancies by employer_id"""
        params = {"only_with_salary": True, "per_page": 100}
        result = []

        for employer_id in cls.employers.values():
            url = f"https://api.hh.ru/vacancies?employer_id={employer_id}"
            r = requests.get(url=url, params=params)

            if r.ok:
                data = r.json()
                pages = data.get("pages")

                for page in range(pages):
                    params["page"] = page
                    response = requests.get(url=url, params=params)
                    data = response.json()
                    vacancies = data.get("items")

                    for vacancy in vacancies:
                        result.append({
                            "name": vacancy.get("name"),
                            "salary_from": vacancy.get("salary").get("from"),
                            "salary_to": vacancy.get("salary").get("to"),
                            "area": vacancy.get("area").get("name"),
                            "employer_id": vacancy.get("employer").get("id"),
                            "url": vacancy.get("alternate_url"),
                        })
            else:
                raise Exception(f"Requests was not successful!\nStatus code: {r.status_code}.")

        return result

    @classmethod
    def get_employers(cls) -> list[dict[str:int or str or None]]:
        """Parsing HH.RU for specific employers by employer_id"""
        result = []

        for employer in cls.employers.values():
            r = requests.get(url=f"https://api.hh.ru/employers/{employer}")

            if r.ok:
                employers = r.json()
                result.append({
                    "id": employers.get("id"),
                    "name": employers.get("name"),
                    "url": employers.get("alternate_url"),
                    "open_vacancies": employers.get("open_vacancies")
                })
            else:
                raise Exception(f"Requests was not successful!\nStatus code: {r.status_code}.")

        return result
