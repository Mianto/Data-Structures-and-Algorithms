#include <iostream>
#include <cstdlib>

long long get_fibonacci_huge_naive(long long n, long long m) {
    if (n <= 1)
        return n;

    long long previous = 0;
    long long current  = 1;

    for (long long i = 0; i < n - 1; ++i) {
        long long tmp_previous = previous;
        previous = current;
        current = tmp_previous + current;
    }

    return current % m;
}


long long pisano_number(long long n){
    
}

long long fibo(long long n, long long m){
    long long arr[n];
    arr[0] = 0;
    arr[1] = 1;
    for(int i = 2; i <= n; i++){
        arr[i] = (arr[i - 1] + arr[i - 2]) % m;
    }
    return arr[n];
}

long long fibo_huge(long long n, long long m){
    long long c = pisano_number(m);
    n = n % c;
    return fibo(n, m);
}

void tester(){
    while (1){
        int n = rand() % 1000;
        int m = rand() % 500;
        n = (long long) n;
        m = (long long) m;
        if (fibo_huge(n, m) != get_fibonacci_huge_naive(n, m)){
            std::cout << n <<" "<<m;
            break;
        }else{
            std::cout << "OK";
        }

    }
}


int main() {
    long long n, m;
    //std::cin >> n >> m;
    //std::cout << get_fibonacci_huge_naive(n, m) << '\n';
    //std::cout << fibo_huge(n, m) << std::endl;
    tester();
}
