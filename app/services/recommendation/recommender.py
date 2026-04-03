from typing import List

# Sample static recommendations (can be dynamic later)
ACTIVITIES = {
    "family": ["Kids' Pool", "Family Safari", "Local Village Tour", "Family Movie Night", "Mini Golf"],
    "solo": ["Spa", "Yoga Class", "Hiking Tour", "Meditation Session", "Reading Lounge"],
    "business": ["Business Center", "Conference Room", "High-Speed WiFi Lounge", "Quiet Workspace"],
    "couple": ["Romantic Dinner", "Sunset Cruise", "Wine Tasting", "Couples Massage"]
}

FOOD_OPTIONS = {
    "spicy": ["Spicy Tibs", "Berbere Chicken", "Spicy Lentil Stew", "Szechuan Noodles"],
    "mild": ["Injera with Veggies", "Mild Doro Wat", "Cheese Platter", "Butter Chicken"],
    "vegetarian": ["Vegetarian Thali", "Farm-to-table Salad", "Plant-based Burger"],
    "vegan": ["Vegan Bowl", "Quinoa Salad", "Plant-based Options"],
    "any": ["Chef's Choice", "Local Favorites", "International Buffet", "24/7 Room Service"]
}


# Make them async to match what guest.py expects
async def recommend_activities(travel_type: str, past_activities: List[str] = []) -> List[str]:
    """
    Return personalized activities, avoiding repeated items in history
    """
    activities = ACTIVITIES.get(travel_type, ACTIVITIES.get("solo", []))
    # Filter out already recommended activities
    new_activities = [a for a in activities if a not in past_activities]
    return new_activities[:3]  # max 3 recommendations


async def recommend_food(food_pref: str, past_foods: List[str] = []) -> List[str]:
    """
    Return personalized food options
    """
    foods = FOOD_OPTIONS.get(food_pref, FOOD_OPTIONS.get("any", []))
    # Filter out already recommended foods
    new_foods = [f for f in foods if f not in past_foods]
    return new_foods[:3]  # max 3 recommendations