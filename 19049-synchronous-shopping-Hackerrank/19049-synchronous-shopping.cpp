#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

/*
 * Complete the 'shop' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. INTEGER k
 *  3. STRING_ARRAY centers
 *  4. 2D_INTEGER_ARRAY roads
 */

int shop(int n, int k, vector<string> centers, vector<vector<int>> roads) {

    // fishMask[i] stores which fish types are available
    // at shopping center i.
    vector<int> fishMask(n);

    for (int i = 0; i < n; i++) {
        stringstream ss(centers[i]);

        int count;
        ss >> count;

        int mask = 0;

        for (int j = 0; j < count; j++) {
            int fish;
            ss >> fish;

            mask |= (1 << (fish - 1));
        }

        fishMask[i] = mask;
    }

    // Build graph
    vector<vector<pair<int, int>>> adj(n);

    for (const auto &road : roads) {
        int u = road[0] - 1;
        int v = road[1] - 1;
        int time = road[2];

        adj[u].push_back({v, time});
        adj[v].push_back({u, time});
    }

    int totalMasks = 1 << k;

    const long long INF = LLONG_MAX / 4;

    // dist[city][mask] = minimum time required to reach
    // city while having collected fish represented by mask.
    vector<vector<long long>> dist(
        n,
        vector<long long>(totalMasks, INF)
    );

    // {distance, {city, mask}}
    using State = pair<long long, pair<int, int>>;

    priority_queue<
        State,
        vector<State>,
        greater<State>
    > pq;

    int startMask = fishMask[0];

    dist[0][startMask] = 0;

    pq.push({
        0,
        {0, startMask}
    });

    // Dijkstra
    while (!pq.empty()) {

        long long currentDist = pq.top().first;
        int city = pq.top().second.first;
        int mask = pq.top().second.second;

        pq.pop();

        if (currentDist != dist[city][mask]) {
            continue;
        }

        for (auto edge : adj[city]) {

            int nextCity = edge.first;
            int weight = edge.second;

            int newMask = mask | fishMask[nextCity];

            long long newDist =
                currentDist + weight;

            if (newDist < dist[nextCity][newMask]) {

                dist[nextCity][newMask] = newDist;

                pq.push({
                    newDist,
                    {nextCity, newMask}
                });
            }
        }
    }

    int fullMask = totalMasks - 1;

    long long answer = INF;

    // Both cats must reach shopping center n.
    // Together their fish masks must contain every fish type.
    for (int mask1 = 0; mask1 < totalMasks; mask1++) {

        if (dist[n - 1][mask1] == INF) {
            continue;
        }

        for (int mask2 = mask1; mask2 < totalMasks; mask2++) {

            if (dist[n - 1][mask2] == INF) {
                continue;
            }

            if ((mask1 | mask2) == fullMask) {

                long long timeTaken = max(
                    dist[n - 1][mask1],
                    dist[n - 1][mask2]
                );

                answer = min(answer, timeTaken);
            }
        }
    }

    return (int)answer;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string first_multiple_input_temp;
    getline(cin, first_multiple_input_temp);

    vector<string> first_multiple_input =
        split(rtrim(first_multiple_input_temp));

    int n = stoi(first_multiple_input[0]);

    int m = stoi(first_multiple_input[1]);

    int k = stoi(first_multiple_input[2]);

    vector<string> centers(n);

    for (int i = 0; i < n; i++) {
        string centers_item;
        getline(cin, centers_item);

        centers[i] = centers_item;
    }

    vector<vector<int>> roads(m);

    for (int i = 0; i < m; i++) {

        roads[i].resize(3);

        string roads_row_temp_temp;
        getline(cin, roads_row_temp_temp);

        vector<string> roads_row_temp =
            split(rtrim(roads_row_temp_temp));

        for (int j = 0; j < 3; j++) {

            int roads_row_item =
                stoi(roads_row_temp[j]);

            roads[i][j] = roads_row_item;
        }
    }

    int res = shop(n, k, centers, roads);

    fout << res << "\n";

    fout.close();

    return 0;
}

string ltrim(const string &str)
{
    string s(str);

    s.erase(
        s.begin(),
        find_if(
            s.begin(),
            s.end(),
            [](unsigned char ch) {
                return !isspace(ch);
            }
        )
    );

    return s;
}

string rtrim(const string &str)
{
    string s(str);

    s.erase(
        find_if(
            s.rbegin(),
            s.rend(),
            [](unsigned char ch) {
                return !isspace(ch);
            }
        ).base(),
        s.end()
    );

    return s;
}

vector<string> split(const string &str)
{
    vector<string> tokens;

    string::size_type start = 0;
    string::size_type end = 0;

    while ((end = str.find(" ", start)) != string::npos) {

        if (end > start) {
            tokens.push_back(
                str.substr(start, end - start)
            );
        }

        start = end + 1;
    }

    if (start < str.length()) {
        tokens.push_back(str.substr(start));
    }

    return tokens;
}


// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna