#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;

/*
 * Complete the function below.
 */
int maxLength(vector < int > a, int k) {
    if (a.size() == 0) {
        return 0;
    }
    
    int lastSum = 0, lastLength = 0, maxLength = 0;
    for (int i = 0; i < a.size(); i++) {
        // lastSum represents the sum of the longest subarray with sum <= k (valid) ending at index i
        // lastLength represents the length of the longest valid subarray ending at index i
        // maxLength is the length of the longest valid subarray found so far
        if (a[i] > k) {
            lastSum = 0;
            lastLength = 0;
            continue;
        }
        if (lastSum + a[i] <= k) {
            lastLength++;
            lastSum += a[i];
        } else {
            lastSum = a[i];
            lastLength = 1;
            int j = i - 1;
            while (j > -1 && lastSum + a[j] <= k) {
                // search backwards to find the longest valid subarray ending at index i
                lastSum += a[j--];
                lastLength++;
            }
        }
        maxLength = maxLength > lastLength ? maxLength : lastLength;
    }
    return maxLength;
}

int main() {
    ofstream fout(getenv("OUTPUT_PATH"));
    int res;
    
    int _a_size = 0;
    cin >> _a_size;
    cin.ignore (std::numeric_limits<std::streamsize>::max(), '\n'); 
    vector<int> _a;
    int _a_item;
    for(int _a_i=0; _a_i<_a_size; _a_i++) {
        cin >> _a_item;
        cin.ignore (std::numeric_limits<std::streamsize>::max(), '\n');
        _a.push_back(_a_item);
    }
    
    int _k;
    cin >> _k;
    cin.ignore (std::numeric_limits<std::streamsize>::max(), '\n');
    
    res = maxLength(_a, _k);
    fout << res << endl;
    
    fout.close();
    return 0;
}
