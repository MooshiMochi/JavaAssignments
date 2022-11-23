package FindMinMaxValues;


public class Main {

    public static void main(String[] args) {

        
        int max = 0;
        int min = 0;
        Boolean first = true;

        String numbers = "124351646146";


        System.out.printf("The string of numbers is: %s\n", numbers);

        for (int i = 0; i < numbers.length(); i++) {
            int num = Integer.parseInt(numbers.substring(i, i + 1));
            if (first) {
                max = num;
                min = num;
                first = false;
            } else {
                if (num > max) {
                    max = num;
                }
                if (num < min) {
                    min = num;
                }
            }
        }

        System.out.printf("The max number is: %d\n", max);
        System.out.printf("The min number is: %d\n", min);

    }
    
}
