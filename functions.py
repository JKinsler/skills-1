"""SKILLS: FUNCTIONS

Please complete the following promps.
"""

#################### PART 1 ####################


"""PROMPT 1

Write a function that returns `True` if a town name matches the name of your
hometown.

Examples: (let's say my hometown is San Francisco)
    - 'Oakland' -> False
    - 'San Francisco' -> True

Arguments:
    - The name of a town (str)

Return:
    - True or False (bool)
"""

# Write your function here


def tests_hometown(town):
    """Test whether a town name matches my home town, 'Lake Angelus' 

    IN: Take in a town name as an input
    OUT: Returns True / False as an output"""

    return town == 'Lake Angelus'


"""PROMPT 2

Write a function that takes in a first and last name and returns a full name.

Examples:
    - 'Brighticorn', 'Hackbright' -> 'Brighticorn Hackbright'

Arguments:
    - First name (str)
    - Last name (str)

Return:
    - Full name (str)
"""

# Write your function here


def writes_full_name(first, last):
    """Take in first and last name and returns a full name"""

    return first + " " + last


"""PROMPT 3

Write a function that prints a greeting.

If the person is from your hometown, print
    Hi <full name>, we're from the same place!

Otherwise, print
    Hi <full name>, I'd like to visit <town name>!

HINT: You can reuse the functions that you wrote in PROMPT 1 and Prompt 2.

Examples: (still assume my hometown is San Francisco)
    - 'Fido', 'Bark', 'Oakland' -> Hi Fido Bark, I'd like to visit Oakland!
    - 'Mel', 'M', 'San Francisco' -> Hi Mel M, we're from the same place!

Arguments:
    - First name (str)
    - Last name (str)
    - Hometown (str)
"""

# Write your function here


def prints_greeting(first_name, last_name, town):
    """Print a greeting.

    If the person is from the same hometown then message says so.
    If the person is from a different hometown then message shows interest 
    to visit."""

    full_name = writes_full_name(first_name, last_name)
    same_town = tests_hometown(town)

    #print greeting for people from the same town
    if same_town == True:
        print(f"Hi {full_name}, we're from the same town!")

    #print greeting for people from a different town
    if same_town == False:
        print(f"Hi {full_name}, I'd like to visit {town}!")

    return


"""PROMPT 4

Write a function that returns True if a fruit is a berry.

Valid berries are:
    - strawberry
    - raspberry
    - blackberry
    - currant

Examples:
    - currant -> True
    - durian -> False

Arguments:
    - A fruit (str)

Return:
    - True or False (bool)
"""

# Write your function here


def test_if_berry(fruit):
    """Test whether a fruit is one of: strawberry, raspberry, blackburry,
    currant. """

    berries = ['strawberry', 'raspberry', 'blackburry', 'currant']
    return fruit in berries


"""PROMPT 5

Write a function that returns the shipping cost of an item.

Berries cost $0 to ship. Everything else costs $5.

Arguments:
    - Something that needs to be shipped (str)

Return:
    - Shipping cost (int)
"""

# Write your function here


def calc_shipping(item):
    """Return the shipping cost of an item.

    Berries cost $0 to ship.
    Everything else costs $5. """

    berry = test_if_berry(item)

    if berry == True:
        return 0

    else:
        return 5


"""PROMPT 6

Write a function that returns the total cost of something by applying
taxes and fees of various states.

States will be given as their two-letter abbreviations. For example,
California's abbreviation is 'CA'.

There are some states with special fees. All fees should be added to the new
subtotal *after* tax:
    - CA (California): add a 3% (0.03) tax for recycling
    - PA (Pennsylvania): add $2.00 safety fee
    - MA (Massachusettes):
        - add $1.00 for items with a base price of $100.00 or less
        - add $3.00 for items over $100.00

Arguments:
    - Base price (int)
    - Two-letter state abbreviation (str)
    - Tax percentage as a decimal (optional, float)
        - If a tax percentage is not given, it defaults to 0.05 (or 5%)

Return:
    - Total price after taxes and fees (float)
"""

# Write your function here


def calc_total_cost(base_price, state, tax_decimal_percent = 0.05):
    """Calculate the total cost of something with taxes and fees.
    
    Fees vary by state, and are added after tax:
    CA: + 3% for recycling
    PA: + $2 for safety
    MA:
        + $1 if total is less than or equal to $100
        + $3 if total is greater than $100  """

    #convert input price to a float
    base_price = float(base_price)
    tax_decimal_percent = float(tax_decimal_percent)

    #calculate taxes
    taxes = base_price * tax_decimal_percent

    #calculate fees, per state rules
    if state == 'CA':
        fees = (base_price + taxes) * 0.03

    elif state == 'PA':
        fees = 2.00

    elif state == 'MA':
        if base_price <= 100.00:
            fees = 1

        elif base_price > 100.00:
            fees = 3.00

    else:
        fees = 0.00

    #calculate total
    total_cost = base_price + taxes + fees

    return total_cost


"""PROMPT 7

Write a function that takes in a list and *any* number of additional arguments.
The function should add all those items to the end of the  list and return
the list.

We haven't taught you how to do this! You'll need to do some research on your
own --- find a way to write a Python function that can take in an arbitrary
amount of arguments.

Arguments:
    - A list (list)
    - Additional args

Return:
    - A list with arguments added to the end (list)
"""

# Write your function here


def append_list(input_list, *args):
    """Create a list that includes an original list and added items """

    #create a list that contains all the items from the input list
    output_list = input_list[::]

    #append each additional input argument
    output_list.append(args)

    return output_list


"""PROMPT 8

Write a function that takes in a word and returns a tuple. You'll do this in an
interesting way though, so make sure you read these directions thoroughly.

The tuple will contain two items:
    - The given word
    - The given word, multiplied 3 times

To do this, your function will create an *inner* function. The *inner*
function will multiply the given word by 3 and return it.

Then, the outer function will call the *inner* function to create a tuple.

Examples:
    - 'hi' -> ('hi', 'hihihi')

Arguments:
    - A word (str)

Return:
    - (word, wordx3) (tuple)
"""

# Write your function here


def tuples_triple_word(word):
    """Tripple a word and return it with the original, as a tuple. """

    def triples_word(word):
        """Triples a word """

        return word*3

    tripple = triples_word(word)


    return (word, tripple)





#------------------------------------------------------------------
"""Developer test code is below"""

#tests_hometown_output = tests_hometown('Barthalameau')
#print(tests_hometown_output)

#tests_writes_full_name = writes_full_name('Beaugle', 'Buddies')
#print(tests_writes_full_name)

#tests_prints_greeting = prints_greeting('Apple', 'Bear', 'Lake Angelus')
#print(tests_prints_greeting)

#print(test_if_berry('apple'))

#print(calc_shipping('strawberry'))

#print(calc_total_cost(100.00, 'IW', 0.3))

#some_args = 'apple', 'berry', 'cherry'
# print(append_list([1, 2], 984, 212, 312))

print(tuples_triple_word('beans'))

