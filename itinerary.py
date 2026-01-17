from utils import ask_hf

def generate_itinerary(destination, days, budget, travel_style, interests, transport, group_size):
    # Format interests into a readable string
    interest_list = ", ".join(interests) if interests else "General Sightseeing"
    
    prompt = f"""
    Acting as a professional student travel consultant, create a highly detailed {days}-day itinerary for {destination}.
    
    Trip Details:
    - Group Size: {group_size} person(s)
    - Total Budget for the trip: {budget} INR
    - Travel Style: {travel_style}
    - Interests: {interest_list}
    - Preferred Transport: {transport}
    
    Please structure your response with:
    1. 'Day X:' bold headings.
    2. Specific student-friendly hostel or budget accommodation names.
    3. Daily breakdown: Morning, Afternoon, and Evening activities that focus on {interest_list}.
    4. At least 2 'Cheap Eats' (local food stalls or student cafes) per day.
    5. A 'Pro-Tip' for each day on how to save money or use {transport} effectively.
    6. Ensure one activity per day is completely free.
    
    Make the tone energetic, adventurous, and encouraging!
    """
    
    return ask_hf(prompt)