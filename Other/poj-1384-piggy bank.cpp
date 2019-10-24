#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
	int n, m, t, l;
	int i, j, k, vl[501], wl[501], p[10001];
	cin >> t;
	for (k = 1; k <= t; k++)
	{
		cin >> n >> m;
		for (i = 1; i < 10001; i++)
			p[i] = 1e9;
		p[0] = 0;
		cin >> l;
		for (i = 1; i <= l; i++)
			cin >> vl[i] >> wl[i];
		for (i = 1; i <= l; i++)
			for (j = 0; j <= (m - n); j++)
			{
				if (j >= wl[i])
					p[j] = min(p[j], p[j - wl[i]] + vl[i]);
			}
		if (p[m - n] < 1e9)
			cout << "The minimum amount of money in the piggy-bank is " << p[m - n] << "." << endl;
		else
			cout << "This is impossible." << endl;
	}
}
