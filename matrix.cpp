#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <set>
#include <bitset>
#include <cmath>
#define PB push_back
#define ST first
#define ND second
#define UI unsigned int
#define DB(x) 

using namespace std;

int M[1000][1000];
int solution(int N, vector<int> &A, string &S) {

	int mx = 0;
	for (UI i = 0; i < A.size(); ++i) {
		if (S[i] == 'R') {
			int row = A[i];

			for (UI j = 0; j < (UI)(N); ++j) {
				M[row][j]++;
				mx = max(mx, M[row][j]);
			}
		} else {
			// S[i][0] == C
			int col = A[i];
			for (UI j = 0; j < (UI)(N); ++j) {
				M[j][col]++;
				mx = max(mx, M[j][col]);
			}
		}
	}
	return mx;
}

int main () {
	// NxN - array size
	int N, as;
	scanf("%d%d", &N, &as);
	vector<int> A;

	for (UI i = 0; i < as; ++i) {
		int t;
		scanf("%d", &t);

		A.PB(t);
	}
	string S;
	char ss[10000];

	scanf("%s", ss);
	S = ss;

	printf("%d\n", solution(N, A, S));
	return 0;
}

