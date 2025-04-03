#include <iostream>
#include <deque>
#include <vector>
#include <tuple>
#include <string>

using namespace std;

int main() {
    int N;
    cin >> N;
    vector<vector<int>> house(N, vector<int>(N));

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> house[i][j];
        }
    }

    deque<tuple<int, int, string>> deq;
    deq.push_back({0, 1, "garo"});
    int cnt = 0;

    while (!deq.empty()) {
        auto [x, y, pos] = deq.front(); // C++17 structured binding
        deq.pop_front();

        if (x == N - 1 && y == N - 1) {
            cnt++;
            continue;
        }

        // 대각선 이동
        if (x + 1 < N && y + 1 < N &&
            house[x][y + 1] == 0 &&
            house[x + 1][y] == 0 &&
            house[x + 1][y + 1] == 0) {
            deq.push_back({x + 1, y + 1, "daegak"});
        }

        // 가로 → 가로
        if (pos == "garo") {
            if (y + 1 < N && house[x][y + 1] == 0) {
                deq.push_back({x, y + 1, "garo"});
            }
        }

        // 세로 → 세로
        else if (pos == "sero") {
            if (x + 1 < N && house[x + 1][y] == 0) {
                deq.push_back({x + 1, y, "sero"});
            }
        }

        // 대각선 → 가로, 세로
        else if (pos == "daegak") {
            if (y + 1 < N && house[x][y + 1] == 0) {
                deq.push_back({x, y + 1, "garo"});
            }
            if (x + 1 < N && house[x + 1][y] == 0) {
                deq.push_back({x + 1, y, "sero"});
            }
        }
    }

    cout << cnt << endl;
    return 0;
}