
class Flowers:
    def __init__(self, name: str, color: str, bud_size: str, petals_number: int, price_usd: float, life_time: int, stem_length: int):
        self.__name = name
        self.__color = color
        self.bud_size = bud_size
        self.petals_number = petals_number
        self.__price_usd = price_usd
        self.__life_time = life_time
        self.stem_length = stem_length

    @property
    def name(self):
        return self.__name

    @property
    def color(self):
        return self.__color

    @property
    def price_usd(self):
        return self.__price_usd

    @property
    def life_time(self):
        return self.__life_time

class Wild_Flowers(Flowers):
    def __init__(self, name, color, bud_size, petals_number, price_usd, life_time, stem_length):
        super().__init__(name, color, bud_size, petals_number, price_usd, life_time, stem_length)
        self.wild = True
        self.exotic = False

class Domesticated_Flowers(Flowers):
    def __init__(self, name, color, bud_size, petals_number, price_usd, life_time, stem_length):
        super().__init__(name, color, bud_size, petals_number, price_usd, life_time, stem_length)
        self.wild = False
        self.exotic = False

class Bouquet:
    def __init__(self, *args):
        self.flowers = []
        for i in range(len(args)):
            self.flowers.append(vars(args[i]))
        self.price = self.calculate_price()
        self.avg_wilting = self.wilting_time()

    def calculate_price(self):
        price = 0
        for i in range (len(self.flowers)):
            print(self.flowers[i])
            price += (self.flowers[i]["_Flowers__price_usd"])
        return f"Bouqet price: {price} $."

    def wilting_time(self):
        days = 0
        counter = 0
        for i in range (len(self.flowers)):
            days += (self.flowers[i]["_Flowers__life_time"])
            counter += 1
        avg_wilting_time = days / counter
        return f"Bouquet average life: {avg_wilting_time} days."


    def __sort_fresh(flower):
        return flower['_Flowers__life_time']

    @property
    def freshness(self):
        self.flowers.sort(key=lambda flower: self.__sort_fresh(flower))
        print(self.flowers)


ghost_orchid = Wild_Flowers("Ghost Orchid", "Beige", "Big", 5, 55, 15, 3)
ghost_orchid.exotic = True

carson_rose = Domesticated_Flowers("Scarlet Carson Rose", "Scarlet", "Big",
                                   35, 10, 7, 180)

pink_tulip = Domesticated_Flowers("Pink Tulip", "Pink", "Middle", 12, 2, 5, 40)

french_lavender = Domesticated_Flowers("Lavender", "Violet", "Big", 5, 7, 30, 55)


my_buquet = Bouquet(ghost_orchid, carson_rose, pink_tulip, french_lavender)
print(my_buquet.price)
print(my_buquet.avg_wilting)
my_buquet.freshness()