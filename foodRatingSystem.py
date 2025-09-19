import heapq
from typing import List


class FoodRatings:
    
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_to_info = {}
        
        self.cuisines_to_heap = {}
        
        for f, c, r in foods, cuisines, ratings:
            self.food_to_info[f] = [c, r]
            if c not in self.cuisines_to_heap:
                self.cuisines_to_heap[c] = []
            heapq.heappush(self.cuisines_to_heap[c], (-r, f))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, _ = self.food_to_info[food]
        self.food_to_info[food][1] = newRating
        heapq.heappush(self.cuisines_to_heap[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisines_to_heap[cuisine]
        while heap:
            rating, name = heap[0]
            if -rating == self.food_to_info[name]:
                return name
            heapq.heappop(heap)



# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)