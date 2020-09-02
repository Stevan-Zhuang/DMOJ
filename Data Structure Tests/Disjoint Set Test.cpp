#include <iostream>

int numVertices, numEdges;
struct Edge {int weight, x, y;};
Edge edges[1000000];

int parent[100001];
int rank[100001];

int mst[99999];

int find(int x) {
    while (x != parent[x])
        x = parent[x];
    return x;
}

void union_(int x, int y) {
    if (rank[x] < rank[y]) {
        parent[x] = y;
    } else if (rank[x] > rank[y]) {
        parent[y] = x;
    } else {
        parent[y] = x;
        rank[x]++;
    }
}

void kruskal() {
    for (int idx = 1; idx < numVertices; idx++) {
        parent[idx] = idx;
    }
    int xRoot, yRoot, MSTsize = 0;
    for (int idx = 0; idx < numEdges; idx++) {
        //printf("%i\n", MSTsize);
        xRoot = find(edges[idx].x);
        yRoot = find(edges[idx].y);
        //printf("%i, %i\n", xRoot, yRoot);
        //printf("%i, %i\n", xRoot, yRoot);
        if (xRoot != yRoot) {
            union_(xRoot, yRoot);
            mst[MSTsize] = edges[idx].weight;
            MSTsize++;
            if (MSTsize == numVertices - 1) {
                for (int idxEdge = 0; idxEdge < MSTsize; idxEdge++)
                    printf("%i\n", mst[idxEdge]);
                return;
            }
        }
    }
    printf("Disconnected Graph");
    return;
}

int main() {
    scanf("%i%i", &numVertices, &numEdges);
    Edge edge;
    for (int idx = 1; idx <= numEdges; idx++) {
        edge.weight = idx;
        scanf("%i%i", &edge.x, &edge.y);
        edges[idx - 1] = edge;
    }
    kruskal();
}
