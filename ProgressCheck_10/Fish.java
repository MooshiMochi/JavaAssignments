
package ProgressCheck_10;

public class Fish
{
  private String name;
  private double weightOfFish;
  private double length;

  // default constructor
  public Fish()
  {
    name = "Fish";
    weightOfFish = 2.0; // lbs
    length = 10;  // in.
  }

  // more specific constructor
  public Fish(String n, double w, double l)
  {
    // initialize the instance variables
    // write code here...
    this.name = n;
    this.weightOfFish = w;
    this.length = l;    
  }

  // Method: printMessage()
  // print the name, weight, and length of the fish
  public void printMessage()
  {
    System.out.println("Name: " + name);
    System.out.println("Weight: " + weightOfFish);
    System.out.println("Length: " + length);
  }

  // Method: eatFood(int weightOfFood)
  // add the weight of the food to the fish's weight
  // note: update the instance variable
  public void feedFood(double weightOfFood)
  {
    weightOfFish += weightOfFood;
  }
  
}

