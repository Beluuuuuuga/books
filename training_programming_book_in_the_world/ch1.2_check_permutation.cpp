#include <iostream>
#include <string>
#include <algorithm>
bool arePermutation(std::string s, std::string t){
    // Get lengths of both strings
    // If length of both strings is not same, then they
    // cannot be anagram
    if (s.length() != t.length()) return false;
    
    // Sort both strings
    sort(s.begin(),s.end());
    sort(t.begin(),t.end());
    // Compare sorted strings
    for (int i=0; i<s.length(); ++i){
        if (s[i] != t[i]) return false;
    }
    return true;
}

bool arePermutation2(const std::string &s,const std::string &t){
    if (s.length() != t.length()) return false;
    int count[128]={0};
    for (int i=0; i<s.length(); ++i){
        int val = s[i];
        count[val]++;
    }
    for (int i=0; i<t.length(); ++i){
        int val = t[i];
        count[val]--;
        if (count[val]<0) return false;
    }
    return true;
}

int main(void){
   // Test Method 1 - Using sort
    std::cout << "Method 1 - Using sort" << std::endl;
    std::string s = "testest";
    std::string t = "estxest";
    std::cout << std::boolalpha << arePermutation(s, t) << std::endl;
    s = "hello";
    t = "oellh";
    std::cout << std::boolalpha << arePermutation(s, t) << std::endl;
    
    //Test Method 2 - Using character count
    std::cout << "Method 2 - Using character count" << std::endl;
    s = "testest";
    t = "estxest";
    std::cout << std::boolalpha << arePermutation2(s, t) << std::endl;
    s = "hello";
    t = "oellh";
    std::cout << std::boolalpha << arePermutation2(s, t) << std::endl;
}
