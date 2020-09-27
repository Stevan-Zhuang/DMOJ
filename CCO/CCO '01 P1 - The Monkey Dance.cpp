#include <bits/stdc++.h>
using namespace std;

int adj[101];
int visited[101];

int gcd(int a, int b) {
    if (a == 0)
        return b;
    return gcd(b % a, a);
}

int lcm(int a, int b) {
    return (a * b) / gcd(a, b);
}

int main() {
    cin.sync_with_stdio(0);
    cin.tie(0);

    int numNodes;
    cin >> numNodes;
    while (numNodes != 0) {
        int I1, I2;
        for (int idx = 0; idx < numNodes; idx++) {
            cin >> I1 >> I2;
            adj[I1] = I2;
        }

        vector<int> cycles;
        int numCycles = 0;
        for (int rootNode = 1; rootNode < numNodes + 1; rootNode++) {
            if (visited[rootNode])
                continue;
            numCycles++;

            int steps = 0;
            int node = rootNode;
            visited[node] = 1;
            do {
                steps++;
                node = adj[node];
                visited[node] = 1;
            }
            while (node != rootNode);
            cycles.push_back(steps);
        }
        int result = 1;
        for (int idx = 0; idx < numCycles; idx++) {
            result = lcm(result, cycles[idx]);
        }

        cout << result << endl;

        memset(adj, 0, numNodes * sizeof(int));
        memset(visited, 0, numNodes * sizeof(int));
        cin >> numNodes;
    }
}
