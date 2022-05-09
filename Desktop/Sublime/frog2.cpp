#include<bits/stdc++.h>
using namespace std;
#define rep(i,n) for (i = 0; i < n; ++i)
#define repr(i,n) for (i = n-1; i >= 0; --i)
int main()
{
	int n,i,k;
	cin>>n>>k;
	int h[n],f[n];
	rep(i,n){
		cin>>h[i];
	}
	f[0]=0;
	for(i=1;i<n;i++){
		f[i] = abs(h[i]-h[i-1])+ f[i-1];
		for(int j=2;j<=k;j++){
			f[i]=min(f[i],abs(h[i]-h[i-j])+ f[i-j]);
		}
	}
	cout<<f[n];
	return 0;
}