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

int solution(string &S) {
	UI i = 0;
	UI res = 0;
	while (i < S.length()) {
		if (S[i] == 'X') {
			DB(printf("Patching %d\n", i););
			S[i] = S[i+1] = S[i+2] = '.';
			res++;
			i+=2;
		}
		++i;
	}

	return res;
}

int main () {
	char ss[10000];
	scanf("%s", ss);
	
	string s(ss);
	s += "---";
	DB(printf("Input: %s\n", s.c_str()););

	printf("%d\n", solution(s));
	return 0;
}

