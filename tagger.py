from pymorphy2 import MorphAnalyzer
from nltk import word_tokenize


morph = MorphAnalyzer()

LANGS = ['английский', 'испанский', 'немецкий', 'итальянский', 'китайский',
         'корейский', 'французский', 'греческий', 'арабский', 'японский',
         'португальский', 'персидский', 'шведский']
INSTRUMENTS = ['гитара', 'пианино', 'фортепиано', 'балалайка', 'барабан', 'флейта', 'саксафон', 'труба']
SUBJ = ['математика', 'информатика', 'химия', 'история', 'обществознание', 'биология', 'физика', 'литература']
START_TAGS = ['Онлайн', 'Программирование', 'Развитие интеллекта', 'Робототехника', 'Борьба', 'Гимнастика',
              'Единоборства', 'Лыжный спорт', 'Спортивное развитие', 'Самбо', 'Танцы', 'Футбол', 'Музыка',
              'Рисование'] + [f'{l[0].upper()}{l[1:]} язык' for l in LANGS] +\
             [f'{i[0].upper()}{i[1:]}' for i in INSTRUMENTS] + ['Театральные курсы', 'Шахматы', 'LEGO',
              'Логопед', 'Подготовка к ОГЭ', 'Подготовка к ЕГЭ'] + [f'{s[0].upper()}{s[1:]}' for s in SUBJ] +\
              ['Каллиграфия', 'Скорочтение', 'Каратэ', 'Айкидо', 'Фехтование', 'Вокал', 'Баскетбол', 'Плавание']


class NaiveTagger:
    def __init__(self, txt):
        self.tag_list = []
        self.valid_words = self.get_valid_words(txt)
        self.words = set(self.valid_words)

    def get_tag(self):
        if len(online_words.intersection(self.words)) > 0:
            self.tag_list.append('Онлайн')
        if len(programming_words.intersection(self.words)) > 0:
            self.tag_list.append('Программирование')
        if len(intell_words.intersection(self.words)) > 2:
            self.tag_list.append('Развитие интеллекта')
        if len(robot_words.intersection(self.words)) > 0:
            self.tag_list.append('Робототехника')
        if 'борьба' in self.words:
            self.tag_list.append('Борьба')
        if 'гимнастика' in self.words:
            self.tag_list.append('Гимнастика')
        if len(combat_words.intersection(self.words)) > 0:
            self.tag_list.append('Единоборства')
        if len(ski_words.intersection(self.words)) > 0:
            self.tag_list.append('Лыжный спорт')
        if len(sport_words.intersection(self.words)) > 3:
            self.tag_list.append('Спортивное развитие')
        if 'самбо' in self.words:
            self.tag_list.append('Самбо')
        if len(dance_words.intersection(self.words)) > 0:
            self.tag_list.append('Танцы')
        if 'футбол' in self.words:
            self.tag_list.append('Футбол')
        for l in LANGS:
            if l in self.words and 'язык' in self.words:
                self.tag_list.append(f'{l[0].upper()}{l[1:]} язык')
        if 'музыка' in self.words or 'музыкальная' in self.words:
            i_tags = []
            for i in INSTRUMENTS:
                if i in self.words:
                    i_tags.append(i)
            if len(i_tags) < 2:
                self.tag_list += i_tags
                self.tag_list.append('Музыка')
            else:
                self.tag_list.append('Музыка')
                self.tag_list += i_tags
        if 'рисовать' in self.words or 'рисование' in self.words or 'живопись' in self.words:
            self.tag_list.append('Рисование')
        if 'театр' in self.words and ('курс' in self.words or 'школа' in self.words):
            self.tag_list.append('Театральные курсы')
        if 'шахматы' in self.words:
            self.tag_list.append('Шахматы')
        if 'lego' in self.words:
            self.tag_list.append('LEGO')
        if 'логопед' in self.words or 'дефектолог' in self.words:
            self.tag_list.append('Логопед')
        if 'огэ' in self.words:
            self.tag_list.append('Подготовка к ОГЭ')
        if 'егэ' in self.words:
            self.tag_list.append('Подготовка к ЕГЭ')
        for s in SUBJ:
            if s in self.words:
                self.tag_list.append(f'{s[0].upper()}{s[1:]}')
        if 'каллиграфия' in self.words:
            self.tag_list.append('Каллиграфия')
        if 'скорочтение' in self.words:
            self.tag_list.append('Скорочтение')
        if 'каратэ' in self.words:
            self.tag_list.append('Каратэ')
        if 'айкидо' in self.words:
            self.tag_list.append('Айкидо')
        if 'фехтование' in self.words:
            self.tag_list.append('Фехтование')
        if len(sing_words.intersection(self.words)) > 0:
            self.tag_list.append('Вокал')
        if 'баскетбол' in self.words or 'баскетбольный' in self.words:
            self.tag_list.append('Баскетбол')
        if len(swim_words.intersection(self.words)) > 0:
            self.tag_list.append('Плавание')

        return self.tag_list

    def get_valid_words(self, txt: str):
        return [morph.parse(w)[0].normal_form for w in word_tokenize(txt)]


online_words = {'skype', 'zoom', 'online', 'онлайн', 'онлайн-школа'}
programming_words = {'python', 'c++', 'c', 'java', 'minecraft', 'робот', 'компьютер',
                     'робототехника', 'программировать'}
intell_words = {'продумать', 'решить', 'программировать', 'умение', 'урок', 'интеллект', 'развитие', 'успевать',
                'ответить', 'потенциал', 'сформироваться', 'открыть'}
robot_words = {'робот', 'робототехника'}
combat_words = {'единоборство', 'борьба', 'каратэ', 'айкидо', 'дзюдо', 'тайский', 'вольный', 'рукопашный', 'джиу',
                      'джитсу', 'драться', 'защита', 'защищаться', 'самооборона', 'тренировка'}
ski_words = {'лыжи', 'лыжный'}
sport_words = {'ОФП', 'общая', 'физическая', 'подготовка', 'бег', 'плавание', 'спорт', 'здоровье', 'здоровый',
               'спортивный', 'развитие'}
dance_words = {'танец', 'танцевальный'}
sing_words = {'петь', 'пение', 'вокал'}
swim_words = {'плавать', 'плавание', 'бассейн'}


def start_tags_to_csv():
    import pandas as pd
    pd.DataFrame.from_dict({'tag_id': range(len(START_TAGS)), 'tag_name': START_TAGS}).to_csv('th/START_TAGS.csv')


def get_id_by_tag(tag):
    return START_TAGS.index(tag)


if __name__ == '__main__':
    # tests
    for n, d in (
            ("Школа Let's Go", 'В нашей школе английского языка ваш ребёнок найдёт всё самое необходимое для изучения'
                               ' всех сложностей английского языка'),
            ('Секция Бориса Петровича', 'Учим детей не быть слабыми, уважать старших и бороться до конца'),
            ('Swim school', 'С нами ваш ребёнок начнёт плавать'),
            ("Уроки английского", 'Супер уроки английского')
    ):
        print(NaiveTagger(n + ' ' + d).get_tag())
