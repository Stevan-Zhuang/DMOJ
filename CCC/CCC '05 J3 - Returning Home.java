import java.util.Scanner;
import java.util.ArrayList;

public class Main {
    public static void main(final String[] args) {
        Scanner sc = new Scanner(System.in);
        
        ArrayList<String> directions = new ArrayList<String>();
        ArrayList<String> places = new ArrayList<String>();

        while (true) {
            directions.add((sc.nextLine().equals("L")) ? "RIGHT" : "LEFT");
            String place = sc.nextLine();
            if (place.equals("SCHOOL")) break;
            places.add(place);
        }

        for (int i = places.size(); i > 0; i--) {
            System.out.println(String.format("Turn %s onto %s street.", directions.get(i), places.get(i - 1)));
        }
        System.out.println(String.format("Turn %s into your HOME.", directions.get(0)));
    }
}
