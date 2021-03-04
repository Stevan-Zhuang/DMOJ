#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <string.h>
using namespace std;
#define MAXN 200001

vector<int> network[MAXN];
int min_dist[MAXN];
queue<int> Q;
int path[MAXN];
multiset<int> results;

int main() {
    cin.sync_with_stdio(0); cin.tie(0);

    int n_stations, n_paths, n_days;
    cin >> n_stations >> n_paths >> n_days;
    int a, b;
    for (int idx = 0; idx < n_paths; idx++) {
        cin >> a >> b;
        network[b].push_back(a);
    }
    for (int idx = 0; idx < n_stations; idx++) {
        min_dist[idx] = MAXN;
    } min_dist[n_stations] = 0;
    
    Q.push(n_stations);
    while (!Q.empty()) {
        int node = Q.front();
        Q.pop();
        for (int adj_node : network[node]) {
            if (min_dist[adj_node] > min_dist[node] + 1) {
                min_dist[adj_node] = min_dist[node] + 1;
                Q.push(adj_node);
            }
        }
    }
    for (int idx = 0; idx < n_stations; idx++) {
        cin >> path[idx];
    }
    for (int step = 0; step < n_stations; step++) {
        results.insert(min_dist[path[step]] + step);
    }
    int x, y, temp;
    for (int idx = 0; idx < n_days; idx++) {
        cin >> x >> y;
        
        x--; y--;
        results.erase(results.find(min_dist[path[x]] + x));
        results.erase(results.find(min_dist[path[y]] + y));

        temp = path[x];
        path[x] = path[y];
        path[y] = temp;

        results.insert(min_dist[path[x]] + x);
        results.insert(min_dist[path[y]] + y);

        cout << *results.begin() << "\n";
    }
}
