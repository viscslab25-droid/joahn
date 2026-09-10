import random
import winsound
import time
t = time.perf_counter()
def cod_mythic_8(pulls, rarity,pull_print):
    
    c = 0
    i = 0
    items_copy = items.copy()
    weights_copy = weights.copy()
    for i in range(min(pulls, len(items_copy))):
        idx = random.choices(range(len(items_copy)), weights=weights_copy)[0]
        pull = items_copy.pop(idx)
        weights_copy.pop(idx)
        c += mg42_draw_cp[i+1]
        if pull[1] == rarity and pull_print == i+1:
            # print(f"Pull {i+1}: {pull[0]} ({pull[1]})")
            return 1,i+1,c
    return 0,i+1,c

mg42_draw_cp = {
    1: 10,
    2: 30,
    3: 50,
    4: 120,
    5: 200,
    6: 350,
    7: 520,
    8: 960,
    9: 1300,
    10: 2300
}
items = [
        ("Emote - Final Siege", "Epic"),
        ("Spray - Final Siege", "Epic"),
        ("Calling Card - Final Siege", "Legendary"),
        ("Charm - Final Siege", "Epic"),
        ("Backpack - Final Siege", "Epic"),
        ("Machete - Final Siege", "Epic"),
        ("MW11 - Final Siege", "Epic"),
        ("EMP - Final Siege", "Legendary"),
        ("Witch Warden - Final Siege", "Epic Operator"),
        ("MG42 - The Campaign", "Mythic"),
    ]

weights = [2900, 2800, 1100, 1000, 650, 550, 467, 400, 125, 8]

trials = 10**9
num_of_pulls = 2
rarity = "Mythic"

success = 0
total_cp = 0
full_draw_cp = sum(mg42_draw_cp.values())
for _ in range(trials):
    _,pull, cp = cod_mythic_8(10, rarity,num_of_pulls)

    if pull <= num_of_pulls:
        success += 1
        total_cp += cp
    else:
        total_cp += full_draw_cp

chance = success / trials * 100
avg_cp = total_cp / trials

print(f"{chance:.3f}%")
print(f"{avg_cp:,.2f} CP")
print(f"Time taken: {time.perf_counter() - t:.2f} seconds to run {trials:,} trials to find the desired item of {rarity} in {num_of_pulls} pulls.")
winsound.Beep(100, 2)