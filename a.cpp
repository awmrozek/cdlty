#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
#include <limits>
#define LL long long int
#define PB push_back
#define ST first
#define ND second
#define INF 9999999999999
#define REP(i,a,b) for(int i=a; i<b; ++i)

using namespace std;

int solution () {
}

// r value reference, reference to something that may be missing memory place
void f(int&& a) {
}

int main () {
	int N;
	vector<bool> edges; // bridge eller ej
	vector<vector<int> > adj;
	vector<vector<int> > adj_e;

	scanf("%d", &N);
	for (int i = 0; i < N; ++i) {
		int a, b;
		scanf("%d%d", &a, &b);
		adj[a].push_back(b);
		adj[b].push_back(a);
	}

	// && for recursive names
	//vector<int> depths(N - 1); // no visited array
	vector<int> depths(N - 1); // no visited array
	vector<int> dp(N, std::numeric_limits<int>::max());
	auto dfs = [&](auto&& dfs, int node, int from, int depth) {
		depths[node] = depth;

		for (auto other : adj[node]) {
			if (other == from) continue;
			int other_d = depths[other];
			if (other_d == -1) {
				dp[node] = min(dp[node], dfs(dfs, other, node, depth + 1));
				// edges[adj_e[node][other]] = dp[other] <= depth;
				// if (dp[other] <= depth) {bridge}
				// art[node] |= dp[other] >= depth; // articulation point
				// andra edgen
			} else if (other_d < depth) {
				// backedge, behover ej kolla
			} else if (other_d > depth) {
				// direct edge, inte heller
			}
		}

		return dp[node];
	};

	solution();
}

