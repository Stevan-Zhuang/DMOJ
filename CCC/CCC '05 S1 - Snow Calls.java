import java.util.Scanner;
import java.util.HashMap;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int numCases = scan.nextInt();
        scan.nextLine();
        for (int i = 0; i < numCases; i++) {
            String phoneNumber = scan.nextLine();
            String result = "";
            HashMap<String, String> characters = new HashMap<>();
            
            characters.put("A", "2");
            characters.put("B", "2");
            characters.put("C", "2");
            characters.put("D", "3");
            characters.put("E", "3");
            characters.put("F", "3");
            characters.put("G", "4");
            characters.put("H", "4");
            characters.put("I", "4");
            characters.put("J", "5");
            characters.put("K", "5");
            characters.put("L", "5");
            characters.put("M", "6");
            characters.put("N", "6");
            characters.put("O", "6");
            characters.put("P", "7");
            characters.put("Q", "7");
            characters.put("R", "7");
            characters.put("S", "7");
            characters.put("T", "8");
            characters.put("U", "8");
            characters.put("V", "8");
            characters.put("W", "9");
            characters.put("X", "9");
            characters.put("Y", "9");
            characters.put("Z", "9");
    
            for (int j = 0; j < phoneNumber.length(); j++) {
                String letter = phoneNumber.substring(j, j + 1);
                if (characters.containsKey(letter)) {
                    result += characters.get(letter);
                } else if (!letter.equals("-")) {
                    result += letter;
                }
                if (result.length() == 3 || result.length() == 7) result += "-";
                if (result.length() == 12) break;
            }
            System.out.println(result);
        }
    }
}
