#include <stdio.h>

int main(void){
    int array[5];
    int i;
    
    // 配列arrayに値を設定
    for (i = 0; i < 5; i++){
        array[i] = i;
    }
    
    // 内容を表示
    for (i = 0; i < 5; i++){
        printf("%d\n", array[i]);
    }
    
    // アドレスを表示
    for (i = 0; i< 5; i++){
        printf("array[%d]... %p\n", i, &array[i]);
    }
    
    return 0;
}
