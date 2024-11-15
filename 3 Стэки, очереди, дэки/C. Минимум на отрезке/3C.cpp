#include <iostream>
#include <stack>
#include <utility>
#include <limits>
#include <vector>

enum {inf = std::numeric_limits<int>::max()};

int main()
{
    size_t n, window, i;
    std::cin >> n >> window;
    std::vector<int> ar(n);

    for (int &d : ar)
        std::cin >> d;

    std::stack<std::pair<int, int>> stack1;
    stack1.push({inf, inf});
    std::stack<int> stack2;
    stack2.push(inf);

    for (size_t i=0; i<window; ++i)
        stack1.push({ar[i], std::min(stack1.top().second, ar[i])});

    for (size_t i=0; i<window; ++i){
        int st1_top = stack1.top().first;
        stack1.pop();
        stack2.push(std::min(stack2.top(), st1_top));
    }

    std::cout << std::min(stack1.top().second, stack2.top()) << '\n';
    i = window;

    while (i < n){
        if (stack2.size() - stack1.size() == window){
            while (stack2.size() != 1 && i < n){
                stack1.push({ar[i], std::min(stack1.top().second, ar[i])});
                stack2.pop();
                std::cout << std::min(stack1.top().second, stack2.top())  << '\n';
                ++i;
            }
        }
        else{
            for (size_t i=0; i<window; ++i){
                int st1_top = stack1.top().first;
                stack1.pop();
                stack2.push(std::min(stack2.top(), st1_top));
            }
        }
    }

}