import random

def generate_users_with_points(num_users):
    users = []

    for user_id in range(1, num_users + 1):
        points = random.randint(1, 1000)
        users.append({'user_id': user_id, 'points': points})

    sorted_users = sorted(users, key=lambda x: x['points'], reverse=True)
    

    top_users = sorted_users[:25000]

    return top_users


num_users = 50000


top_users = generate_users_with_points(num_users)

def generate_leaderboard_with_prizes(top_users):

    prize_ranges = [(1,1,1000),(2,2,800),(3,3,500),(4, 5000, 250), (5001, 10000, 100), (10001, 15000, 50), (15001, 20000, 25), (20001, 25000, 10)]



    for start_rank, end_rank, prize_amount in prize_ranges:
        if start_rank == end_rank:
            print(f"Rank{start_rank}\tRs {prize_amount}")
        else:
            print(f"Rank{start_rank}-{end_rank}\tRs {prize_amount}")

final_leaderboard = generate_leaderboard_with_prizes(top_users)