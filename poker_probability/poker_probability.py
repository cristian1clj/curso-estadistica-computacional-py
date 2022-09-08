# Python
from typing import Tuple, List, Dict
from random import sample

# Files
from hand_validations import is_flush, is_poker, is_royal_flush, is_straight, count_values

CARD_SUITS: Tuple[str] = ('Pica', 'Trebol', 'Corazon', 'Diamante')
CARD_VALUES: Tuple[str] = ('A', '2', '3', '4', '5', '6', 
                           '7', '8', '9', '10', 'J', 'Q', 'K')
TYPES_HANDS: Tuple[str] = ('Escalera Real', 'Escalera de Color', 'Poker', 'Full', 
                           'Color', 'Escalera', 'Trio', 'Doble Pareja', 'Pareja')

TEST_HAND: List[List[Tuple[str, str]]] = [[('pica', 'A'), ('pica', 'J'), ('pica', 'Q'), ('pica', 'K'), ('pica', '10')], 
                              [('trevol', '2'), ('trevol', '3'), ('trevol', '4'), ('trevol', '5'), ('trevol', '6')], 
                              [('trevol', '9'), ('corazon', 'J'), ('diamante', 'Q'), ('trevol', 'K'), ('pica', '10')], 
                              [('trevol', 'A'), ('corazon', 'A'), ('diamante', 'A'), ('trevol', 'A'), ('pica', '10')], 
                              [('trevol', 'Q'), ('corazon', 'Q'), ('diamante', 'Q'), ('trevol', '4'), ('pica', '4')], 
                              [('corazon', 'A'), ('corazon', '8'), ('corazon', '2'), ('corazon', '4'), ('corazon', '10')], 
                              [('trevol', 'A'), ('corazon', '2'), ('diamante', '2'), ('trevol', '2'), ('pica', '10')], 
                              [('trevol', 'A'), ('corazon', 'A'), ('diamante', '10'), ('trevol', '5'), ('pica', '10')], 
                              [('trevol', '3'), ('corazon', '3'), ('diamante', '5'), ('trevol', 'A'), ('pica', '10')], 
                              [('trevol', '4'), ('corazon', '2'), ('diamante', 'Q'), ('trevol', 'K'), ('pica', '10')]]


def generate_deck(suits: list, values: list) -> List[Tuple[str, str]]:
    deck: List[Tuple[str, str]] = []
    
    for suit in suits:
        for value in values:
            deck.append((suit, value))
    
    return deck


def generate_hand(deck: List[Tuple[str, str]], hand_size: int) -> List[Tuple[str, str]]:
    hand = sample(deck, hand_size)
    return hand


def count_hands(types_hands: Tuple[str], hands: List[List[Tuple[str, str]]]) -> Dict[str, int]:    
    count: Dict[str, int] = {hand: 0 for hand in types_hands}
    
    for hand in hands:
        suit: List[str] = []
        value: List[str] = []
        
        for card in hand:
            suit.append(card[0])
            value.append(card[1])
        
        if is_royal_flush(suit, value):
            count['Escalera Real'] += 1
        
        elif is_straight(value, CARD_VALUES):
            if len(set(suit)) == 1 :
                count['Escalera de Color'] += 1
            else:
                count['Escalera'] += 1
        
        elif is_poker(value):
            count['Poker'] += 1
            
        elif is_flush(suit):
            count['Color'] += 1
        
        else:
            count_vals: List[int] = sorted(list(count_values(value).values()))
            
            if count_vals.count(3) == 1 and count_vals.count(2) == 1:
                count['Full'] += 1
            
            elif count_vals.count(3) == 1:
                count['Trio'] += 1
            
            elif count_vals.count(2) == 2:
                count['Doble Pareja'] += 1
            
            elif count_vals.count(2) == 1:
                count['Pareja'] += 1
        
    # print(count)
    return count


def calculate_probability(values: Dict[str, int], attempts: int) -> Dict[str, float]:
    probabilities = {}
    for key, value in values.items():
        probabilities[key] = value / attempts
    
    return probabilities


def simulation(hand_size: int, attempts: int):
    deck: List[Tuple[str, str]] = generate_deck(CARD_SUITS, CARD_VALUES)
    hands: List[List[Tuple[str, str]]] = []
    
    for _ in range(attempts):
        hand = generate_hand(deck, hand_size)
        hands.append(hand)
    
    count: Dict[str, int] = count_hands(TYPES_HANDS, hands)
    probabilities: Dict[str, float] = calculate_probability(count, attempts)
    
    for type_hand, probability in probabilities.items():
        print(f'Probabilidad de {type_hand} es {probability}')


def run():
    attempts = int(input('Cuantas veces se repetira el proceso?: '))
    simulation(5, attempts)


if __name__ == '__main__':
    run()