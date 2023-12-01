#include<bits/stdc++.h>
using namespace std;

#define int long long
#define pb push_back
#define sz(v) (int)(v.size())
#define all(v) (v.begin(),v.end())
#define uniq(v) (v).erase(unique(all(v)),(v).end())
#define mem1(a) memset(a,-1,sizeof(a))
#define mem0(a) memset(a,0,sizeof(a))

constexpr int pct(int x) { return __builtin_popcount(x); }
constexpr int bits(int x) { return 31 - __builtin_clz(x); }

const long long INF=1e18;
const int32_t M=1e9+7;
const int32_t MM=998244353;
const long double pi = 3.14159265358979323846;

template<typename T, typename = void> struct is_iterable : false_type {};
template<typename T> struct is_iterable<T, void_t<decltype(begin(declval<T>())),decltype(end(declval<T>()))>> : true_type {};
template<typename T> typename enable_if<is_iterable<T>::value&&!is_same<T, string>::value,ostream&>::type operator<<(ostream &cout, T const &v);
template<typename T> typename enable_if<is_iterable<T>::value&&!is_same<T, string>::value,ostream&>::type operator<<(ostream &cout, T const &v) {
	cout << "["; 
	for (auto it = v.begin(); it != v.end();) {
		cout << *it;
		if (++it != v.end()) cout << ", ";
	}
	return cout << "]";
}
template<typename A, typename B> ostream& operator<<(ostream &cout, pair<A, B> const &p) { return cout << "(" << p.first << ", " << p.second << ")"; }
template<typename A, typename B> istream& operator>>(istream& cin, pair<A, B> &p) {
	cin >> p.first;
	return cin >> p.second;
}


int toint(char c){
	return (int)(c-'0');
}

signed main(){
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	
	int lines = 1000;
	int ans = 0;
	int val = 0;
	while(lines--){
		string s;
		cin >> s;
		int first =0;
		int second=0;
		for(int i = 0;i<s.length();i++){
			if(isdigit(s[i])){
				first = toint(s[i])*10;
				break;
			}
		}
		for(int i = s.length()-1;i>=0;i--){
			if(isdigit(s[i])){
				second = toint(s[i]);
				break;
			}
		}
		val = first + second;
		ans+=val;
	}
	cout << ans;

	return 0;
}