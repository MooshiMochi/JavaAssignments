/**
 * This class runs the program for managing a checking account.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */


public class Main {
    public static void main(String[] args) {
        
          
        // create CheckingAccount object with starting deposit of
        // $1000, 1.2% interest rate, and an account owner.
        CheckingAccount acc1 = new CheckingAccount(1000, 0.012, "Mr. Yesilyurt");
        
        // create CheckingAccount object with an account owner (no initial deposit).
        CheckingAccount acc2 = new CheckingAccount("Black Jack");
        
        // print account info for both accounts
        acc1.printInfo();
        acc2.printInfo();
        
        // make one month pass for both accounts
        acc1.runMonth();
        acc2.runMonth();
        
        // print account info for both accounts
        acc1.printInfo();
        acc2.printInfo();
        
        // make three months pass for both accounts
        acc1.runMultMonths(3);
        acc2.runMultMonths(3);
        
        // deposit $300 into both accounts
        acc1.processDeposit(300);
        acc2.processDeposit(300);

        // make eight months pass for both accounts
        acc1.runMultMonths(8);
        acc2.runMultMonths(8);
        
        // print account info for both accounts
        acc1.printInfo();
        acc2.printInfo();
        
        // withdraw $75 from both accounts
        acc1.processWithdrawal(75);
        acc2.processWithdrawal(75);

        // print account info for both accounts
        acc1.printInfo();
        acc2.printInfo();
    }
  }
  