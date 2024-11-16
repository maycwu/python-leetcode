#Statement

# A recruiter plans to hire n people and conducts their interviews at two different locations of the company.
# He evaluates the cost of inviting candidates to both these locations. The plan is to invite 50% at one location,
# and the rest at the other location, keeping costs to a minimum.

# You need to determine the minimum cost to invite all the candidates for the interview such that exactly
# n/2 people are invited in each city.


# What is the minimum cost to invite every person to two different cities such that the same number of people arrive in each city if the costs are as follows?
#
# [10, 15], [10, 20], [10, 25], [10, 30]?
#
# Output: 55 (Inviting the third and fourth person to City A and the first and second person to City B minimizes the cost. 10 + 10 + 15 + 20 = 55)
#
# What is the minimum cost to invite every person to two different cities such that the same number of people arrive in each city if the costs are as follows?
#
# [1, 2], [2, 1], [1, 3], [4, 1]?
#
# Output: 4 (Inviting the first and third person to City A and the second and fourth person to City B minimizes the cost. 1 + 1 + 1 + 1 = 4)


def two_city_scheduling(costs):
    # Initialize the total cost to 0
    total_cost = 0
    # Sort the costs list in ascending order based on the difference
    # between the costs of sending someone to city A vs city B
    costs.sort(key = lambda x : x[0] - x[1])
    # Get the length of the costs list
    cost_length = len(costs)
    # For each pair of cities, add the cost of sending one person to city A and the other person to city B to the total cost
    for i in range(cost_length//2):
        total_cost = total_cost + costs[i][0] + costs[cost_length-i-1][1];
    # Return the total cost
    return total_cost

# Driver code
def main():
    input_costs = [
        [[10, 20], [30, 200], [400, 50], [30, 20]],
        [[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]],
        [[515, 563], [451, 713], [537, 709], [343, 819], [855, 779], [457, 60], [650, 359], [631, 42]],
        [[1, 2], [3, 4], [5, 6], [7, 8]],
        [[1, 2], [1, 2], [1, 2], [1, 2]],
        [[10, 100], [10, 1000], [50, 500], [1,100]]]

    for i in range(len(input_costs)):
        print(i + 1, "\tcosts: ",input_costs[i])
        print("\n\tThe minimum cost to send people equally into city A and B is:", two_city_scheduling(input_costs[i]))
        print("-" * 100)


if __name__ == '__main__':
    main()
