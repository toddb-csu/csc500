if __name__ == '__main__':
    address_book = {}
    # Add an entry to the dictionary
    address_book[111] = {'first_name': 'Fred', 'last_name': 'Flintstone',
                         'address': '201 Cobblestone Lane', 'city': 'Bedrock City'}
    address_book[222] = {'first_name': 'Barney', 'last_name': 'Rubble',
                         'address': '142 Boulder Ave', 'city': 'Granitetown'}
    address_book[333] = {'first_name': 'Vilma', 'last_name': 'Flintstone',
                         'address': '201 Cobblestone Lane', 'city': 'Bedrock City'}

    for key in address_book.keys():
        print(address_book[key])

    # Try to remove an entry that doesn't exist
    old_address = address_book.pop(555, 'Entry not found')
    print("Removed address:", old_address)
    # Remove an entry using pop
    old_address = address_book.pop(222, 'Entry not found')
    print("Removed address:", old_address)

    for key in address_book.keys():
        print(address_book[key])

    # Remove an entry
    del address_book[333]

    print(address_book)
