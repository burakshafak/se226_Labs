

#include <iostream>
#include <cmath>
using namespace std;

int main() {

   
    // TASK 1 
   

    cout << "----- TASK 1 -----" << endl;

    string name;
    string studentID;

    cout << "What is your name?" << endl;
    cin >> name;

    cout << "Hello " << name << "." << endl;

    cout << "What is your Student ID?" << endl;
    cin >> studentID;

    cout << "Your ID is " << studentID << "." << endl;


    
    // TASK 2
    

    cout << "\n----- TASK 2 -----" << endl;

    int totalSeconds;

    cout << "Enter total seconds: ";
    cin >> totalSeconds;

    int hours = totalSeconds / 3600;
    int remainingSeconds = totalSeconds % 3600;
    int minutes = remainingSeconds / 60;
    int seconds = remainingSeconds % 60;

    cout << totalSeconds << " seconds is "
         << hours << " hours, "
         << minutes << " minutes, and "
         << seconds << " seconds." << endl;


    
    // TASK 3 
   

    cout << "\n----- TASK 3 -----" << endl;

    double x1, y1, x2, y2;

    cout << "Enter x1: ";
    cin >> x1;

    cout << "Enter y1: ";
    cin >> y1;

    cout << "Enter x2: ";
    cin >> x2;

    cout << "Enter y2: ";
    cin >> y2;

    double distance = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));

    cout << "The distance between the points is " << distance << endl;


    
    // TASK 4 
    

    cout << "\n----- TASK 4 -----" << endl;

    cout << "*******\n *****\n  ***\n   *" << endl;


    return 0;
}
