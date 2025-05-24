def get_input():
    items = []
    weights = []
    profits = []
    n = int(input("how many items pookie? "))
    for i in range(n):
        print("\n\nitem " + str(i + 1) + ":")
        weight = int(input("     enter weight: "))
        profit = int(input("     enter profit: "))
        items.append(i + 1)
        weights.append(weight)
        profits.append(profit)
    capacity = int(input("\nbag capacity love?\n "))
    return items, weights, profits, capacity

def bruteforce_knapSack(capacity, weights, profits, n):
    if n == 0 or capacity == 0:
        return 0, []
    if weights[n-1] > capacity:
        return bruteforce_knapSack(capacity, weights, profits, n-1)
    else:
        profit_incl, items_incl = bruteforce_knapSack(capacity - weights[n-1], weights, profits, n-1)
        profit_incl += profits[n-1]

        profit_excl, items_excl = bruteforce_knapSack(capacity, weights, profits, n-1)

        if profit_incl > profit_excl:
            return profit_incl, items_incl + [n-1]
        else:
            return profit_excl, items_excl

def dp_knapsack(items, weights, profits, capacity):
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(profits[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    chosen_indexes = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            chosen_indexes.append(i - 1)
            w -= weights[i - 1]
    chosen_indexes.reverse()

    max_profit = dp[n][capacity]
    return max_profit, chosen_indexes

def greedy_knapsack(weights, profits, capacity):
    indexed_items = list(zip(weights, profits, range(len(weights))))
    indexed_items.sort(key=lambda x: (x[1]/x[0] if x[0] > 0 else 0), reverse=True)

    total_profit = 0
    selected_items = []
    remaining = capacity

    for w, p, idx in indexed_items:
        if w <= 0:
            continue
        if w <= remaining:
            selected_items.append(idx)
            total_profit += p
            remaining -= w

    return total_profit, selected_items

def print_result(name, max_profit, chosen_indexes, items, weights, profits, complexity=None):
    print(f"\nMax profit you can get with {name}: ${max_profit}")
    if complexity:
        print(f"Time Complexity: {complexity}")
    print("Selected Items:")
    for i in chosen_indexes:
        print(f"   Item {items[i]}:")
        print(f"       Weight = {weights[i]}")
        print(f"       Profit = {profits[i]}")
    print("-" * 40)

# Main program
items, weights, profits, capacity = get_input()

n = len(weights)

bf_profit, bf_chosen = bruteforce_knapSack(capacity, weights, profits, n)
dp_profit, dp_chosen = dp_knapsack(items, weights, profits, capacity)
gr_profit, gr_chosen = greedy_knapsack(weights, profits, capacity)

print_result("Brute Force", bf_profit, bf_chosen, items, weights, profits, "O(2^n)")
print_result("Dynamic Programming", dp_profit, dp_chosen, items, weights, profits, "O(n * W)")
print_result("Greedy", gr_profit, gr_chosen, items, weights, profits, "O(n log n)")