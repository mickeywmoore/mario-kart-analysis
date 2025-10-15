def best_items(racers):
    """
    Given a list of racer dictionaries, return a dictionary mapping items
    to the number of times they were used by first-place finishers.
    """
    winner_item_counts = {}
    for racer in racers:
        if racer['finish'] == 1:
            for item in racer['items']:
                winner_item_counts[item] = winner_item_counts.get(item, 0) + 1
    return winner_item_counts

# Sample dataset to test our function
sample_data = [
    {'name': 'Peach', 'items': ['green shell', 'banana', 'green shell'], 'finish': 3},
    {'name': 'Bowser', 'items': ['green shell'], 'finish': 1},
    {'name': None, 'items': ['mushroom'], 'finish': 2},
    {'name': 'Toad', 'items': ['green shell', 'mushroom'], 'finish': 1},
]

# Call the function and print the result
print("Analyzing Mario Kart race data...")
item_counts = best_items(sample_data)
print(f"Items used by first-place finishers: {item_counts}")