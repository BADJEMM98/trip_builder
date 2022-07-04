from params import list_of_cities, list_prices

# City class
class City(object):
    """
    Stores City objects. Upon initiation, automatically appends itself to list_of_cities
    self.name: human readable name.
    self.price_to: dictionary of price to other cities (keys are city names, values are floats)
    """
    def __init__(self, name, x, y, price_to=None):
        # Name and coordinates:
        self.name = name
        self.x  = x
        self.y  = y
        # Appends itself to the global list of cities:
        list_of_cities.append(self)
        # Creates a dictionary of the distances to all the other cities (has to use a value so uses itself - always 0)
        self.price_to = {self.name:0.0}
        #self.price_to = list_prices[self.name]:0.0

        if price_to:
            self.price_to = price_to
 
    def get_travel_price(self): 
        '''
        self --> None
        the price of a trip from the
        city to all other cities in the global 
        list list_of_cities, and places these values 
        in a dictionary called self.price_to
        with city name keys and float values
        ''' 
        for city in list_of_cities:
            if city.name != self.name:
                #appel Ã  l'API des prix de trajets
                print(city.name)
                trip_price = list_prices[self.name][city.name]
                self.price_to[city.name] = trip_price
                
