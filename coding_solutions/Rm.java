// reverse every row of the given 2D array.

//Given a 2D array arr[][] of size M x N 
//integers where M is the number of rows and N is the number of columns. 
//The task is to reverse every row of the given 2D array.

class Rm {

	static void reverseArray(int arr[][]) {
// System.out.println("debug : Row : M : " + arr.length);

		for (int i = 0; i < arr.length; i++) {
			// System.out.println("debug : Columns : N : " + arr[i].length);

			int start = 0;
			int end = arr[i].length - 1;

			while (start < end) {

				int temp = arr[i][start];
				arr[i][start] = arr[i][end];
				arr[i][end] = temp;

				start++;
				end--;
			}
		}
		for (int i = 0; i < arr.length; i++) {
			for (int j = 0; j < arr[i].length; j++) {
				System.out.print(arr[i][j] + " ");
			}
			System.out.println();
		}

	}

// Driver Code 
	public static void main(String[] args) {
		int arr[][] = { { 1, 2, 3 }, { 4, 5, 6 }, { 7, 8, 9 }, { 10, 9, 8 } };

		// Function call
		reverseArray(arr);

	}
}
