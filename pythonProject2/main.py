from heapq import heappush,heappop,heapify
from collections import defaultdict


def create_prob_model(text):
    """
    Vytvoření alphabety na základě zprávy a ke každému symbolu přidáme její frekvenci
    """

    prob_model = defaultdict (int)  # Každý nový znak má hodnotu 0
    for char in text:
        prob_model[char] += 1 / len (text)

    return prob_model


def huff_encode(text):
    """Huffmanovo kodování vstupní zprávy .

    Args:
        text: String, pořadí znaků(symbolů)

    Returns:
        source_code: Dict kde každá položka je {symbol: (frekvence, kod)}
        encoded_message: String, bitový řetězec kodové vstupní zprávy pomocí source_code

    """

    prob_model = create_prob_model (text)

    heap = [[freq,[sym,""]] for sym,freq in prob_model.items ()]
    heapify (heap)
    while len (heap) > 1:
        lo = heappop (heap)
        hi = heappop (heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush (heap,[lo[0] + hi[0]] + lo[1:] + hi[1:])
    symbol_code_pairs = sorted (heappop (heap)[1:],key=lambda p:(len (p[-1]),p))

    """Kod pro formátování textu """
    source_code = {}
    for pair in symbol_code_pairs:
        symbol = pair[0]
        codeword = pair[1]
        freq = prob_model[symbol]
        source_code[symbol] = (freq,codeword)

    encoded_message = ''
    for symbol in text:
        encoded_message += source_code[symbol][1]

    return source_code,encoded_message


"""Vložení textu, který chceme přeložit"""
text ="Toto je novy test pro testovani daného kodu"
source_code,encoded_message = huff_encode (text)
textde=len(encoded_message)
print ("Text:            {}".format (text))
print ("Zakodovaný text: {}".format (encoded_message))
print ("Délka textu:     {}\n".format (textde))

print ("Symbol Frekvence Kod")
for symbol,pair in sorted (source_code.items ()):
    print("{0:>2} {1:>9,.2f} {2:>8}".format(symbol, pair[0], pair[1]))