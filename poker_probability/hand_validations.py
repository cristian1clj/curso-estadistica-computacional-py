# Python
from typing import Dict, Tuple, List
from collections import Counter


def is_royal_flush(suits: List[str], values: List[str]) -> bool:
    ROYAL_FLUSH: Tuple[str] = ('10', 'A', 'J', 'K', 'Q')
    royal_val_counts = lambda vals: sorted(vals) == list(ROYAL_FLUSH)
    
    if (len(set(suits)) == 1) and royal_val_counts(values):
        return True
    
    return False


def is_straight(values: List[str], card_val_counts: Tuple[str]) -> bool:
    ladder_model: List[str] = []
    
    for i in range(len(card_val_counts)):
        if card_val_counts[i] in values:
            ladder_model.extend(card_val_counts[i:i + 5])
            break
    
    for value in values:
        if value not in ladder_model:
            return False
    
    return True


def is_poker(values: List[str]) -> bool:
    for value in values:
        if values.count(value) == 4:
            return True
    
    return False


def is_flush(suits: List[str]) -> bool:
    if len(set(suits)) == 1:
        return True
    
    return False


def count_values(values: List[str]) -> Dict[str, int]:
  return dict(Counter(values))
