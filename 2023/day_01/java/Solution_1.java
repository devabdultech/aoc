import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Solution_1 {
    public static void main(String[] args) {
        int cv = 0;

        try (BufferedReader br = new BufferedReader(new FileReader("C:\\Users\\abdul\\Desktop\\LearningJava\\src\\basics\\input.txt"))) {
            String line;
            while ((line = br.readLine()) != null) {
                Pattern pattern = Pattern.compile("\\d");
                Matcher matcher = pattern.matcher(line);

                StringBuilder digits = new StringBuilder();
                while (matcher.find()) {
                    digits.append(matcher.group());
                }

                if (digits.length() > 0) {
                    cv += Integer.parseInt(digits.charAt(0) + "" + digits.charAt(digits.length() - 1));
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        System.out.println("Congratulations! You've successfully recovered the calibration values. " +
                "The sum of all values is: " + cv + " stars! 🌟✨");
    }
}
