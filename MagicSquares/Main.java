

import java.util.Scanner;

class Main{

    private static Scanner sc = new Scanner(System.in);
public static void main(String[] args){

    // Get the number of magic squares to find.
    System.out.println("Enter the amount of magic squares u want to find:");
    int numOfSquares = sc.nextInt();


    // make sure the number of squares is > 1 as all other values are not magic squares.
    if (numOfSquares < 1){
        System.out.println("Invalid input");
        sc.close();
        return;
    }

    // Start a timer to see how long it takes to find the magic squares.
    long startTime = System.currentTimeMillis();

    // find the magic squares
    printMagicSquares(numOfSquares);

    long endTime = System.currentTimeMillis();

    long duration = (endTime - startTime);

    System.out.println("Program finished executing in " + duration / 1e3  + " seconds...");


    // close the scanner to save resources.
    sc.close();
    };

    /*
     * @param numOfSquares: the number of magic squares to find.
     * 
     * numOfSquaresToBeFound is the number of magic squares to be found.
     * AmountFound is the number of magic squares that we've found so far. This will basically be our index when printing out the magic squares.
     * SumSoFar is the sum of the numbers from 1 up to the current magic square. We save the sum to make the program more efficient.
     * LastAddedDigit is the last digit that was added to the SumSoFar. We save this to make the program more efficient.
     * TotalNumsAdded is the total number of numbers that have been added to make SumSoFar. This is used to determine how many numbers you need to add to get the magic square.
     */
    public static void printMagicSquares(int NumOfSquares) {

        int numOfSquaresToBeFound = NumOfSquares;
        int AmountFound = 0;
        long SumSoFar = 0;
        long LastAddedDigit = 0;
        long TotalNumsAdded = 0;

        // This is our index that we will follow to find the magic squares.
        long n = 0;

        // While we haven't found the number of magic squares we want to find.
        while (AmountFound != numOfSquaresToBeFound) {
            n++;

            // find the square of n
            long SquareOfN = n * n;

            // find the sum of the digits from 1 up to the same value as square of n.
            while (SumSoFar < SquareOfN) {
                // Increment the last digit added by 1.
                LastAddedDigit ++;
                // Increment the number of total digits added.
                TotalNumsAdded ++;
                // Add the last digit added to the sum so far.
                SumSoFar += LastAddedDigit;
            }

            // if sum so far is equal to the square of n then we have found a magic square.
            if (SumSoFar == SquareOfN) {
                // increment the number of magic squares found.
                AmountFound ++;
                System.out.println("#" + AmountFound + " " + SquareOfN + " (1 to " + TotalNumsAdded + ")");
                
                // this is where we ask whether the user wants to find more magic squares.
                if (AmountFound == numOfSquaresToBeFound) {
                    
                    System.out.println("Enter the next amount of magic squares (or enter 0 or less to stop): ");
                    int newAmount = sc.nextInt();
                    if (newAmount > 0) {
                        // reset the variables to find the new amount of magic squares so the while loop continues.
                        numOfSquaresToBeFound += newAmount;
                    } else {
                        return;
                    }
                }
            }
        }
        
    }
}