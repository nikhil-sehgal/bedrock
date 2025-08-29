import datetime

class TravelPlannerAgent:
    def __init__(self, destination, days):
        self.destination = destination
        self.days = days

    def plan_trip(self):
        itinerary = []
        for i in range(1, self.days + 1):
            itinerary.append(f"Day {i}: Explore {self.destination}, visit top attractions, try local food.")
        return itinerary

if __name__ == "__main__":
    planner = TravelPlannerAgent("New York", 3)
    trip = planner.plan_trip()
    print("AI Travel Itinerary:")
    for day in trip:
        print(day)
