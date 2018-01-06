#include <iostream>
#include <stack>
#include <string>

struct Bracket {
    Bracket(char type, int position):
        type(type),
        position(position)
    {}

    bool Matchc(char c) {
        if (type == '[' && c == ']')
            return true;
        if (type == '{' && c == '}')
            return true;
        if (type == '(' && c == ')')
            return true;
        return false;
    }

    char type;
    int position;
};

int main() {
    std::string text;
    getline(std::cin, text);
    int flag = 1, k = 0;
    std::stack <Bracket> opening_brackets_stack;
    for (int position = 0; position < text.length(); ++position) {
        char next = text[position];
        k++;
        if (next == '(' || next == '[' || next == '{') {
            Bracket b = {next, position};
            opening_brackets_stack.push(b);
        }

        if (next == ')' || next == ']' || next == '}') {
            // Process closing bracket, write your code here
            if (opening_brackets_stack.empty()){
                std :: cout << position + 1;
                flag = 0;
                break;
            }
            Bracket b = opening_brackets_stack.top();
            if (next == ')' && b.type != '(' ){
                std::cout << position + 1;
                flag = 0;
                break;
            } else if (next == '}' && b.type != '{' ){
                std::cout << position + 1;
                flag = 0;
                break;
            } else if (next == ']' && b.type != '[' ){
                std::cout << position + 1;
                flag = 0;
                break;
            } else {
                opening_brackets_stack.pop();
            }
        }
    }
    if (flag == 1 && opening_brackets_stack.empty())
        std::cout << "Success" << "\n";
    else if (flag == 1){
        std :: cout << opening_brackets_stack.top().position + 1;
    }

    return 0;
}
