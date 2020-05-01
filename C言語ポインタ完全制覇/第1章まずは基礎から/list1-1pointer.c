#include <stdio.h>

int main(void){
    // Your code here!
    int hoge = 5;
    int piyo = 10;
    int *hoge_p;
    
    // アドレス表示
    printf("&hoge..%p\n", &hoge); // %pはpointer型
    printf("&piyo..%p\n", &piyo);
    printf("&hoge_p..%p\n", &hoge_p);
    
    // hoge->hoge_p
    hoge_p = &hoge;
    printf("&hoge_p..%p\n", &hoge_p);
    
    // hoge_@
    printf("*hoge_p..%d\n", *hoge_p); // %dはint型
    
    // 20->hoge_p
    *hoge_p = 10;
    printf("hoge..%d\n", hoge);
    
    return 0;
}
