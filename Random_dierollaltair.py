import random

import altair

trials = 600
dice_rolls = []

for i in range(trials):
    die_roll_1 = random.randrange(1,7)
    die_roll_2 = random.randrange(1,7)
    dice_sum = die_roll_1 + die_roll_2
    dice_rolls.append(dice_sum)
    
#print(dice_rolls)


data = altair.Data(rolls=dice_rolls)
chart = altair.Chart(data)
mark = chart.mark_bar()
X = altair.Axis("rolls:Q", bin=True)
Y = altair.Axis("count()")
enc = mark.encode(x=X,y=Y)
enc.display()
