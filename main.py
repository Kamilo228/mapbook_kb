# definicja prostej struktury danych obejmujące przykładowego użytkownika
users = [
    {'name': 'Artur', 'location': 'Łomża',
     'posts': ['Sprzedam mercedesa', 'Kupię skrzynię biegów', 'Ratunku co robić po wypadku?',
               'Kto dzisiaj idzie biegać?']},
    {'name': 'Daniel', 'location': 'Legionowo',
     'posts': ['Mój kod nie działa, pomocy!']},
    {'name': 'Kamil', 'location': 'Ciechanów',
     'posts': ['Czy ktoś zrobił już sprawozdanie z Ppyt?']},

]


def read_users(users_data: list) -> None:
    for user in users_data:
        print(f'Twój znajomy {user["name"]} z miejscowości {user["location"]} opublikował post {user["posts"][-1]}')


def add_user(users_data: list) -> None:
    users_data.append({'name': input('Podaj imię użytkownika: '), 'location': input('Podaj swoją lokalizację: '),
                       'posts': ['Dołączono do znajomych']})


def remove_user(users_data: list) -> None:
    user_to_remove = input('Podaj imię znajomego do usunięcia: ')
    for user in users_data:
        if user['name'] == user_to_remove:
            users.remove(user)


def update_user(users_data: list) -> None:
    user_to_update = input('Podaj imię znajomego do zaktualizowania: ')
    for user in users_data:
        if user['name'] == user_to_update:
            user['name'] = input('Podaj nowe imię znajomego: ')
            user['location'] = input('Podaj nową lokalizację znajomego: ')

def update_user_post(users_data: list) -> None:
    user_to_update = input('Podaj imię znajomego do zaktualizowania: ')
    for user in users_data:
        if user['name'] == user_to_update:
            user['posts'].append(input('Co słychać? '))

while True:
    print('======MENU=======')
    print('0 - Zakończ program')
    print('1 - Wyświetl znajomych')
    print('2 - Dodaj znajomego')
    print('3 - Usuń znajowwego')
    print('4 - Zaktualizuj znajowwego')
    print('5 - Zaktualizuj posta')
    choice = input('Wybierz opcję menu: ')
    print(f'Wybrano opcję {choice}')
    if choice == '0':
        break

    if choice == '1':
        read_users(users)

    if choice == '2':
        add_user(users)

    if choice == '3':
        remove_user(users)

    if choice == '4':
        update_user(users)

    if choice == '5':
        update_user_post(users)