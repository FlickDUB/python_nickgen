from random import choice, randint

__version__ = '1.0.0'

LOCALES = ('en', 'ru')


en_vowels = ('a', 'e', 'i', 'o', 'u', 'y')
en_consonants = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z',
                 'sh', 'zh', 'ch', 'kh', 'th')
ru_vowels = ('а', 'е', 'и', 'о', 'у', 'э', 'ю', 'я')
ru_consonants = ('б', 'в', 'г', 'д', 'ж', 'з', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ')


def generate(num=10, locale='en', deviation_rate=10, min_length=6, max_length=9, ends_num_amount=2):

    if locale not in LOCALES:
        raise ValueError('Locale is not correct!')
    
    if not (deviation_rate <= 100 and deviation_rate >= 0):
        raise ValueError('Deviation rate is not correct!')

    vowels = globals()[f'{locale}_vowels']
    consonants = globals()[f'{locale}_consonants']

    is_vowels_first = randint(0, 1)
    
    result = []
    for _ in range(num):
        nick = ''
        for i in range(0, randint(min_length, max_length)):
            is_even = i % 2
            if randint(0, 100) <= deviation_rate:
                is_even = (is_even + 1) % 2

            if (is_vowels_first and is_even) or (not is_vowels_first and not is_even):
                nick += choice(vowels)
            else:
                nick += choice(consonants)

        if ends_num_amount:
            for _ in range(ends_num_amount):
                nick += str(randint(0, 9))
            
        result.append(nick.title())

    return result

if __name__ == '__main__':
    get_format_num = lambda  s, num: s - num if (s := len(s)) > num else num - s
    ru = generate(locale='ru'); eng = generate()
    text = (lambda i, j: [i[k] + ' ' * get_format_num(i[k], 20) + j[k] for k in range(min([len(i), len(j)]))])(eng, ru)
    print('English' + get_format_num('English', 20) * ' ' + 'Русский', end='\n\n')
    print('\n'.join(text))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
'''
⣿⠟⣽⣿⣿⣿⣿⣿⢣⠟⠋⡜⠄⢸⣿⣿⡟⣬⢁⠠⠁⣤⠄⢰⠄⠇⢻⢸
⢏⣾⣿⣿⣿⠿⣟⢁⡴⡀⡜⣠⣶⢸⣿⣿⢃⡇⠂⢁⣶⣦⣅⠈⠇⠄⢸⢸
⣹⣿⣿⣿⡗⣾⡟⡜⣵⠃⣴⣿⣿⢸⣿⣿⢸⠘⢰⣿⣿⣿⣿⡀⢱⠄⠨⢸
⣿⣿⣿⣿⡇⣿⢁⣾⣿⣾⣿⣿⣿⣿⣸⣿⡎⠐⠒⠚⠛⠛⠿⢧⠄⠄⢠⣼
⣿⣿⣿⣿⠃⠿⢸⡿⠭⠭⢽⣿⣿⣿⢂⣿⠃⣤⠄⠄⠄⠄⠄⠄⠄⠄⣿⡾
⣼⠏⣿⡏⠄⠄⢠⣤⣶⣶⣾⣿⣿⣟⣾⣾⣼⣿⠒⠄⠄⠄⡠⣴⡄⢠⣿⣵
⣳⠄⣿⠄⠄⢣⠸⣹⣿⡟⣻⣿⣿⣿⣿⣿⣿⡿⡻⡖⠦⢤⣔⣯⡅⣼⡿⣹
⡿⣼⢸⠄⠄⣷⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣕⡜⡌⡝⡸⠙⣼⠟⢱⠏
⡇⣿⣧⡰⡄⣿⣿⣿⣿⡿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣋⣪⣥⢠⠏⠄
⣧⢻⣿⣷⣧⢻⣿⣿⣿⡇⠄⢀⣀⣀⡙⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠂⠄⠄
⢹⣼⣿⣿⣿⣧⡻⣿⣿⣇⣴⣿⣿⣿⣷⢸⣿⣿⣿⣿⣿⣿⣿⣿⣰⠄⠄⠄
⣼⡟⡟⣿⢸⣿⣿⣝⢿⣿⣾⣿⣿⣿⢟⣾⣿⣿⣿⣿⣿⣿⣿⣿⠟⠄⡀⡀
⣿⢰⣿⢹⢸⣿⣿⣿⣷⣝⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠉⠄⠄⣸⢰⡇
⣿⣾⣹⣏⢸⣿⣿⣿⣿⣿⣷⣍⡻⣛⣛⣛⡉⠁⠄⠄⠄⠄⠄⠄⢀⢇⡏⠄ 
'''
