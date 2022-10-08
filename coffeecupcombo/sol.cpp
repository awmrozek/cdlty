#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <set>
#define PB push_back
#define ST first
#define ND second

using namespace std;

int solution (int n, char *c) {
	int hands = 0;
	int awake = 0;
	for (int i = 0; i < n; ++i) {
		// fill cups
		if (c[i] == '1') {
			hands = 2;
		}

		// drink
		if (hands > 0) {
			awake++;
			hands--;
		}

		// fill again
		if (c[i] == '1') {
			hands = 2;
		}
	}

	return awake;
}

int main () {
	int n;
	char c[100002];

	scanf("%d %s", &n, c);
	printf("%d\n", solution(n, c));
}

