#include <iostream>
#define ull unsigned long long

ull dp[100001];

int main() {
    int numItems, maxWeight; scanf("%i%i", &numItems, &maxWeight);
    int weight; ull value;
    for (int item = 0; item < numItems; item++) {
        scanf("%i%llu", &weight, &value);
        for (int possWeight = maxWeight; possWeight >= weight; possWeight--) {
            dp[possWeight] = std::max(dp[possWeight - weight] + value, dp[possWeight]);
        }
    }
    printf("%llu\n", dp[maxWeight]);
}
