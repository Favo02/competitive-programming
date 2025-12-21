#include<bits/stdc++.h>
using namespace std;
using ll = long long;

void solve(){
    ll n,l,r; cin>>n>>l>>r;
    vector<ll> v(n);
    vector<array<ll,2>> vl(n),vr(n), psl(n+1), psr(n+1); //[0] retta crescente

    for(auto &x:v) cin>>x;
    sort(v.begin(),v.end());
    for(ll i=0;i<n;i++){
        //cout<<v[i]<<" "<<r<<endl;
        vl[i][0]= -v[i]+l;
        vl[i][1]= v[i]-l;
        vr[i][0]= -v[i]+r;
        vr[i][1]= v[i]-r;
    }

 //   for(ll i=0;i<n;i++) 
   //     cout<<vr[i][0]<<endl;

    for(ll i=1;i<=n;i++){
        psl[i][0]=psl[i-1][0]+vl[i-1][0];
        psl[i][1]=psl[i-1][1]+vl[i-1][1];

        psr[i][0]=psr[i-1][0]+vr[i-1][0];
        psr[i][1]=psr[i-1][1]+vr[i-1][1];
    }

    auto suml = [&](ll crescente, ll a, ll b){ //[]
        return psl[b+1][crescente]-psl[a][crescente];
    };
    auto sumr = [&](ll crescente, ll a, ll b){ //[]
        return psr[b+1][crescente]-psr[a][crescente];
    };

    // cout<<"ciao";

    // for(ll i=0;i<n+1;i++){
    //     cout<<vl[i][0]<<" ";
    //     cout<<psl[i][0]<<endl;
    // }
    // cout<<endl;

    ll res =0;
    for(ll i=0;i<n;i++){ //i = indice dell'ultimo elemento >=
        //retta crescente
        ll si = max(i+1, n-i);
        res = max(res, suml(0,0,i)+suml(1, si, n-1));
        //retta costante
        if(n-i-1>i){
            res = max(res, suml(0,0,i)+suml(1, n-i-1,n-1));
          //  cout<<"quack"<<" "<<suml(0,0,i)<<" "<<suml(1, n-i-1,n-1)<<endl;
        }
        //retta decrescente
        si = n - i - 2;
        if(si>i)
            res = max(res, sumr(0,0,i) + sumr(1, si, n-1));
    }

    for(ll i=n-1;i>=0;i--){ //i = indice dell'ultimo elemento >=
        int dec = n - i; //numero rette decrescenti
        //retta decrescente
        ll si = dec-2; 
        if(dec-2>=i) si = i-1;
        res = max(res, sumr(0,0,si)+sumr(1, i, n-1));
    }

    cout<<res<<"\n";
}

int main(){
    ll t; cin>>t;
    while(t--) solve();
}