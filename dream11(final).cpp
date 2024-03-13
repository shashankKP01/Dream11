#include <iostream>
#include <vector>
#include <algorithm>
#include <random>
#include <tuple>

using namespace std;

struct User {
    int user_id;
    int points;
};

vector<User> generate_users_with_points(int num_users) {
    vector<User> users;
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<int> dis(1, 1000);

    for (int user_id = 1; user_id <= num_users; ++user_id) {
        int points = dis(gen);
        users.push_back({user_id, points});
    }

    sort(users.begin(), users.end(), [](const User& a, const User& b) {
        return a.points > b.points;
    });

    users.resize(min(num_users, 25000));

    return users;
}

void generate_leaderboard_with_prizes(const vector<User>& top_users) {
    const vector<tuple<int, int, int>> prize_ranges = {
        {1, 1, 1000},
        {2, 2, 800},
        {3, 3, 500},
        {4, 5000, 250},
        {5001, 10000, 100},
        {10001, 15000, 50},
        {15001, 20000, 25},
        {20001, 25000, 10},
    };

    for (const auto& range : prize_ranges) {
        int start_rank = get<0>(range);
        int end_rank = get<1>(range);
        int prize_amount = get<2>(range);

        if (start_rank == end_rank) {
            cout << "Rank " << start_rank << "\tRs " << prize_amount << endl;
        } else {
            cout << "Rank " << start_rank << "-" << end_rank << "\tRs " << prize_amount << endl;
        }
    }
}

int main() {
    int num_users = 50000;
    const vector<User> top_users = generate_users_with_points(num_users);
    generate_leaderboard_with_prizes(top_users);
    return 0;
}