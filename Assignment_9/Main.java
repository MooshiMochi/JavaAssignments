package Assignment_9;

import java.util.Scanner;

class Main {
  public static void main(String[] args) {
    System.out.print("Welcome. What is your name? ");
    Scanner in = new Scanner(System.in);
    String name = in.nextLine();
    System.out.println("Hello, " + name);
    System.out.println("Enter an integer between 1000 and 9999: ");
    int num = in.nextInt();
      
    System.out.println("Sum of digits:" + Integer.toString(sum(num)));
    System.out.println("Reversed:" + Integer.toString(reverse(num)));
    in.close();
  }

  // create a function that will reverse the number
  public static int reverse(int num) {
    int reversed = 0;
    while (num != 0) {
      int digit = num % 10;
      reversed = reversed * 10 + digit;
      num /= 10;
    }
    return reversed;
  }

  // create a function that will sum the digits
  public static int sum(int num) {
    int sum = 0;
    while (num != 0) {
      sum += num % 10;
      num /= 10;
    }
    return sum;
  }
  
  // create a function that will reverse the number by converting it to a string
  public static String reverseString(int num) {
    String reversed = "";
    String numString = Integer.toString(num);
    for (int i = numString.length() - 1; i >= 0; i--) {
      reversed += numString.charAt(i);
    }
    return reversed;
  }

  // create a function that will sum the digits by converting it to a string
  public static int sumString(int num) {
    int sum = 0;
    String numString = Integer.toString(num);
    for (int i = 0; i < numString.length(); i++) {
      sum += Character.getNumericValue(numString.charAt(i));
    }
    return sum;
  }
}
