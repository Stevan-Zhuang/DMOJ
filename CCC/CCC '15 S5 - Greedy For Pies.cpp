#include <iostream>
#include <algorithm>
#include <string.h>

int numFirst, numSecond;
int first[3001], second[101];
int memo[3001][2][101][101];

int dfsearch(int idx, int tookLast, int usedL, int usedR) {
	int result;
	if (memo[idx][tookLast][usedL][usedR] != -1) {
		return memo[idx][tookLast][usedL][usedR];
	}
	if (idx == numFirst) {
		if (usedL <= usedR) {
			if (tookLast) {
				result = dfsearch(idx, 0, usedL, usedR - 1) + second[usedR];
				memo[idx][tookLast][usedL][usedR] = result;
				return result;
			} else {
				result = dfsearch(idx, 1, usedL + 1, usedR);
				memo[idx][tookLast][usedL][usedR] = result;
				return result;
			}
		}
		return 0;
	}

    if (tookLast) {
        result = dfsearch(idx + 1, 0, usedL, usedR) + first[idx];
        result = std::max(dfsearch(idx + 1, 1, usedL, usedR), result);
		if (usedL <= usedR)
		    result = std::max(dfsearch(idx, 0, usedL, usedR - 1) + second[usedR], result);
	} else { 
        result = dfsearch(idx + 1, 1, usedL, usedR);
		if (usedL <= usedR)
		    result = std::max(dfsearch(idx, 1, usedL + 1, usedR), result);
	}
	memo[idx][tookLast][usedL][usedR] = result;
	return result;
}

int main() {
	scanf("%i", &numFirst);
	for (int idx = 0; idx < numFirst; idx++)
		scanf("%i", &first[idx]);
	scanf("%i", &numSecond);
	for (int idx = 0; idx < numSecond; idx++)
		scanf("%i", &second[idx]);
    std::sort(second, second + numSecond);
    memset(memo, -1, sizeof(memo));
	printf("%i\n", dfsearch(0, 1, 0, numSecond - 1));
}

