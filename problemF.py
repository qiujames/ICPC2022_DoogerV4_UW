import sys

n_line = sys.stdin.readline().split()
n = int(n_line[0])
my_list = [int(elem) for elem in sys.stdin.readline().strip().split()]
list_of_lists = []
for x in range(n - 1):
    values = sys.stdin.readline().strip().split()
    list_of_lists.append([int(elem) for elem in values])



# Calculate probability that everyone ties (so that's a win)
probability_tie = {}
if (len(list_of_lists) > 2):
    for elem in list_of_lists[0]:
        probability_tie_on_elem = 1
        for other_list in list_of_lists[1:]:
            tie_counter = 0
            for other_elem in other_list:
                if other_elem == elem:
                    tie_counter += 1
            probability_tie_on_elem *= tie_counter

        if (elem not in probability_tie):
            probability_tie[elem] = 0
        probability_tie[elem] += probability_tie_on_elem
# print(probability_tie, "Tie chance")


max_probability = 0
max_number = my_list[0]

for my_num in my_list:
    total_prob_win = 1
    total_prob_tie = 1
    for other_list in list_of_lists:
        prob_win = 0
        prob_tie = 0
        for elem in other_list:
            if my_num > elem:
                prob_win += 1
            elif my_num == elem:
                prob_tie += 1

        total_prob_win *= prob_win
        total_prob_tie *= prob_tie


    total_total = total_prob_win + total_prob_tie
    for elem in probability_tie:
        if (elem > my_num):
            total_total += probability_tie[elem]

    # print("probability", my_num, total_total)
    if total_total > max_probability:
        max_probability = total_total
        max_number = my_num

max_probability /= (5 ** (n - 1))

print(max_number)
print("%.5f" % max_probability)

#  Should output 1, probability 1
# 4
# 1 2 3 4 4
# 5 5 5 5 5
# 5 5 5 5 5
# 5 5 5 5 5

# Should also output 1, probability 1
# 4
# 1 2 3 4 5
# 5 5 5 5 5
# 5 5 5 5 5
# 5 5 5 5 5

