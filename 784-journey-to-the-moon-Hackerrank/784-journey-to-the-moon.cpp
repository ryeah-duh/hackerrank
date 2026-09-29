#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

/*
 * Complete the 'journeyToMoon' function below.
 *
 * The function returns the number of valid pairs of astronauts
 * belonging to different countries.
 */

long long journeyToMoon(int n, vector<vector<int>> astronaut) {

    vector<vector<int>> adj(n);

    // Build graph
    for (const auto &pair : astronaut) {
        int u = pair[0];
        int v = pair[1];

        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<bool> visited(n, false);
    vector<long long> countrySizes;

    // Find connected components
    for (int i = 0; i < n; i++) {

        if (visited[i]) {
            continue;
        }

        queue<int> q;
        q.push(i);
        visited[i] = true;

        long long size = 0;

        while (!q.empty()) {

            int node = q.front();
            q.pop();

            size++;

            for (int neighbor : adj[node]) {

                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    q.push(neighbor);
                }
            }
        }

        countrySizes.push_back(size);
    }

    // Count pairs belonging to different countries
    long long result = 0;
    long long remaining = n;

    for (long long size : countrySizes) {

        remaining -= size;

        result += size * remaining;
    }

    return result;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string first_multiple_input_temp;
    getline(cin, first_multiple_input_temp);

    vector<string> first_multiple_input =
        split(rtrim(first_multiple_input_temp));

    int n = stoi(first_multiple_input[0]);

    int p = stoi(first_multiple_input[1]);

    vector<vector<int>> astronaut(p);

    for (int i = 0; i < p; i++) {

        astronaut[i].resize(2);

        string astronaut_row_temp_temp;
        getline(cin, astronaut_row_temp_temp);

        vector<string> astronaut_row_temp =
            split(rtrim(astronaut_row_temp_temp));

        for (int j = 0; j < 2; j++) {

            int astronaut_row_item =
                stoi(astronaut_row_temp[j]);

            astronaut[i][j] = astronaut_row_item;
        }
    }

    long long result = journeyToMoon(n, astronaut);

    fout << result << "\n";

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