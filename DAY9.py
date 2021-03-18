#DICTIONARIES AND NESTING DAY
#'''
#            KEY       |                  VALUE
#       -----------------------------------------------------------
#            Bug       |     An error in a program that prevents
#                      |        the program from running as
#                      |                  expected.
#       -----------------------------------------------------------
#          Function    |    A piece of code that you can easily
#                      |          call over and over again
#       -----------------------------------------------------------
#          Loop        |     The action od doing something over
#                      |               and over again
#       -----------------------------------------------------------
#
# {"Bug": "An error in a program that prevents the program from running as expected.",
#  "Function": "A piece of code that you can easily call over and over again",
#  "Loop": "The action od doing something over and over again"
#  }
#
#
# '''
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again",
    56: "I'm here to inform you how to write in dictionary with the correct data type!",

}

# Retrieving items from dictionary.
print(programming_dictionary["Bug"])
print(programming_dictionary[56])

# Adding new items to dictionary.
programming_dictionary["Loop"] = "The action od doing something over and over again."
print(programming_dictionary["Loop"])

# Create an empty dictionary
empty_dictionary = {}

# Wipe an existing dictionary
programming_dictionary = {}
print(programming_dictionary)

# Edit an item in dictionary
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary["Bug"])

print("\n")
# Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])


student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 96,
    "Draco": 74,
    "Zack": 98,
    "Neville": 62,
}
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_scores[student] = 'Outstanding'
    elif score > 80:
        student_scores[student] = 'Exceeds Expectation'

    elif score > 70:
        student_scores[student] = 'Acceptable'
    else:
        student_scores[student] = 'Fail'
print(student_scores)


# NESTING

capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}
# NESTING Dictionary/List in a Dictionary '''
#
# {
#   key: {"": [], "": [], "": value},
#   Key2: {"": [], "": [], "": value2},
# }
# '''
travel_log = {
    "France": {"cities_visited":["Paris", "Lille", "Dijon"], "total_visited": 12 },
    "Germany": {"cities_visited":["Berlin", "Hamburg", "Stuttgart"], "total_visited": 5},
}
# NESTING dictionary in a List '''
#
# [{
#   key: [List],
#   Key2: {Dict}}
# },
#   key: value,
#   Key2: value,
# }]
# '''


def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["Country"] = country_visited
    new_country["cities_visited"] = cities_visited
    new_country["total_visited"] = times_visited
    travel_log2.append(new_country)

travel_log2 = [
    {"country": "France",
     "cities_visited": ["Paris", "Lille", "Dijon"],
     "total_visited": 12
     },
    {"Country": "Germany",
     "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
     "total_visited": 5
     },
]

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log2)

# The secret auction Program
bids = {}
bidding_finished = False


def get_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bids[name] = bid
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no': ")
    if other_bidders == 'no':
        bidding_finished = True
        get_highest_bidder(bids)
    elif other_bidders == 'yes':
        continue






