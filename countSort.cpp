#include <iostream>
#include <vector>
using namespace std;

// O(n + k)
void countSort(vector<long long>& A) {
	// find min, max, and make a copy of  A -- O(n)
	long long min = A[0];
	long long max = A[0];
	vector<long long> B;
	B.push_back(A[0]);
	for (long long i = 1; i < A.size(); i++) {
		if (A[i] < min) {
			min = A[i];
		}
		if (A[i] > max) {
			max = A[i];
		}
		B.push_back(A[i]);
	}
	// largest possible difference
	long long k = max - min;
	long long numElements = k + 1;

	// initialize C and I in O(k)
	vector<long long> C;
	vector<long long> I;
	for (long long i = 0; i < numElements; i++) {
		C.push_back(0);
		I.push_back(0);
	}

	// count the number of instances -- O(n)
	for (long long i = 0; i < A.size(); i++) {
		// increment count
		long long correspondingIndex = A[i] - min;
		C[correspondingIndex] += 1;
	}




	// find left boundary of each kind -- O(k)
	for (long long i = 1; i < numElements; i++) {
		I[i] = I[i-1] + C[i-1];
	}

	// move back in sorted order -- O(n)
	for (long long i = 0; i < A.size(); i++) {
		// maps to corresponding index/position (not value) in C and I
		long long correspondingIndex = B[i] - min;
		A[I[correspondingIndex]] = B[i];
		I[correspondingIndex] += 1;
	}
}




int main() {
	long long arraySize;
	vector<long long> array;
	cin >> arraySize;
	if (arraySize == 0) return 0;

	for (long long i = 0; i < arraySize; i++) {
		long long element;
		cin >> element;
		array.push_back(element);
	}

	countSort(array);
	for (long long i = 0; i < array.size(); i++) {
		cout << array[i] << endl;
	}
}
