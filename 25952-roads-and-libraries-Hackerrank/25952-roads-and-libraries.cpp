#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

/*
 * Complete the 'roadsAndLibraries' function below.
 *
 * The function is expected to return a LONG_INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. INTEGER c_lib
 *  3. INTEGER c_road
 *  4. 2D_INTEGER_ARRAY cities
 */

long roadsAndLibraries(int n, int c_lib, int c_road, vector<vector<int>> cities) {

    // If building a road costs as much as or more than a library,
    // simply build a library in every city.
    if (c_road >= c_lib) {
        return 1LL * n * c_lib;
    }

    // Adjacency list
    vector<vector<int>> adj(n + 1);

    for (const auto &edge : cities) {
        int u = edge[0];
        int v = edge[1];

        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<bool> visited(n + 1, false);

    long long totalCost = 0;

    // Find all connected components
    for (int city = 1; city <= n; city++) {

        if (visited[city]) {
            continue;
        }

        // Every connected component needs exactly one library
        totalCost += c_lib;

        queue<int> q;
        q.push(city);
        visited[city] = true;

        while (!q.empty()) {

            int node = q.front();
            q.pop();

            for (int neighbor : adj[node]) {

                if (!visited[neighbor]) {

                    visited[neighbor] = true;
                    q.push(neighbor);

                    // One road connects this new city
                    totalCost += c_road;
                }
            }
        }
    }

    return totalCost;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string q_temp;
    getline(cin, q_temp);

    int q = stoi(ltrim(rtrim(q_temp)));

    for (int q_itr = 0; q_itr < q; q_itr++) {

        string first_multiple_input_temp;
        getline(cin, first_multiple_input_temp);

        vector<string> first_multiple_input =
            split(rtrim(first_multiple_input_temp));

        int n = stoi(first_multiple_input[0]);
        int m = stoi(first_multiple_input[1]);
        int c_lib = stoi(first_multiple_input[2]);
        int c_road = stoi(first_multiple_input[3]);

        vector<vector<int>> cities(m);

        for (int i = 0; i < m; i++) {

            cities[i].resize(2);

            string cities_row_temp_temp;
            getline(cin, cities_row_temp_temp);

            vector<string> cities_row_temp =
                split(rtrim(cities_row_temp_temp));

            for (int j = 0; j < 2; j++) {

                int cities_row_item =
                    stoi(cities_row_temp[j]);

                cities[i][j] = cities_row_item;
            }
        }

        long result =
            roadsAndLibraries(n, c_lib, c_road, cities);

        fout << result << "\n";
    }

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