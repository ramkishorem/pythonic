"""
Drill 2: Persistent high score board

Write the high_scores module for the following code to execute as intended

"""

from high_scores import HighScores

mario = HighScores('Super Mario', 'super-mario.txt')


# Execution 1
mario.post_score('Steve', 3432)
mario.post_score('Lara', 4376)
mario.post_score('Mike', 4899)

print(mario.get_top_5())
# Output
# [('Mike', 4899), ('Lara', '4376'), ('Steve', 3432)]
# super-mario.txt #######
# Steve, 3432
# Lara, 4376
# Mike, 4899


# Execution 2
mario.post_score('Wendy', 4122)
mario.post_score('Tom', 5212)
mario.post_score('Winston', 4777)

print(mario.get_top_5())
# Output
# [('Tom', 5212), ('Mike', 4899), ('Winston', 4777), ('Lara', 4376), ('Wendy', 4122)]
# super-mario.txt #######
# Steve, 3432
# Lara, 4376
# Mike, 4899
# Wendy, 4122
# Tom, 5212
# Winston, 4777