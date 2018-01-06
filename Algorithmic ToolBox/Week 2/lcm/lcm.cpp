#include <iostream>

long long lcm_naive(int a, int b) {
  for (long l = 1; l <= (long long) a * b; ++l)
    if (l % a == 0 && l % b == 0)
      return l;

  return (long long) a * b;
}

int gcd(int a, int b){
    if(b == 0){
        return a;
    }else{
    if(a > b){
      return gcd(b, a % b);
    }else{
      return gcd(a, b % a);
    }
  }
}

long long lcm(int a, int b){
    int c = gcd(a, b);
    long long d = (long long)a * (long long)b;
    return d/c;
}

int main() {
  int a, b;
  std::cin >> a >> b;
  //std::cout << lcm_naive(a, b) << std::endl;
  std::cout << lcm(a, b) << std::endl;
  return 0;
}
