/**
 * CheckingAccount models a bank account and can
 * simulate time passing, as well as taking
 * deposits and withdrawals.
 * 
 * @author Mooshi
 * @version 15.09.2022
 */


public class CheckingAccount {
    // Private instance variables
    private double bal;  // balance
    private double r;  // rate
    private String own;  // owner
    private int age; // account age

    /**
     * Create account with starting balance bal, interest rate r, owner own
     * Remember to initialize all class variables.
     */
    public CheckingAccount(double bal, double r, String own)
    {
        this.bal = bal;
        this.r = r;
        this.own = own;
        this.age = 0;
    
    }
    
    /**
     * Create account with owner given, but without an initial deposit
     * Remember to initialize all class variables (set rate = 0.001).
     */
    public CheckingAccount(String own)
    {
        this.own = own;
        this.r = 0.001;
    }

    /**
     * Get the balance (getter)
     * 
     * @return returns the current balance in the account
     */
    public double getBalance()
    {
        return this.bal;
    }
    
    /**
     * Get the account owner (getter)
     * 
     * @return returns the name of the owner on the account
     */
    public String getOwner() 
    {
        return this.own;
    }
    
    /**
     * Get the interest rate (getter)
     * 
     * @return returns the interest rate for the account (as a decimal)
     */
    public double getRate()
    {   
        return this.r * 100;
    }
    
    /**
     * Get the account age (getter)
     * 
     * @return returns the number of months account has been open
     */
    public int getAge() 
    {
        return this.age;
    }
    
    /**
     * Deposits some money into the account (amount > 0)
     * 
     * @param amount - the amount of money to be deposited into the account
     */
    public void processDeposit(double amount)
    {
        if (amount > 0) {
            this.bal += amount;
        }
    }
    
    /**
     * Withdraws some money into the account (amount > 0)
     * 
     * @param amount - the amount of money to be taken out of the account
     */ 
    public void processWithdrawal(double amount)
    {
        if (amount > 0 && amount <= this.bal) {
            this.bal -= amount;
        }
        else if (amount > this.bal) {
            System.out.println("Insufficient funds.");
        }
    }
    
    /**
     * Simulates a month passing.
     *
     * 
     * A = P * (1 + (rate / 12))
     * 
     * P is current amount
     * A is new amount after interest is added.
     */
    public void runMonth()
    { 
        /* Interest is added to balance and acctAge is incremented by one
         * A = P * (1 + (rate / compounds))
         * P is current amount in the account
         * A is new amount after interest is added */
        this.bal = this.bal * (1 + this.r / 12);
        this.age++;
    }
    
    /**
     * The account info (age, owner, rate, balance) is printed.
     */
    public void printInfo(){
        System.out.println("Checking Account (" + age + " months old)");
        System.out.println("Rate: " + this.getRate() + "%");
        System.out.println("Owner: " + own);
        System.out.printf("Balance: $%.1f\n", bal);
        System.out.println();
    }


    /**
     * Simulate multiple months at once.
     *
     * @param n - the number of months to run.
     */
    public void runMultMonths(int n)
    {
        for(int i = 0; i < n; i++)
        {
            runMonth();
        }
    }
}
