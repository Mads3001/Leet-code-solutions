
# this is a movie rental implementation



# utilizing tuples, since it doesn't need to be mutable is a new way of thinking when storing something a in a particular order. It is a very smart solution.

from sortedcontainers import SortedList
# this is easier when sorting by price. Searches become much faster.

class MovieRentingSystem:

    def __init__(self, n: int, entries: list[list[int]]): # this should create a list of each rental shop and all their stock. A movie shop only has at maximum one copy of a movie.
        # n is the amount of shops. Entries are the corresponding movies in that shop.
        self.rented_movies = set() # keeps track of the rented movies. 
        self.shop_stock = {} # this should create a key for each movie and connect the movie to the price and shop.
        self.movies = {} # this should create a key for a movie and then make a sorted list for all the prices. That way the cheapest can easily be found.

        for shop, movie, price in entries: # this created an entry of a movie in the specific shop and in the list of prices for that certain movie.
            self.movies[(shop, movie)] = price # the shop and movie will be connected to a price
            if movie not in self.shop_stock: # if the movie is not connected to a shop, then it is created and now marked as existing in that shop.
                self.shop_stock[movie] = SortedList() # a sorted list is used instead of a normal list
            self.shop_stock[movie].add((price, shop)) # a tuple of the price and movie is inserted in the list.
        
        #for movie in self.shop_stock: OPTIANAL SINCE SORTEDLIST IS USED INSTEAD
        #    self.shop_stock[movie].sort() # all the movies are now sorted by price in each shop. A sorted list could be used instead



    def search(self, movie: int) -> list[int]: # this should return the 5 shops with the cheapest rental of a movie in stock. The shop should be sorted by price in ascending order.
        # if two shops have the same price, then the shop with the lowest "shop number" should be first
        # the list should return all the shops, if less than 5 unrented movie copies exist.
        result = [] # the list of shops
        for price, shop in self.shop_stock.get(movie, []): # this will retrieve the price and shop for each off the specified movie.
            if (shop, movie) not in self.rented_movies: # this checks, if the movie is rented.
                result.append(shop) # if it isn't rented, then it adds the shop to the list. 
            if len(result) == 5: # if there are 5 shops listed, then the result is returned
                break
        return result

        

    def rent(self, shop: int, movie: int) -> None:
        # this should rent a copy of a movie from a shop and mark it as rented.
        self.rented_movies.add((shop, movie)) # it is now added to rented_movies and can't show up in search
        

    def drop(self, shop: int, movie: int) -> None:
        # this should return a copy of a movie to the shop it was rented from.
        self.rented_movies.discard((shop, movie)) # both .remove and .discard can be used, since there can only be one.
        

    def report(self) -> list[list[int]]:
        # this lists the 5 cheapest movies that are currently rented out. the list should be sorted by ascending price. If there's a tie, then the "shop number" is the deciding factor.
        # if there's still a tie, then the movie number is the deciding factor.
        rented_list = SortedList()

        for shop, movie in self.rented_movies: # checks in the rented movies
            price = self.movies[(shop, movie)] # this retrieves the price from the other dictionary. It is connected to the shop and movie
            rented_list.add((price, shop, movie)) # adds the price to the rented list
        
        # the rented list is now full of the five cheapest prices.
        return [[shop, movie] for price, shop, movie in rented_list[:5]] # this should return all elements up to index 5.
    
# this solution is made from:
# my implementation utilized sorted lists, which should make it marginally faster.

class MovieRentingSystem:

    def __init__(self, n: int, entries: list[list[int]]):
        self.available = {}  # (shop, movie) -> price
        self.movie_shops = {}  # movie -> list of (price, shop)
        self.rented = set()  # (shop, movie) that are currently rented

        for shop, movie, price in entries:
            self.available[(shop, movie)] = price
            if movie not in self.movie_shops:
                self.movie_shops[movie] = []
            self.movie_shops[movie].append((price, shop))

        # Sort shops by price for each movie initially
        for movie in self.movie_shops:
            self.movie_shops[movie].sort()

    def search(self, movie: int) -> list[int]:
        result = []
        for price, shop in self.movie_shops.get(movie, []):
            if (shop, movie) not in self.rented:
                result.append(shop)
            if len(result) == 5:
                break
        return result

    def rent(self, shop: int, movie: int) -> None:
        self.rented.add((shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        self.rented.discard((shop, movie))

    def report(self) -> list[list[int]]:
        rented_list = []
        for shop, movie in self.rented:
            price = self.available[(shop, movie)]
            rented_list.append((price, shop, movie))

        rented_list.sort()
        return [[shop, movie] for price, shop, movie in rented_list[:5]]