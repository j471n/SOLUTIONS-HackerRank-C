// Date - Oct 5, 2020 By Jatin Sharma


#include<iostream>
#include<vector>
using namespace std;

int main()
{
    vector<vector<int>> a(6, vector<int>(6));
    int sum = -100, s = -100;
    for (int arr_i = 0; arr_i < 6; arr_i++)
    {
        for (int arr_j = 0; arr_j < 6; arr_j++)
        {
            cin >> a[arr_i][arr_j];
        }
    }
    for (int i = 1; i < 5; i++)
    {
        for (int j = 1; j < 5; j++)
        {
            s = a[i][j] + a[i - 1][j - 1] + a[i - 1][j] + a[i - 1][j + 1] + a[i + 1][j - 1] + a[i + 1][j] + a[i + 1][j + 1];
            if (s > sum)
                sum = s;
        }
    }
    cout << sum;
    return 0;
}