def estimate_budget(days):
    # Dynamic values based on day count
    stay = days * 1200
    food = days * 800
    transport = days * 500
    misc = 2000
    
    return {
        "Accommodation": stay,
        "Food & Dining": food,
        "Transport": transport,
        "Activities": misc,
        "Total": stay + food + transport + misc
    }