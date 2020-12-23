import array

# each deck is represented by an array.. the left side is the top
# and the right side is the bottom

def load_decks(filename):
    with open(filename) as f:
        deck_data = f.read().split('\n\n')
    # Ignore header line with [1:]
    return [array.array("i", [int(line) for line in cards.split('\n')[1:]]) for cards in deck_data]

def print_decks(decks):
    for i, deck in enumerate(decks):
        print(f"Player {i}'s deck: {deck}")    

def round(decks):
    cards = [deck.pop(0) for deck in decks]

    if cards[0] > cards[1]:
        decks[0].append(cards[0])
        decks[0].append(cards[1])
        return 0
    else:
        decks[1].append(cards[1])
        decks[1].append(cards[0])
        return 1

def score(deck):
     return sum([(len(deck)-i)*card for i,card in enumerate(deck)])
    
def part1(filename):
    decks = load_decks(filename)

    while len(decks[0]) > 0 and len(decks[1]) > 0:
        winner = round(decks)

    print("== Combat Post Game Results ==")
    print_decks(decks)
    print(f"Player {winner} wins!")

    print(score(decks[winner]))
    print()

def have_played(history, decks):
    h0, h1 = score(decks[0]), score(decks[1])
    if h0 in history and h1 in history[h0]:
        return True
    return False

def record_played(history, decks):
    h0, h1 = score(decks[0]), score(decks[1])
    hist0 = history.get(h0, set())
    hist0.add(h1)
    history[h0] = hist0


def play_game(decks):
    history = {}
    winner = 0

    while len(decks[0]) > 0 and len(decks[1]) > 0:
        if have_played(history, decks):
            return 0
        record_played(history, decks)

        if (m := max(decks[0])) > max(decks[1]) and m > len(decks[0]) + len(decks[1]):# p0 can't lose
            return 0
        
        cards = [deck.pop(0) for deck in decks]

        if len(decks[0]) >= cards[0] and len(decks[1]) >= cards[1]:
            winner = play_game([decks[0][:cards[0]], decks[1][:cards[1]]])
        else:
            winner = 0 if cards[0] > cards[1] else 1

        if winner == 0:
            decks[0].append(cards[0])
            decks[0].append(cards[1])
        else:
            decks[1].append(cards[1])
            decks[1].append(cards[0])

    return winner

def part2(filename):
    decks = load_decks(filename)
    winner = play_game(decks)
    print("== Recursive Combat Post Game Results ==")
    print_decks(decks)
    print(f"Player {winner} wins!")

    print(score(decks[winner]))

part1('input/input22.txt')
part2('input/input22.txt')