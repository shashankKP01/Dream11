import random
import heapq

def generate_users_with_points(num_users):
    users = [{'user_id': user_id, 'points': random.randint(1, 1000)} for user_id in range(1, num_users + 1)]
    return heapq.nlargest(25000, users, key=lambda x: x['points'])

def generate_leaderboard_with_dynamic_prizes(top_users, range_value,prize_amnt):

    users_per_range = len(top_users) // range_value

    prize_ranges = []

    start_rank = 4
    for _ in range(range_value):
        end_rank = min(start_rank + users_per_range - 1, len(top_users))
        prize_ranges.append((start_rank, end_rank+1))
        start_rank = end_rank + 1


    for idx, (start_rank, end_rank) in enumerate(prize_ranges, start=2):
        prize_amount = prize_amnt // (2 ** idx)
        if start_rank == end_rank:
            print(f"Rank {start_rank}\tRs {prize_amount}")
        else:
            print(f"Rank {start_rank}-{end_rank}\tRs {prize_amount}")

num_users = 50000
range_value = 5
prize_amnt=20000
top_users = generate_users_with_points(num_users)
generate_leaderboard_with_dynamic_prizes(top_users, range_value,prize_amnt)
