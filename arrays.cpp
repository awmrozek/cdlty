#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <set>
#include <bitset>
#define PB push_back
#define ST first
#define ND second
#define UI unsigned int
#define DB(x) 

using namespace std;

vector<int> solution(vector<int> &A, int K) {
	DB(printf("len = %d k = %d\n", A.size(), K);
	for (UI i; i < A.size(); ++i) {
		printf("%d\n", A[i]);
	});

	if (K == 0)
		return A;
	if (A.size() == 1)
		return A;

	vector <int> ret;
	ret.resize(A.size());

	copy(A.end() - K, A.end(), ret.begin());
	copy(A.begin(), A.end() - K, ret.begin()+K);
	//copy(A.begin(), A.end(), ret.begin());
	//rotate (A.begin(), A.begin()+K, A.end());
	return ret;
}

int main () {
	int n, K;
	vector<int> A;
	scanf("%d", &n);

	for (int i = 0; i < n; ++i) {
		int x;
		scanf ("%d", &x);

		A.PB(x);
	}

	scanf("%d", &K);

	vector<int> ret = solution(A, K);

	if (ret.size() == 0)
		return 0;

	printf ("%d", ret[0]);
	for (UI i = 1; i < ret.size(); ++i) {
		printf(" %d", ret[i]);
	}

	printf("\n");
	return 0;
}

