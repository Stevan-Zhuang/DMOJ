#include <iostream>
#include <vector>
#include <queue>

#define scan(x) do{while((x=getchar())<'0'); for(x-='0'; '0'<=(_=getchar()); x=(x<<3)+(x<<1)+_-'0');}while(0)
char _;

struct Route {int city; int cost;};
std::vector<Route> adjacent[5001];
bool sellers[5001];
int costs[5001];
int minCosts[5001];

int main() {
    int numCities; scan(numCities);
    int numRoutes; scan(numRoutes);
    for (int idx = 0; idx < numRoutes; idx++) {
        int city; scan(city);
        int adjCity; scan(adjCity);
        int cost; scan(cost);

        Route route1; route1.city = adjCity; route1.cost = cost;
        Route route2; route2.city = city; route2.cost = cost;
        adjacent[city].push_back(route1);
        adjacent[adjCity].push_back(route2);
    }
    int numSellers; scan(numSellers);
    for (int idx = 0; idx < numSellers; idx++) {
        int city; scan(city);
        int cost; scan(cost);

        sellers[city] = true;
        costs[city] = cost;
    }
    std::fill_n(minCosts, 5001, 50010001);

    int root; scan(root);
    minCosts[root] = 0;
    std::priority_queue< int, std::vector<int>, std::greater<int> > queue;
    queue.push(root);
    while (!queue.empty()) {
        int city = queue.top();
        queue.pop();

        for (int idx = 0; idx < adjacent[city].size(); idx++) {
            Route route = adjacent[city][idx];
            if (minCosts[city] + route.cost < minCosts[route.city]) {
                minCosts[route.city] = minCosts[city] + route.cost;
                queue.push(route.city);
            }
        }
    }
    int minCost = 50010001;
    for (int city = 1; city <= numCities; city++) {
        if (sellers[city]) minCost = std::min(minCosts[city] + costs[city], minCost);
    }
    printf("%i\n", minCost);
}
