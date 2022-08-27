#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <set>
#include <vector>
#define PB push_back
#define ST first
#define ND second
#define UI unsigned int
#define DB(x) x

using namespace std;

int solution (int X, vector<int> &A) {
	bool visited[1000000];
	int sum = 0;

	for (UI i = 0; i < A.size(); ++i) {
		int t = A[i];
		
		if (!visited[t]) {
			visited[t] = 1;
			sum++;
		}

		if (sum == X)
			return i;
	}

	return -1;
}

int main () {
	int n, X;
	scanf("%d%d", &X, &n);

	vector<int> A;
	
	for (int i = 0; i < n; ++i) {
		int t;
		scanf("%d", &t);
		A.PB(t);
	}

	printf("%d\n", solution (X, A));
}

