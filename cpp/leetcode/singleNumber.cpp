#include <iostream>
using namespace std;

class Solution {
public:
    int singleNumber(int A[], int n) {
        int r = 0;
        for(int i=0; i < n; i++){
            r = r^A[i];
        }
        return r;
    }
};

int main(int argc, char const *argv[])
{
    Solution* s = new Solution();
    int A[] = {1,2,3,2,3};
    cout << s->singleNumber(A, 5) << endl;
    return 0;
}
