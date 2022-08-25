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

/*float distance (int x1, int y1, int x2, int y2) {
	return (sqrt((x1-x2)^2 + (y1-y2)^2));
}*/

int solution(string &direction, int radius, vector<int> &X, vector<int> &Y) {
	int res = 0;
	for (UI i = 0; i < X.size(); ++i) {
		int x = X[i];
		int y = Y[i];
		float dst = sqrt(x * x + y * y);

		if (dst <= radius) {
			if (direction[0] == 'U' && (y >= 0 && (abs(y) >= abs(x))))
				res++;

			else if (direction[0] == 'D' && (y <= 0 && (abs(x) <= abs(y))))
				res++;

			else if (direction[0] == 'L' && (x <= 0 && (abs(x) >= abs(y))))
				res++;

			else if (direction[0] == 'R' && ((x >= 0 && (abs(x) >= abs(y)))))
				res++;
		}
	}

	return res;
}

int main () {
	char direction[1];
	int radius;
	scanf("%s %d", direction, &radius);
	vector <int> X;
	vector <int> Y;

	int n;
	scanf("%d", &n);

	for (UI i = 0; i < n; ++i) {
		int t;
		scanf("%d", &t);
		X.PB(t);
	}

	for (UI i = 0; i < n; ++i) {
		int t;
		scanf("%d", &t);
		Y.PB(t);
	}

	string dir;
	dir = direction;
	printf("%d\n", solution(dir, radius, X, Y));
	return 0;
}

