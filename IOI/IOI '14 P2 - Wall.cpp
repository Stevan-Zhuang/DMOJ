#include <iostream>
#include <limits>
#define MAXN 4194303
#define INF std::numeric_limits<int>::max();

struct Node {int minOp, maxOp;};
Node segmentTree[MAXN];

void updateDown(int idx, int rootIdx) {
    segmentTree[idx].minOp = std::max(std::min(segmentTree[rootIdx].minOp,
                                               segmentTree[idx].minOp),
                                      segmentTree[rootIdx].maxOp);
    segmentTree[idx].maxOp = std::min(std::max(segmentTree[rootIdx].maxOp,
                                               segmentTree[idx].maxOp),
                                      segmentTree[rootIdx].minOp);
}

void update(int segLeft, int segRight, int left, int right,
            int idx, int height, int op) {
    if (segRight < left || segLeft > right)
        return;
    if (left <= segLeft && right >= segRight) {
        if (op == 1) {
            segmentTree[idx].minOp = std::max(height, segmentTree[idx].minOp);
            segmentTree[idx].maxOp = std::max(height, segmentTree[idx].maxOp);
        } if (op == 2) {
            segmentTree[idx].minOp = std::min(height, segmentTree[idx].minOp);
            segmentTree[idx].maxOp = std::min(height, segmentTree[idx].maxOp);
        }
        return;
    }
    int leftIdx = idx * 2 + 1;
    int rightIdx = idx * 2 + 2;

    updateDown(leftIdx, idx);
    updateDown(rightIdx, idx);

    segmentTree[idx].minOp = INF;
    segmentTree[idx].maxOp = 0;

    int segMiddle = (segLeft + segRight) / 2;
    update(segLeft, segMiddle, left, right, leftIdx, height, op);
    update(segMiddle + 1, segRight, left, right, rightIdx, height, op);
}

int query(int segLeft, int segRight, int left, int right, int idx) {
    if (segRight < left || segLeft > right)
        return INF;
    if (left <= segLeft && right >= segRight) {
        return segmentTree[idx].minOp;
    }
    int leftIdx = idx * 2 + 1;
    int rightIdx = idx * 2 + 2;

    updateDown(leftIdx, idx);
    updateDown(rightIdx, idx);

    int segMiddle = (segLeft + segRight) / 2;
    return std::min(query(segLeft, segMiddle, left, right, leftIdx),
                    query(segMiddle + 1, segRight, left, right, rightIdx));
}

int main() {
    int numCols, numPhases;
    scanf("%d %d", &numCols, &numPhases);

    int op, left, right, height;
    for (int phase = 0; phase < numPhases; phase++) {
        scanf("%d %d %d %d", &op, &left, &right, &height);
        update(0, numCols - 1, left, right, 0, height, op);
    }

    for (int col = 0; col < numCols; col++) {
        printf("%d\n", query(0, numCols - 1, col, col, 0));
    }
}
