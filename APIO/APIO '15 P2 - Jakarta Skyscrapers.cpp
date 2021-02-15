#pragma GCC optimize("Ofast")
#pragma GCC target("avx,avx2,fma")
#include <iostream>
#include <unordered_set>
#include <vector>
#include <queue>
#include <string.h>
using namespace std;

#define MAXN 30000
#define INF 0x3f3f3f3f
#define usi unordered_set<int>
#define pii pair<int, int>
#define scan(x) do{while((x=getchar())<'0'); for(x-='0'; '0'<=(_=getchar()); x=(x<<3)+(x<<1)+_-'0');}while(0)
char _;

int nNodes, nDoges, node, doge;

usi network[MAXN];
int minDist[MAXN];
priority_queue<pii, vector<pii>, greater<pii>> Q;

void getLine() {
    scan(node); scan(doge);
    network[node].insert(doge);
}

int main() {
    scan(nNodes); scan(nDoges);
    int src, dest;
    getLine(); src = node;
    getLine(); dest = node;
    for (int idx = 2; idx < nDoges; idx++) {
        getLine();
    }
    memset(minDist, INF, sizeof(minDist));
    minDist[src] = 0;
    Q.push(make_pair(0, src));
    while (!Q.empty()) {
        int curDist = Q.top().first;
        int curNode = Q.top().second;
        Q.pop();
        if (curNode == dest)
            break;
        for (int doge : network[curNode]) {
            for (int jump = 1; curNode - jump * doge >= 0; jump++) {
                int adjNode = curNode - jump * doge;
                if (minDist[adjNode] > curDist + jump) {
                    minDist[adjNode] = curDist + jump;
                    Q.push(make_pair(curDist + jump, adjNode));
                    if (network[adjNode].find(doge) != network[adjNode].end())
                        break;
                }
            }
            for (int jump = 1; curNode + jump * doge < nNodes; jump++) {
                int adjNode = curNode + jump * doge;
                if (minDist[adjNode] > curDist + jump) {
                    minDist[adjNode] = curDist + jump;
                    Q.push(make_pair(curDist + jump, adjNode));
                    if (network[adjNode].find(doge) != network[adjNode].end())
                        break;
                }
            }
        }
    }
    if (minDist[dest] == INF)
        printf("-1\n");
    else
        printf("%i\n", minDist[dest]);
}
