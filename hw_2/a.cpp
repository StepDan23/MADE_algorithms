# include <iostream>
# include <vector>
# include <tuple>
using namespace std;

int split_arr(int l, int r, int x, vector<int>&arr)
{
    int m = l;
    for (int i=l; i <= r; i++)
        if (arr[i] < x)
        {
            swap(arr[i], arr[m]);
            m++;
        }
    return m;
}


void find_val(int k, int l, int r, vector<int>&arr)
{
    if (r == l)
    {
        cout << arr[l] << endl;;
        return ;
    }
    int x = arr[l + rand() % (r - l + 1)];
    int m = split_arr(l, r, x, arr);
    if (k < m)
        find_val(k, l, m-1, arr);
    else
        find_val(k, m, r, arr);
}


int main()
{
    int size, n_tests, i, j, k;
    cin >> size;
    vector<int> arr(size);

    for (int ind=0; ind < size; ind++)
        cin >> arr[ind];

    cin >> n_tests;
    while (n_tests--)
    {
        vector<int> input_arr = arr;
        cin >> i >> j >> k;
        find_val(k+i-2, i-1, j-1, input_arr);
    }
    return (0);
}
