package FindSubstring;

public class Main {
    

    public static void main(String[] args) {
        String str = "javaXDjava";


        String resp = sameEnds2(str);
        System.out.println(resp);
    }

    public static String sameEnds(String str) {
        String result = "";
        int len = str.length();
        int i = 0;

        while (true) {
            if (str.substring(0, i).equals(str.substring(len - i, len))) {
                result = str.substring(0, i);
            }
            i++;
            if (i > len / 2) {
                break;
            }
        }

        return result;
    }

    public static String sameEnds2(String s) {
        int stop = 0;
        int index = 0;
        String str = "";

        while (stop != -1) {
            if (s.indexOf(s.substring(0, index + 1), s.length() / 2) != -1) {
                index++;
                System.out.printf("Incrementing index %d\n", index);
            }
            else {
                stop = -1;
                System.out.println("Stopping while loop");
            }
            if (index != 0) {
                str = s.substring(0, index);
                System.out.printf("Set new result to %s\n", str);
            }
        }
        return str;
    }
}
