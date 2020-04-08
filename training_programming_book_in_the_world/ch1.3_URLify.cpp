#include <iostream>

void urlify(char *str, int len){
    int spaceCount = 0, index;
    for(int i = 0; i < len; ++i){
        if (str[i] == ' '){ ++spaceCount;}
    }
    cout << spaceCount << endl;
    index = len + spaceCount * 2 - 1; // 元の空白と合わせて3倍の空白文字を足している, 文字列の配列用意するので-1
    
    for(int j = len - 1; j >= 0; --j){
        if (str[j] == ' '){
            str[index--] = '0';
            str[index--] = '2';
            str[index--] = '%';
        }
        else{
            str[index--] = str[j];
        }
    }
}

int main()
{
    char str[] = "Mr John Smith    ";                       //String with extended length ( true length + 2* spaces)
    std::cout << "Actual string   : " << str << std::endl;
    urlify(str, 13);                                        //Length of "Mr John Smith" = 13
    std::cout << "URLified string : " << str << std::endl;
    return 0;
}
