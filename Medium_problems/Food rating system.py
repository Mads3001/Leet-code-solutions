
# the rating system is based on the class with "FoodRatings(String[] foods, String[] cuisines, int[] ratings)"


# we can start off by creating a dataclass called "food"






class FoodRatings:

    
    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]): # this should create the system and insert the data for each food.
        self.food

        # we need to have the rating tied to the food, so we can change the rating.


    def changeRating(self, food: str, newRating: int) -> None: # this should change the rating of a food object.
        pass
    def highestRated(self, cuisine: str) -> str: # this should return the highest highest score of a food in the given cuisine.
        pass


# I simply do not know enough to implement a data structure.




# this is the best solution from the internet. It makes sense, but I can't do it yet.
import heapq

class FoodRatings:
    def __init__(self, foods, cuisines, ratings):
        self.food_to_cuisine = {}
        self.food_to_rating = {}
        self.cuisine_foods = {}

        for f, c, r in zip(foods, cuisines, ratings):
            self.food_to_cuisine[f] = c
            self.food_to_rating[f] = r
            if c not in self.cuisine_foods:
                self.cuisine_foods[c] = []
            heapq.heappush(self.cuisine_foods[c], (-r, f))

    def changeRating(self, food, newRating):
        cuisine = self.food_to_cuisine[food]
        self.food_to_rating[food] = newRating
        heapq.heappush(self.cuisine_foods[cuisine], (-newRating, food))

    def highestRated(self, cuisine):
        heap = self.cuisine_foods[cuisine]
        while heap:
            rating, food = heap[0]
            if -rating == self.food_to_rating[food]:
                return food
            heapq.heappop(heap)




