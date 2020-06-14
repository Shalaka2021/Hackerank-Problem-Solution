#include <bits/stdc++.h>

using namespace std;

// Complete the maximizingXor function below.
int maximizingXor(int l, int r) {
    int n=l^r,cnt=0;
    while(n>0)
    {
        n=n>>1;
        cnt++;
    }
    //cout<<n<<endl;
    //n=1<<cnt;
    //cout<<n<<endl;
    return (1<<cnt)-1;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int l;
    cin >> l;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    int r;
    cin >> r;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    int result = maximizingXor(l, r);

    fout << result << "\n";

    fout.close();

    return 0;
}
