# stars for card number

number = '2034399002121100'


def get_hidden_card(card_number, stars_count=4):
    stars = "*" * stars_count
    card_number = card_number[12:16]
    return stars + card_number


print(get_hidden_card(number, 3))
