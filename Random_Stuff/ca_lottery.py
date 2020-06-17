from random import choice

"""
Models the CA Lottery Straight Bet
----------------------------------

In Straight Bet order does matter
Box bet order doesn't matter
"""


def straight_bet(games=10, nums=9):
 non_unique_nums = []
 unique_nums = [x for x in range(nums + 1)]
 random_num_one = choice(unique_nums)
 random_num_two = choice(unique_nums)
 random_num_three = choice(unique_nums)
 non_unique_nums.extend([random_num_one, random_num_two, random_num_three])
 unique_nums.remove([random_num_one, random_num_two])
 unique_nums.remove(random_num_two)
 unique_nums.remove(random_num_three)
 for x in games:
  print('{} {} {}'.format(random_num_one, random_num_two, random_num_three))


 # rand_one = randint(0, 9)
 #  rand_two = randint(0, 9)
 #  rand_three = randint(0, 9)
 # print('{} {} {}'.format(rand_one, rand_two, rand_three))
