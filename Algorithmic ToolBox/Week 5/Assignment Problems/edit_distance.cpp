#include <iostream>
#include <string>
#include <algorithm>

using std::string;
using namespace std;

int min(int a, int b, int c){
	if(a < b && a < c)
		return a;
	else if(b < a && b < c)
		return b;
	return c;
}


int edit_distance(const string &str1, const string &str2) {
  //write your code here
  int n = str1.length();
  int m = str2.length();
  int arr[m][n];
  for (int j = 0; j <= m; j++){
  	for (int i = 0; i <= n; i++){
  		if (j == 0) 
    		arr[i][j] = i;
			
			if (i == 0)
    		arr[i][j] = j;

  		else if (str2[i] == str1[j]) {
  			arr[i][j] = arr[i - 1][j - 1];
  		}else{
  			arr[i][j] = 1 + min(arr[i][j - 1] , arr[i - 1][j] , arr[i - 1][j - 1]);
  		}
  	}
  }
  for (int i = 0; i < m; ++i) {
  	for (int j = 0; j < n; ++j) {
  		std::cout << arr[i][j] << " ";
  	}
  	std::cout << "\n";
  }
  return arr[m - 1][n - 1];
}

int main() {
  string str1;
  string str2;
  std::cin >> str1 >> str2;
  std::cout << edit_distance(str1, str2) << std::endl;
  return 0;
}
