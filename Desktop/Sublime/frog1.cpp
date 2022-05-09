#include<bits/stdc++.h>
using namespace std;
#define rep(i,n) for (i = 0; i < n; ++i)
#define repr(i,n) for (i = n-1; i >= 0; --i)
int main()
{
	int n,i;
	cin>>n;
	int h[n],f[n];
	rep(i,n){
		cin>>h[i];
	}
	f[0]=0;
	for(i=1;i<n;i++){
		f[i]=min(abs(h[i]-h[i-1])+ f[i-1],abs(h[i]-h[i-2])+ f[i-2]);
	}
	cout<<f[n-1];
	return 0;
}