import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int numCases = scan.nextInt();
        scan.nextLine();

        String[] quotients = new String[numCases];
        String[] remainders = new String[numCases];

        for (int curCase = 0; curCase < numCases; curCase++) {

            String dividend = scan.nextLine();
            String divisor = scan.nextLine();

            String quotient = "0";

            int dividendLen = dividend.length();
            int divisorLen = divisor.length();
            for (int pos = 0; pos + divisorLen <= dividendLen; pos++) {
                String partialDividend = dividend.substring(0, pos + divisor.length());

                int count = 0;
                while (canSubtract(partialDividend, divisor)) {
                    partialDividend = subtract(partialDividend, divisor);
                    count++;
                }
                dividend = partialDividend + dividend.substring(pos + divisor.length());
                quotient += String.valueOf(count);
            }

            quotients[curCase] = quotient.replaceFirst("^0+(?!$)", "");
            remainders[curCase] = dividend.replaceFirst("^0+(?!$)", "");
        }

        for (int curCase = 0; curCase < numCases; curCase++) {
            System.out.println(quotients[curCase]);
            System.out.println(remainders[curCase]);
            if (curCase + 1 < numCases) {
                System.out.println(" ");
            }
        }
    }

    static String subtract(String top, String bottom) {
        String result = "";
        String[] tempTop = top.split("");
        String[] tempBottom = bottom.split("");
        for (int i = top.length() - 1; i >= 0; i--) {
            int j = i - (top.length() - bottom.length());
            if (j < 0) {
                result = tempTop[i] + result;
                continue;
            }
            if (Integer.valueOf(tempTop[i]) < Integer.valueOf(tempBottom[j])) {
                tempTop[i] = String.valueOf(Integer.valueOf(tempTop[i]) + 10);
                tempTop[i - 1] = String.valueOf(Integer.valueOf(tempTop[i - 1]) - 1);
            }
            result = String.valueOf(Integer.valueOf(tempTop[i]) - Integer.valueOf(tempBottom[j])) + result;
        } 
        return result;
    }

    static boolean canSubtract(String top, String bottom) {
        top = top.replaceFirst("^0+(?!$)", "");
        if (top.length() != bottom.length()) return top.length() > bottom.length();
        for (int i = 0; i < top.length() - 1; i++) {
            if (Integer.valueOf(top.substring(i, i + 1)) > Integer.valueOf(bottom.substring(i, i + 1))) return true;
            if (Integer.valueOf(top.substring(i, i + 1)) < Integer.valueOf(bottom.substring(i, i + 1))) return false;
        }
        return Integer.valueOf(top.substring(top.length() - 1)) >= Integer.valueOf(bottom.substring(bottom.length() - 1));
    }
}
