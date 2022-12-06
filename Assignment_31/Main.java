package Assignment_31;

/**
 * A31
 *
 * @author
 * @version
 */

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.print("How many values? ");
        int n = in.nextInt();
        double[] arr = new double[n];
        for (int i = 0; i < n; i++) {
            System.out.print("Enter next value: ");
            arr[i] = in.nextDouble();
        }
        printArr(arr);
        printArr(ordered(arr));
        System.out.println("Median = " + median(arr));
        in.close();
    }

    /**
     * Computes the median for the set, which is the middle value. If there
     * are two middle values, then the median is the average of those two values.
     * 
     * @param vals - the set of numbers as an array of doubles.
     * @return the median of the set of numbers.
     */
    public static double median(double[] vals) {

        // you need to sort the array vals first
        // (using the method below)
        // then find the middle one and return it
        vals = ordered(vals);
        int middle = 0;
        double median = 0;
        if (vals.length % 2 == 0) {
            middle = vals.length / 2;
            median = (vals[middle] + vals[middle + 1]) / 2;
        } else {
            median = vals[vals.length / 2];
        }
        return median;
    }

    /**
     * Puts the set in order from smallest to largest (using the selection sort
     * algorithm).
     * 
     * @param vals - the set of numbers to be sorted as an array of doubles.
     * @return the sorted array.
     */
    public static double[] ordered(double[] vals) {
        // Starting your search at index 0, find the smallest value,
        // (use the method indexOfSmallest (below) to do this)
        // then move it to the front (swap values).
        vals[0] = vals[indexOfSmallest(vals, 0)];

        // Starting your search at index 1, find the smallest value,
        int index = 0;
        for (int i = 1; i < vals.length; i++) {
            index = indexOfSmallest(vals, i);
            double temp = vals[i];
            vals[i] = vals[index];
            vals[index] = temp;
            i++;
        }
        return vals;
        // then swap it with the value at index 1.

        // Repeat for the rest of the array
        // (smallest at index 2, index 3, etc. and swap them).

        // Print the sorted array using the method below
        // and then return the sorted array.

    }

    /**
     * Finds the index of the smallest value in the set.
     * 
     * @param vals  - the set of numbers as an array of doubles.
     * @param index - the index from which to start the search.
     * @return the index where the smallest value is, starting at the specified
     *         index.
     */
    public static int indexOfSmallest(double[] vals, int index) {

        // Starting at the specified index, find the smallest value
        // in the array and return its index.
        double smallest = vals[index];
        int smallestIndex = index;
        for (int i = index; i < vals.length; i++) {
            if (vals[i] < smallest) {
                smallest = vals[i];
                smallestIndex = i;
            }
        }
        return smallestIndex;
    }

    /**
     * Prints the contents of the given array.
     * 
     * @param arr - the array of doubles to be printed.
     */
    public static void printArr(double[] arr) {
        System.out.print("{");
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i]);
            if (i < arr.length - 1) {
                System.out.print(", ");
            }
        }
        System.out.println("}");
    }
}
