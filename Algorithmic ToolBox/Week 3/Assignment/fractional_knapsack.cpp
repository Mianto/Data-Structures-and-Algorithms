#include <iostream>
#include <vector>

using std::vector;

double get_optimal_value(int capacity, vector<int> weights, vector<int> values, int n) {
  double value = 0.0;
  for (int i = 0; i < n; i++){
    if(capacity <= 0){
      return value;
    }
    double a = 0.0;
    int st = 0;

    for(int j = 0; j < n; j++){
      if (weights[j] != 0){
        if ((double)values[j]/(double)weights[j] > a){
          a =  (double)values[j]/weights[j];
          st = j;
        }
      }
    }
    if(capacity > weights[st]){
      capacity -= weights[st];
      value += (double)values[st];
      weights[st] = 0;
    }else{
      value += capacity * ((double)values[st]/weights[st]);
      capacity = 0;
    }
  }
  return value;
}

int main() {
  int n;
  int capacity;
  std::cin >> n >> capacity;
  vector<int> values(n);
  vector<int> weights(n);
  for (int i = 0; i < n; i++) {
    std::cin >> values[i] >> weights[i];
  }

  double optimal_value = get_optimal_value(capacity, weights, values, n);

  std::cout.precision(10);
  std::cout << optimal_value << std::endl;
  return 0;
}
