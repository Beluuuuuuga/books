#include <stdio.h>

int main(void){
    
    int hoge;
    int *hoge_p;
    
    // hoge->hoge_p
    hoge_p = &hoge;
    
    // hoge_p
    printf("hoge_p..%p\n", hoge_p);
    
    // increament hoge_p
    hoge_p++;
    
    // hoge_p
    printf("hoge_p..%p\n", hoge_p); // + 4
    
    // hoge_p+3
    hoge_p = hoge_p + 3;
    printf("hoge_p..%p\n", hoge_p); // + 12
    
    
    return 0;
}
