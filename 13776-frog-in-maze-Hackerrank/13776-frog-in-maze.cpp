#include "bits/stdc++.h"
using namespace std;
#define rep(i,n) for(int (i)=0;(i)<(int)(n);++(i))
#define rer(i,l,u) for(int (i)=(int)(l);(i)<=(int)(u);++(i))
#define reu(i,l,u) for(int (i)=(int)(l);(i)<(int)(u);++(i))
static const int INF = 0x3f3f3f3f; static const long long INFL = 0x3f3f3f3f3f3f3f3fLL;
typedef vector<int> vi; typedef pair<int, int> pii; typedef vector<pair<int, int> > vpii; typedef long long ll;
template<typename T, typename U> static void amin(T &x, U y) { if (y < x) x = y; }
template<typename T, typename U> static void amax(T &x, U y) { if (x < y) x = y; }

int main() {
    int H; int W; int K;
    while (~scanf("%d%d%d", &H, &W, &K)) {
        vector<string> maze(H);
        rep(i, H) {
            char buf[101];
            scanf("%s", buf);
            maze[i] = buf;
        }
        vector<int> tunnel(H * W, -1);
        rep(i, K) {
            int y1; int x1; int y2; int x2;
            scanf("%d%d%d%d", &y1, &x1, &y2, &x2), -- y1, -- x1, -- y2, -- x2;
            int u = y1 * W + x1, v = y2 * W + x2;
            tunnel[u] = v;
            tunnel[v] = u;
        }
        vector<vector<pair<int, double>>> gw(H * W);
        rep(i, H) rep(j, W) {
            int u = i * W + j;
            if (!strchr("#*%", maze[i][j])) {
                static const int dy[4] = { 0, 1, 0, -1 }, dx[4] = { 1, 0, -1, 0 };
                for (int d = 0; d < 4; ++ d) {
                    int yy = i + dy[d], xx = j + dx[d];
                    if (yy < 0 || yy >= H || xx < 0 || xx >= W) continue;
                    if (maze[yy][xx] == '#') continue;
                    int v = yy * W + xx;
                    if (tunnel[v] != -1)
                        v = tunnel[v];
                    gw[u].emplace_back(v, 1.);
                }
            }
            if (gw[u].empty()) {
                gw[u].emplace_back(u, 1.);
            } else {
                for(auto &p : gw[u])
                    p.second /= (int)gw[u].size();
            }
        }
        //(1 - A)^{-1} c
        typedef double Num;
        vector<vector<Num>> A(H * W, vector<Num>(H * W)), B = A;
        rep(u, H * W) for (auto e : gw[u])
            A[u][e.first] += e.second;
        rep(iter, 20) {
            rep(i, H * W) rep(j, H * W) {
                Num x = 0;
                rep(k, H * W)
                    x += A[i][k] * A[k][j];
                if (x < 1e-20)
                    x = 0;
                B[i][j] = x;
            }
            A.swap(B);
        }
        double ans = 0;
        rep(i, H) rep(j, W) if (maze[i][j] == 'A')
            rep(k, H) rep(l, W) if(maze[k][l] == '%')
                ans += A[i * W + j][k * W + l];
        printf("%.10f\n", ans);
    }
    return 0;
}


// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna