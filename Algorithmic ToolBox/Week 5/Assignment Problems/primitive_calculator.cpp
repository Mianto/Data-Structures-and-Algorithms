#include <iostream>
#include <vector>
#include <algorithm>

using std::vector;

vector<int> optimal_sequence(int n) {
  std::vector<int> sequence;
  std::vector<int> c(n+1);
  int num;
  c[0] = 0;
  for (int i = 1; i <= n; ++i) {
    num = c[i - 1];
    if (i % 3 == 0 && num > c[i / 3]){
      num = c[i / 3]; 
    }
    if (i % 2 == 0 && num > c[i / 2]){
      num = c[i / 2];
    }
    c[i] = num + 1;
  }
  while (n >= 1){
    sequence.push_back(n);
    num = c[n];
    if (n % 3 == 0 && num == c[n/3] + 1){
      n = n / 3;
    }else if (n % 2 == 0 && num == c[n/2] + 1){
      n = n / 2;
    }else{
      n = n - 1;
    }
  }
  reverse(sequence.begin(), sequence.end());
  return sequence;
}

int main() {
  int n;
  std::cin >> n;
  vector<int> sequence = optimal_sequence(n);
  std::cout << sequence.size() - 1 << std::endl;
  for (size_t i = 0; i < sequence.size(); ++i) {
    std::cout << sequence[i] << " ";
  }
}
