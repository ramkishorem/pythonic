"""
Drill 2: Game Over, High Scores

Let us build a high score tracking model for our game
(high_scores.py)

Multiple players could go head-to-head online.
So we should be able to post one or many scores.

Write the module so that the following function calls provide 
corresponding results
"""

####### do the right import here for the calls below

high_scores.post_scores(3430)
high_scores.post_scores(2320, 4210, 3070)

high_scores.view_top5()
# Output:
# 1. 4210
# 2. 3430
# 3. 3070
# 4. 2320


####### do a new import here for the calls below

post_scores(4540, 5100)
total_attempts()
# Output: 6


####### do a new import here for the calls below
post(3700)
top5()
# Output:
# 1. 5100
# 2. 4540
# 3. 4210
# 4. 3700
# 5. 3430
