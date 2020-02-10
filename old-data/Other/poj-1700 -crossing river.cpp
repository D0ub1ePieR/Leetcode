#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
	int n, sp[1001], t;
	int i, j, ans;
	cin >> t;
	for (i = 1; i <= t; i++)
	{
		cin >> n;
		for (j = 1; j <= n; j++)
			cin >> sp[j];
		sort(sp + 1, sp + n);
		ans = 0;
		while (n)
		{
			if (n == 1)
			{
				ans += sp[1];
				break;
			}
			if (n == 2)
			{
				ans += sp[2];
				break;
			}
			if (n == 3)
			{
				ans += sp[1] + sp[2] + sp[3];
				break;
			}
			ans += min(sp[2] + sp[1] + sp[n] + sp[2], sp[n] + sp[1] + sp[n - 1] + sp[1]);
			n -= 2;
		}
		cout << ans << endl;
	}
}
