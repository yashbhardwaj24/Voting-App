/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <bits/stdc++.h>

using namespace std;

bool comp(const pair<int,pair<int,int>>&a, const pair<int,pair<int,int>>&b){
    return a.second.second<b.second.second;
}

int main()
{
    int n;
    cout<<"Enter number of processes : ";
    cin>>n;
    vector<pair<int,pair<int,int>>>Pri;
    int BT, P;
    for(int i = 0;i<n;i++){
        cout<<"Enter BT for process "<<i+1<<" and priority : ";
        Pri.push_back(make_pair(i+1,make_pair(BT, P)));
        cin>>BT>>P;
    }
    sort(Pri.begin(),Pri.end(),comp);
    cout<<"\n";
    for(int i = 0;i<n;i++){
        cout<<Pri[i].first<<" "<<Pri[i].second.first<<" "<<Pri[i].second.second<<"\n";
    }
    int WT = 0;
    vector<int>wt;
    wt.push_back(0);
    for(int i = 0;i<n-1;i++){
    	wt.push_back(Pri[i].second.first);
    	WT+=wt[i];
    }
    vector<int>ta;
    int TA = 0;
    for(int i = 0;i<n;i++){
    	ta.push_back(Pri[i].second.first+ wt[i]);
    	TA+=ta[i];
    }
    cout<<"Process   Burst time    Priority      Waiting time     ";
    for(int i = 0;i<n;i++){
    	cout<<Pri[i].first<<"   "<<Pri[i].second.first<<"    "<<Pri.second.second<<"     "<<wt[i]<<"        "<<ta[i]<<"\n;
    }
    return 0;
}
