#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <set>
#define LL long long int
#define PB push_back
#define ST first
#define ND second
#define INF 9999999999999

using namespace std;

LL solution (int n, vector<LL> a) {
	LL hei = 0;

	for (int i = 0; i < a.size(); ++i) {
		//printf("Hill %d [%lld]\n", i, a[i]);

		// assume current highest
		// scan left
		int j = i;
		while (a[j-1] <= a[j] && j >= 0) j--;

		//printf(" -> going left %d [%lld]\n", j, a[j]);

		// scan right
		int k = i;
		while (k+1 < a.size() && a[k+1] <= a[k]) {
			//printf(" **** %lld < %lld going right\n", a[k+1], a[k]);
			k++;
		}

		//printf(" -> going right %d [%lld]\n", k, a[k]);

		//printf("Leftmost hill: \t%d [%lld] rightmost: \t%d [%lld]\n", 
		//		j, a[j], k, a[k]);

		LL lh = a[i] - a[j];
		LL rh = a[i] - a[k];

		//printf("Deltas: left:\t%lld\tright:\t%lld\n", lh, rh);

		if (lh == 0)
			lh = INF;

		if (rh == 0)
			rh = INF;

		LL loch = min(lh, rh);
		//printf("New delta: %lld globmax: %lld\n", loch, hei);
		if (loch != INF) {
			//printf("Updating global max\n");
			hei = max(loch, hei);
		} else {
			//printf("Not updating global max as loch == %lld == INF\n", loch);
		}
	}

	return hei;
}

int main () {
	int n;
	scanf("%d", &n);
	vector<LL> a;

	for (int i = 0; i < n; ++i) {
		LL t;
		scanf("%lld", &t);

		a.PB(t);
	}

	printf("%lld\n", solution(n, a));
}

