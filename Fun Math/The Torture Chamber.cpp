#include <iostream>
#include <cmath>

#define ull unsigned long long

bool flag1[100002];
bool flag2[20000002];

void sieve(ull upLimit) {
    for (ull n = 2; n <= upLimit; n++) {
        if (!flag1[n]) {
            for (ull m = n * 2; m <= upLimit; m += n)
                flag1[m] = true;
        }
    }
}

int main() {

    ull low, high, upLimit, lowLimit;
    scanf("%llu", &low); scanf("%llu", &high);
    upLimit = floor(sqrt(high)) + 1;
    sieve(upLimit);

    for (ull n = 2; n <= upLimit; n++) {
        if (!flag1[n]) {
            lowLimit = floor(low / n) * n;
            if (lowLimit < low) lowLimit += n;
            if (lowLimit == n) lowLimit += n;

            for (ull nn = lowLimit; nn <= high; nn += n) {
                flag2[nn - low] = true;
            }
        }
    }

    ull count = 0;
    for (ull n = low; n <= high - 1; n++) {
        if (!flag2[n - low]) {
            count++;
        }
    }
    printf("%llu\n", count);
}
