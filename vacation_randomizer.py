import random

JAPAN = "Japan"
SPAIN = "Spain"

count_metrics = {
    JAPAN: 0,
    SPAIN: 0,
}

years_since_japan_founded = 2023 + 660  # Japan was founded in 660 bc
years_since_spain_founded = 2023 - 1492  # Spain was founded in 1492

# Create list entries for how ever many years the country has existed
japan_entries = [JAPAN for i in range(years_since_japan_founded)]
spain_entries = [SPAIN for i in range(years_since_spain_founded)]

# Combine the lists and randomize the order
all_entries = japan_entries + spain_entries
random.shuffle(all_entries)
entry_count = len(all_entries)

chosen_log = []
for attempt in range(entry_count):
    # Choose a random value between one and the length of the combined list
    random_index = random.randint(0, entry_count - 1)
    chosen = all_entries[random_index]
    count_metrics[chosen] = count_metrics[chosen] + 1
    chosen_log.append(f"{chosen} has been chosen.")


print(f"After {entry_count} attempts, the last chosen value was {chosen}.")
print(f"SCOREBOARD: Japan: {count_metrics[JAPAN]}, Spain: {count_metrics[SPAIN]}")

for i, msg in enumerate(chosen_log):
    print(f"Attempt {i}:  {msg}")
