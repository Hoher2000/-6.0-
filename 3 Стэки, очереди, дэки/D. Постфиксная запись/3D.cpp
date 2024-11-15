#include <iostream>
#include <vector>
#include <string>

int main()
{
    std::vector<int> stack;
    std::string val;
    size_t len = 0;
    while (std::cin >> val){
        if (val == "+"){
            stack[len-2] += stack[len-1];
            stack.pop_back();
            len--;
        }else if (val == "-"){
            stack[len-2] -= stack[len-1];
            stack.pop_back();
            len--;
        }else if (val == "*"){
            stack[len-2] *= stack[len-1];
            stack.pop_back();
            len--;
        }else{
            stack.push_back(stoi(val));
            len++;
        }
    }
    std::cout << stack[len-1] << std::endl;
    
}