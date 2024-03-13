import random

def generate_users_with_points(num_users):
    users = [{'user_id': user_id, 'points': random.randint(1, 1000)} for user_id in range(1, num_users + 1)]
    return sorted(users, key=lambda x: x['points'], reverse=True)[:25000]

def generate_leaderboard_with_prizes(top_users):
    prize_ranges = [(1, 1, 1000), (2, 2, 800), (3, 3, 500), (4, 5000, 250), (5001, 10000, 100), (10001, 15000, 50),
                    (15001, 20000, 25), (20001, 25000, 10)]

    for start_rank, end_rank, prize_amount in prize_ranges:
        if start_rank == end_rank:
            print(f"Rank{start_rank}\tRs {prize_amount}")
        else:
            print(f"Rank{start_rank}-{end_rank}\tRs {prize_amount}")

num_users = 50000
top_users = generate_users_with_points(num_users)
generate_leaderboard_with_prizes(top_users)
