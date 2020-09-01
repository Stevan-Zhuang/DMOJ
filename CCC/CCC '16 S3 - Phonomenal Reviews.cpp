#include <iostream>
#include <vector>
using namespace std;

vector<int> adj[100000];
bool valid[100000];
bool visited[100000];

void prune(int node, int root=-1) {
    for (int adjNode : adj[node]) {
        if (!visited[adjNode]) {
            visited[adjNode] = true;
            prune(adjNode, node);
        }
    }
    for (int adjNode : adj[node]) {
        if (valid[adjNode] && adjNode != root) {
            valid[node] = true;
        }
    }
}

pair<int, int> dfs(int node, int depth=0) {
    pair<int, int> maxNodeDepth = make_pair(node, depth);
    pair<int, int> nodeDepth;
    for (int adjNode : adj[node]) {
        if (!visited[adjNode] && valid[adjNode]) {
            visited[adjNode] = true;
            nodeDepth = dfs(adjNode, depth + 1);
            if (nodeDepth.second > maxNodeDepth.second) {
                maxNodeDepth = nodeDepth;
            }
        }
    }
    return maxNodeDepth;
}

int main() {
    int N; scanf("%i", &N);
    int M; scanf("%i", &M);

    int pho;
    for (int i = 0; i < M; i++) {
        scanf("%i", &pho);
        valid[pho] = true;
    }

    for (int i = 0; i < N - 1; i++) {
        int a; scanf("%i", &a);
        int b; scanf("%i", &b);
        adj[a].push_back(b);
        adj[b].push_back(a);
    }

    int root = pho;
    visited[root] = true;
    prune(root);

    int numValid = -1;
    for (bool value : valid) {
        if (value) numValid++;
    }

    fill_n(visited, 100000, false);
    visited[root] = true;
    int furthestNode = dfs(root).first;

    fill_n(visited, 100000, false);
    visited[furthestNode] = true;
    int diameter = dfs(furthestNode).second;

    printf("%i\n", diameter + (numValid - diameter) * 2);
}
