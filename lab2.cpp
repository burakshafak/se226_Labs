

#include <iostream>
using namespace std;

int main()
{

    
    // Task 1 
    

    int n;
    cout << "Please enter a positive integer greater than 9: ";
    cin >> n;

    while (n <= 9)
    {
        cout << "Please enter a positive integer greater than 9: ";
        cin >> n;
    }

    int current = n;
    int steps = 0;

    cout << current;

    while (current >= 10)
    {
        int temp = current;
        int digit_sum = 0;

        while (temp > 0)
        {
            digit_sum += temp % 10;
            temp /= 10;
        }

        current = digit_sum;
        steps++;

        cout << " -> " << current;
    }

    cout << endl;
    cout << "Final value: " << current << endl;
    cout << "Total steps: " << steps << endl;

    cout << "\n-------------------------------\n" << endl;


   
    // Task 2 
    

    cout << "Please enter a number between 10 and 100: ";
    cin >> n;

    while (n < 10 || n > 100)
    {
        cout << "Invalid input. Please enter a number between 10 and 100: ";
        cin >> n;
    }

    int fizz_count = 0;
    int buzz_count = 0;
    int fizzbuzz_count = 0;

    for (int i = 1; i <= n; i++)
    {

        if (i % 7 == 0)
        {
            cout << "(" << i << " is skipped)" << endl;
            continue;
        }

        if (i % 3 == 0 && i % 5 == 0)
        {
            cout << "FizzBuzz" << endl;
            fizzbuzz_count++;
        }
        else if (i % 3 == 0)
        {
            cout << "Fizz" << endl;
            fizz_count++;
        }
        else if (i % 5 == 0)
        {
            cout << "Buzz" << endl;
            buzz_count++;
        }
        else
        {
            cout << i << endl;
        }
    }

    cout << "--- Summary ---" << endl;
    cout << "Fizz count : " << fizz_count << endl;
    cout << "Buzz count : " << buzz_count << endl;
    cout << "FizzBuzz count: " << fizzbuzz_count << endl;

    cout << "\n-------------------------------\n" << endl;


    
    // Task 3 
   

    cout << "Please enter a number between 3 and 9: ";
    cin >> n;

    while (n < 3 || n > 9)
    {
        cout << "Please enter a number between 3 and 9: ";
        cin >> n;
    }

    for (int i = 1; i < 2 * n; i++)
    {
        int k;

        if (i <= n)
            k = i;
        else
            k = 2 * n - i;

        for (int j = 1; j <= k; j++)
        {
            cout << j;
        }

        cout << endl;
    }

    return 0;
}
