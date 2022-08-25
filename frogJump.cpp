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

int solution (int X, int Y, int D) {
	int res = (Y - X) / D;

	if ((Y - X) % D != 0)
		return (res + 1);
	return res;
}

int main () {
	int X, Y, D;
	scanf("%d %d %d", &X, &Y, &D);
	printf("%d\n", solution (X, Y, D));
}

