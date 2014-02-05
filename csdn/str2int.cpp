#include <iostream>
using namespace std;

// # 20

int str2int(char *c){
    // forget about neg
    int num = 0;
    while(*c != '\0'){
        // cout << *c << endl;
        if(*c - '0' > 0 and *c - '9' < 0){
            num = (*c - '0') + num * 10;
        }
        else{
            return -1;
        }
        c ++ ;
    }
    return num;
}

int main(){
    char *test = "345";
    cout << str2int(test) << endl;
    return 0;
}
