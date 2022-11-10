

import java.util.Scanner;

class Main{

    private static Scanner sc = new Scanner(System.in);
public static void main(String[] args){

    System.out.println("Enter the amount of magic squares u want to find:");
    int num_of_squares = sc.nextInt();

    if (num_of_squares < 1){
        System.out.println("Invalid input");
        sc.close();
        return;
    }

    long startTime = System.currentTimeMillis();
    printMagicSquares(num_of_squares);

    long endTime = System.currentTimeMillis();

    long duration = (endTime - startTime);

    System.out.println("Program finished executing in " + duration / 1e3  + " seconds...");

    sc.close();
    };

    public static void printMagicSquares(int NumOfSquares) {

        int numOfSquaresToBeFound = NumOfSquares;
        int AmountFound = 0;
        long SumSoFar = 0;
        long LastAddedDigit = 0;
        long TotalNumsAdded = 0;

        long n = 0;
        while (AmountFound != numOfSquaresToBeFound) {
            n++;

            long SquareOfN = n * n;

            while (SumSoFar < SquareOfN) {
                LastAddedDigit ++;
                TotalNumsAdded ++;
                SumSoFar += LastAddedDigit;
            }

            if (SumSoFar == SquareOfN) {
                AmountFound ++;
                System.out.println("#" + AmountFound + " " + SquareOfN + " (1 to " + TotalNumsAdded + ")");
                
                if (AmountFound == numOfSquaresToBeFound) {
                    
                    System.out.println("Enter the next amount of magic squares (or enter 0 or less to stop): ");
                    int newAmount = sc.nextInt();
                    if (newAmount > 0) {
                        numOfSquaresToBeFound += newAmount;
                    } else {
                        return;
                    }
                }
            }
        }
        
    }
}