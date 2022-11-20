package PrintingShapes;

import java.util.Scanner;

public class Main {

    private static Scanner sc = new Scanner(System.in);
    
    public static void main(String args[]) {

        System.out.print("Enter the size of the object: ");
        int size = sc.nextInt();

        System.out.println("Enter the type of object: ");
        String type = sc.next();

        if (type.equals("square")) {
            printSquare(size);
        } else if (type.equals("triangle")) {
            printTriangle(size);
        } else if (type.equals("rightTriangle")) {
            printRightTriangle(size);
        } else {
            System.out.println("Invalid input");
        }
    };

    public static void printSquare(int size) {
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                if (i == 0 || i == size - 1) {
                    System.out.print("*");
                } else if (j == 0 || j == size - 1) {
                    System.out.print("*");
                } else {
                    System.out.print(" ");
                }
            }
            System.out.println();
        }
    }

    
    public static void printTriangle(int size) {
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size - i - 1; j++) {
                System.out.print(" ");
            }
            for (int j = 0; j < i + 1; j++) {
                System.out.print("* ");
            }
            System.out.println();
        }
    }


    public static void printRightTriangle(int size) {
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < i + 1; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }

}
