
#include <bits/stdc++.h>
using namespace std;

void permute(string a, int l, int r)
{	int f = 0;
	vector<int> v;
	if (l == r) {
		int num = std::stoi(a);
		cout << num << endl;
		if (num % 30 == 0) {
			f++;
			v.push_back(num);
		}
	v.erase(v.begin());
	int n1 = *max_element(v.begin(), v.end());
	if (f == 1)
	{	cout << n1 << endl;
	}
	else cout << "-1";
	}
	else
	{

		for (int i = l; i <= r; i++)
		{


			swap(a[l], a[i]);


			permute(a, l + 1, r);


			swap(a[l], a[i]);
		}
	}
	// v.erase(v.begin());
	// int n1 = *max_element(v.begin(), v.end());
	// if (f == 1)
	// {	cout << n1 << endl;
	// }
	// else cout << "-1";
}

int main()
{	vector<int> v;
	string str;
	cin >> str;
	int n = str.size();
	permute(str, 0, n - 1);
	// cout<<v[0];
	return 0;
}

