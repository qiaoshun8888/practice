#include <iostream>
using namespace std;
//# 25

int continumax(char *outputstr, char *inputstr){
    int c = 0;
    int best = 0;
    char * p;
    while(true){
        if(*inputstr >= '0' && * inputstr <= '9'){
            c ++;
            if(c > best){
                best = c;
                p = inputstr - best + 1;
            }
        }
        else{
            c = 0;
        }
        inputstr ++;
        if(*inputstr == '\0') break;
    }

    // cout << *p;
    for(int i=0; i<best; i++){
        cout << *p++;
        // cout << *outputstr;
        // *outputstr++ = *p++ ;
    }
    // *outputstr = '\0';
    return best;
}
int main(){
    char * s = "abcd12345ed125ss123456789";
    char * outputstr;
    cout << endl << continumax(outputstr, s) << endl;
    return 0;
}
