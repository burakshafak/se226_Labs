#include <iostream>
#include <utility>
using namespace std;


void swapValues(int* p1, int* p2) {
    int temp = *p1;
    *p1 = *p2;
    *p2 = temp;
}
void reverseArray(int* arr, int size) {
    int start = 0;
    int end = size - 1;

    while (start < end) {
    
        std::swap(arr[start], arr[end]);

        /
        start++;
        end--;
    }
}


void printArray(int* arr, int size) {
    for (int i = 0; i < size; i++) {
        cout << *(arr + i) << " ";
    }
    cout << endl;
}


int findSum(int* arr, int size) {
    int sum = 0;
    for (int i = 0; i < size; i++) {
        sum += *(arr + i);
    }
    return sum;
}





int* createArray(int size) {
    int* arr = new int[size];
    return arr;
}


void deleteArray(int* arr) {
    delete[] arr;
}

int main() {

    cout << "Creating array" << endl;

    int size;
    cout << "Enter array size: ";
    cin >> size;

    int* arr = createArray(size);

    cout << "Enter values: ";
    for (int i = 0; i < size; i++) {
        cin >> *(arr + i);
    }

    cout << "Array elements:" << endl;
    printArray(arr, size);



    cout << "Sum of elements: " << findSum(arr, size) << endl;

    cout << "----------------------------------" << endl;

    cout << "Swapping two numbers" << endl;

    int a = 5, b = 8;

    cout << "Before swap" << endl;
    cout << "a = " << a << endl;
    cout << "b = " << b << endl;

    swapValues(&a, &b);

    cout << "After swap" << endl;
    cout << "a = " << a << endl;
    cout << "b = " << b << endl;

    cout << "---------------" << endl;
    cout << "Reversed array:" << endl;

    reverseArray(arr,size);
    printArray(arr, size);

    cout << "---------------" << endl;

    

    cout << "Deleting array" << endl;

    deleteArray(arr);

    cout << "Memory released." << endl;

    return 0;
}
