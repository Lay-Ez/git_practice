import datetime

# Create class menu

class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = datetime.time(start_time)
    self.end_time = datetime.time(end_time)
  def __repr__(self):
    return "{name} is served between {start} and {end} o'clock".format(name = self.name, start = self.start_time.hour, end = self.end_time.hour)
  def calculate_bill(self, purchased_items):
      total_price = 0
      for item in purchased_items:
          total_price += self.items[item]
      return total_price

#Creates different menus

brunch = Menu("Brunch menu", {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}, 11, 16)

early_bird = Menu("Early-bird menu", {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}, 15, 18)

dinner = Menu("Dinner", {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}, 17, 23)

kids = Menu("Kids menu", {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}, 11, 21)

arepas_menu = Menu("Take a' Arepa", {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}, 10, 20)

#Creates class Franchise

class Franchise:
    def __init__(self, adress, menus):
        self.adress = adress
        self.menus = menus
    def __repr__(self):
        return str(self.adress)
    def available_menus(self, time):
        avail_menus = list([])
        for menu in self.menus:
            if time < menu.end_time.hour and time >= menu.start_time.hour:
                avail_menus.append(menu.name)
        if len(avail_menus) == 0:
            return "There are no available menus at {}".format(time)
        else:
            new_string = "These menus are available at {} : \n   {}.".format(time, avail_menus)
            new_string = new_string.replace("[", "")
            new_string = new_string.replace("]", "")
            new_string = new_string.replace("'", "")
            new_string = new_string.replace("'", "")
            return new_string
#Creates class Business

class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises
    def __repr__(self):
        new_string =  "Franchise \"{}\" is covering: {}".format(self.name, self.franchises)
        new_string = new_string.replace("[", "")
        new_string = new_string.replace("]", "")
        return new_string

#Creates different places

flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])
new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

#Creates businesses

basta_fazoolin = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])
arepa_business = Business("Take a' Arepa!", [arepas_place])

#print(basta_fazoolin)
#print(arepa_business)

print(flagship_store.available_menus(17))
