#include <iostream>
#include <cmath>
using namespace std;

double geometricSeries(int n, double r) {
    if (n == 0)
        return 1;

    return pow(r, n) + geometricSeries(n - 1, r);
}

int main() {
    int n;
    double r;

    cout << "Enter n: ";
    cin >> n;

    cout << "Enter r: ";
    cin >> r;

    cout << "Result: " << geometricSeries(n, r) << endl;

    return 0;
}
