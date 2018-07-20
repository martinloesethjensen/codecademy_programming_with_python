class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return "Menu Name: {name}\nItems To Order: {items}\nTime Available: {st} to {et}" \
            .format(name=self.name, items=self.items, st=self.start_time, et=self.end_time)

    # Method to calculate the order
    def calculate_bill(self, purchased_items):
        total = 0 # initializing a variable

        # for each item in the order list
        for item in purchased_items:

            # if the item exists in the menu dictionary
            if item in self.items:

                # get the value from the dictionary and add to the variable
                total += self.items.get(item)
        return total

