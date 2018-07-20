from dateutil import parser
from Menu import Menu  # or * if you want all from the Menu file
from Franchise import Franchise
from Business import Business

# Initialize four menus
brunch = Menu(
    "brunch", {
        'pancakes': 7.50,
        'waffles': 9.00,
        'burger': 11.00,
        'home fries': 4.50,
        'coffee': 1.50,
        'espresso': 3.00,
        'tea': 1.00,
        'mimosa': 10.50,
        'orange juice': 3.50
    },
    parser.parse("11:00"),
    parser.parse("16:00")
)

# print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))
# print(brunch)

early_bird = Menu(
    "Early Bird", {
        'salumeria plate': 8.00,
        'salad and breadsticks (serves 2, no refills)': 14.00,
        'pizza with quattro formaggi': 9.00,
        'duck ragu': 17.50,
        'mushroom ravioli (vegan)': 13.50,
        'coffee': 1.50, 'espresso': 3.00
    },
    parser.parse("15:00"),
    parser.parse("18:00")
)
# print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))
# print(early_bird)

dinner = Menu(
    "Dinner", {
        'crostini with eggplant caponata': 13.00,
        'ceaser salad': 16.00,
        'pizza with quattro formaggi': 11.00,
        'duck ragu': 19.50,
        'mushroom ravioli (vegan)': 13.50,
        'coffee': 2.00,
        'espresso': 3.00
    },
    parser.parse("17:00"),
    parser.parse("23:00")
)
# print(dinner)

kids = Menu(
    "Kids", {
        'chicken nuggets': 6.50,
        'fusilli with wild mushrooms': 12.00,
        'apple juice': 3.00
    },
    parser.parse("11:00"),
    parser.parse("21:00")
)
# print(kids)

flagship_store = Franchise(
    "1232 West End Road",
    [brunch, early_bird, dinner, kids]
)
# print(flagship_store)

new_installment = Franchise(
    "12 East Mulberry Street",
    [brunch, early_bird, dinner, kids]
)
# print(new_installment)

# Testing the available menus
# print(new_installment.available_menus(parser.parse("16:30")))

parser.parse("Tue May 08 15:14:45 +0800 2012")
arepas_menu = Menu(
    "Take a\' Arepa", {
        'arepa pabellon': 7.00,
        'pernil arepa': 8.50,
        'guayanes arepa': 8.00,
        'jamon arepa': 7.50
    },
    parser.parse("10:00"),
    parser.parse("20:00")
)

# Initializes three businesses
arepas_place = Franchise(
    "189 Fitzgerald Avenue",
    [arepas_menu]
)

business1 = Business(
    "Take a\' Arepa",
    [arepas_place]
)

business = Business(
    "\'Basta FazooLin\' with my Heart",
    [flagship_store, new_installment]
)
