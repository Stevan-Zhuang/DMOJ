import java.util.Scanner;
import java.util.Arrays;

public class Main {
    public static void main(final String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int cases = sc.nextInt();
        sc.nextLine();
        for (int i = 0; i < cases; i++) {
            String[] words = {sc.nextLine(), sc.nextLine(), sc.nextLine()};
            System.out.println(fixFree(words));
        }
    }

    public static String fixFree(String[] words) {
        Arrays.sort(words, (String x, String y) -> x.length() - y.length());
        if (words[0].equals(words[1].substring(0, words[0].length())) ||
            words[0].equals(words[2].substring(0, words[0].length())) ||
            words[1].equals(words[2].substring(0, words[1].length())) ||
            words[0].equals(words[1].substring(words[1].length() - words[0].length())) ||
            words[0].equals(words[2].substring(words[2].length() - words[0].length())) ||
            words[1].equals(words[2].substring(words[2].length() - words[1].length()))) return "No";
        return "Yes";
    }
}
