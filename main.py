import random
import time


class Toad:
    name: str  # Имя персонажа
    health: int  # Кол-во здоровья
    damage: int  # Урон
    armor: int  # Броня
    character_class: str  # Класс персонажа

    def __init__(self,
                 name,
                 health=150,
                 damage=10,
                 armor=8,
                 character_class: str = random.choice(['assassin', 'craftsman', 'adventurer'])):
        """ Присваиваем стандарные значения и рандомный класс """
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor
        self.character_class = character_class
        self.initial_health = health

    def reset_health(self):
        self.health = self.initial_health
    # def random_class(self):
    #     """ Присваиваем рандомный класс персонажу """
    #     list_class = ['assassin', 'craftsman', 'adventurer']
    #     chosen_class = random.choice(list_class)
    #     self.character_class = chosen_class

    def cause_damage(self, pers_for_attack: 'Toad') -> None:
        """ Логика нанесение удара """
        damage = random.randint(0, self.damage)
        if self.character_class == 'assassin':
            chance_to_dodge_damage = 5  # В процентах
            if random.randint(1, 100) <= chance_to_dodge_damage:
                # print(f'{pers_for_attack.name} использует способность и уворачивается от урона')
                return
        if self.character_class == 'craftsman':
            chance_of_damage_reduction = 20  # В процентах
            if random.randint(1, 100) <= chance_of_damage_reduction:
                damage = int(damage * 0.3)
                # print(f"{pers_for_attack.name} использует способность и снижает урон")
        if self.character_class == 'adventurer':
            chance_of_duble_damage = 2
            # print(f"{self.name} использует способность и удваивает урон")
            if random.randint(1, 100) <= chance_of_duble_damage:
                damage *= 2
        pers_for_attack.health -= damage

        # баловался просто рандомные фразы и таймер чтобы читать успевать ))
        # random_phrase = [
        #     'наносит болючий удар',
        #     'бьёт с левой пятки в нос',
        #     'неожиданно наносит удар',
        #     'бьёт с левой',
        # ]
        # random_phrase_for_print = random.choice(random_phrase)
        # print(f"{self.name} {random_phrase_for_print} {pers_for_attack.name} и наносит {damage} урона")
        # time.sleep(.1)
        # тут конец )


def battle(pers_1: Toad, pers_2: Toad):
    """
    Функция для проведия битвы между двумя персонажами
    pers_1 начинает аттаку первый
    PS можно сделать и рандом
    """
    while all([pers_1.health > 0, pers_2.health > 0]):
        pers_1.cause_damage(pers_2)
        pers_2.cause_damage(pers_1)
    if pers_1.health > pers_2.health:
        return pers_1
    if pers_1.health == pers_2.health:
        return 'draw'
    if pers_2.health > pers_1.health:
        return pers_2


def get_finght(count_fight: int):

    count_win_pers_1 = 0
    count_win_pers_2 = 0

    for _ in range(count_fight):

        pers_1 = Toad(name='Biba', character_class='assassin')
        pers_2 = Toad(name='Boba', character_class='assassin')

        pers_win = battle(pers_1=pers_1, pers_2=pers_2)
        if pers_win == 'draw':
            # print('Ничья')
            continue
        if pers_win.name == pers_1.name:
            # print(f'{pers_1.name} win')
            count_win_pers_1 += 1
        else:
            # print(f'{pers_2.name} win')
            count_win_pers_2 += 1

    print(f"""{pers_1.name} выйграл {count_win_pers_1}
{pers_2.name} выйграл {count_win_pers_2}""")
    # можно вернуть json тип такого
    # dict_win = {
    #     pers_1.name:{
    #         'count_win': count_win_pers_1
    #     },
    #     pers_2.name: {
    #         'count_win': count_win_pers_2
    #     }
    # }
    # return dict_win

get_finght(100)
