import requests
import re
import pprint


def filter_text(text):
    new_test = re.sub(r'<.*?>', '', text)
    russian_chars = re.compile(r'[А-Яа-яёЁ0-9]')
    # Замена русских символов на пустую строку
    cleaned_text = russian_chars.sub('', new_test)
    technologies = re.findall(r'\b\w+\b', cleaned_text)
    technologies_filter = [i for i in technologies if len(i) > 1]
    return technologies_filter


def get_percent(el, mas):
    count = 0
    for j in mas:
        if el == j:
            count += 1
    return count


def get_tyrple(el_new_array, el_new_array_percent, el_new_array_count):
    text = {
        'name': el_new_array,
        'count': el_new_array_count,
        'persent': f"{el_new_array_percent}%",
    },
    return text
def request_hh(TEXT_PARAM,url="https://api.hh.ru/vacancies"):
    param = {
        'text': TEXT_PARAM,
        "area": 1,
        'page': 20,
    }
    response = requests.get(url, params=param)
    json = response.json()
    vacancies = json.get('items', [])
    print(f"1.Всего вакансий {len(vacancies)}")
    mas_salary_to = []
    mas_salary_from = []
    for i in vacancies:
        if i['salary']:
            mas_salary_from.append(i['salary']['from'])
            mas_salary_to.append(i['salary']['to'])

    print(
        f"2. Средняя зп от {sum([i for i in mas_salary_from if i is not None]) / len(mas_salary_from)} до {sum([i for i in mas_salary_to if i is not None]) / len(mas_salary_to)}")
    print(f"3. Требования к вакансии")

    mas_tech = []
    for i, vac in enumerate(vacancies):
        temp_mas = filter_text(
            vac['snippet']['requirement'].replace('<highlighttext>', '').replace('</highlighttext>', ''))
        [mas_tech.append(i) for i in temp_mas]
        print(f"3.{i} Вакансия {i} || Требования {temp_mas}")
    new_array = list(set(mas_tech))
    new_array_percent = []
    new_array_count = []
    for i in new_array:
        count = get_percent(i, mas_tech)
        new_array_count.append(count)
        percent = str(count / len(new_array) * 100)[:4]
        new_array_percent.append(percent)
        print(f"4. {i} {percent}%")

    seg = {
        "keywords": TEXT_PARAM,
        'count': len(vacancies),
        "requirements": [get_tyrple(new_array[i], new_array_percent[i], new_array_count[i]) for i in
                         range(len(new_array))]
    }
    pprint.pprint(seg)
    return seg

#request_hh("Python developer")
