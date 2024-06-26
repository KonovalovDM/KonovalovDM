#Практическая работа по созданию списка словарей и определению среднего возраста в разрезе пола с помощью функции

names = ['igor', 'dasha', 'martin', 'vladimir', 'rishat', 'maria', 'marat', 'petr', 'dima', 'polina', 'katya', 'elena']
ages = ['25', '24', '28', '26', '32', '45', '42', '54', '57', '41', '23', '27']
genders = ['male', 'female', 'male', 'male', 'male', 'female', 'male', 'male', 'male', 'female', 'female', 'female']

# определяем список для запаковки словарей
data = []

# создаем словарь имен с возрастом и полом
name_age_gender_dict = {}

# набиваем в цикле список словарями из списков имен с возрастом и полом

for i in range(len(names)):
    name_age_gender_dict = {
        'name': names[i],
        'age': int(ages[i]),
        'gender': genders[i],
    }
    data.append(name_age_gender_dict)

print(f'\nСписок словарей: data =\n', data)


#Создаем словари из списка словарей, выбираем только пол человека и забираем его возраст
"""Функция для создания словарей с выбранным полом и соответствующим возрастом"""
def genders_m_f(age, gender):
    return {data['age']: data['gender'] for data in data if data['gender'] == gender}

#контроль работы функции
print(genders_m_f(data, 'male'))
print(len(genders_m_f(data, 'male')))
print(genders_m_f(data, 'female'))
print(len(genders_m_f(data, 'female')))

"""Функция для определения среднего возраста по соответствующему полу"""
def avg_ages_filter_genders(info, gender):
    return sum(st['age'] for st in info if st['gender'] == gender) / len(genders_m_f(data, gender))

#контроль работы функции
print('\n')
print(round(avg_ages_filter_genders(data, 'male'), 3))
print(round(avg_ages_filter_genders(data, 'female'), 3))