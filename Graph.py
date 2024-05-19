graph = {
    "Aman": ["R1", "R2"],
    "R1": ["C1", "R2", "Aman"],
    "R2": ["C1", "C2", "Aman"],
    "C1": ["R1", "C2", "R2"],
    "C2": ["C1", "R1", "R2"]
}

prep_times = {
    "R1":pt1,
    "R2":pt2
}

# speed in KMPH
average_speed = 20

