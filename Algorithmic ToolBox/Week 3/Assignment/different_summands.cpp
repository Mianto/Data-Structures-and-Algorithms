#include <iostream>
#include <vector>

using std::vector;
int sum_vector(vector<int> v);

vector<int> optimal_summands(int n) {
  vector<int> summands;
  int counter = 1;
  int original_total = n;
  while( sum_vector(summands) != original_total){
    if (n - counter <= counter ) {
      summands.push_back(n);
    }else{
      summands.push_back(counter);
    }
    n -= counter;
    counter++;
  }
  return summands;
}

int sum_vector(vector<int> v){
  int sum = 0;
  for (size_t i = 0; i<v.size(); i++){
    sum += v[i];
  }
  return sum;
}

int main() {
  int n;
  std::cin >> n;
  vector<int> summands = optimal_summands(n);
  std::cout << summands.size() << '\n';
  for (size_t i = 0; i < summands.size(); ++i) {
    std::cout << summands[i] << ' ';
  }
}
