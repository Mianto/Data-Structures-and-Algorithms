#include <iostream>
#include <vector>
#include <cstdlib>
#include <tuple>

using std::vector;
using std::swap;
using namespace std;

tuple<int, int> partition2(vector<int> &a, int l, int r) {
  int x = a[l];
  int j = l;
  int m = r;
  int i;
  for (i = l + 1; i <= m; i++) {
    if (a[i] < x) {
      j++;
      swap(a[i], a[j]);
    }else if (a[i] > x){
      swap(a[i], a[m]);
      m--;
      i--;
    }
  }
  swap(a[l], a[j]);
  return make_tuple(j, m);
}

void randomized_quick_sort(vector<int> &a, int l, int r) {
  if (l >= r) {
    return;
  }

  int k = l + rand() % (r - l + 1);
  swap(a[l], a[k]);
  int m1, m2 ;
  tie(m1, m2) = partition2(a, l, r);

  randomized_quick_sort(a, l, m1 - 1);
  randomized_quick_sort(a, m2 + 1, r);
}

int main() {
  int n;
  std::cin >> n;
  vector<int> a(n);
  for (size_t i = 0; i < a.size(); ++i) {
    std::cin >> a[i];
  }
  randomized_quick_sort(a, 0, a.size() - 1);
  for (size_t i = 0; i < a.size(); ++i) {
    std::cout << a[i] << ' ';
  }
} 

