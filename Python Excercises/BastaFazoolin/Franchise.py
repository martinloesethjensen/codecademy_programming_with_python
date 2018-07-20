class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __repr__(self):
        return "Address: {store}".format(store=self.address)

    # Compare the time with the starting and ending times from the menu objects in the list
    def comparison(self, time, other_start, other_end):
        if other_start <= time <= other_end:
            return True
        else:
            return False

    def available_menus(self, time):
        return [item for item in self.menus if Franchise.comparison(self, time, item.start_time, item.end_time)]
