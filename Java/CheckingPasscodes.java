public class CheckingPasscodes {
   public static void main (String [] args) {
      boolean hasDigit = false;
      String passCode = "";
      int valid = 0;

      passCode = "abc";
      int i = 0;
      for (i = 0; i < passCode.length(); ++i) {
         if (Character.isDigit(passCode.charAt(i))) {
            hasDigit = true;
         }
      }

      if (hasDigit) {
         System.out.println("Has a digit.");
      }
      else {
         System.out.println("Has no digit.");
      }

      return;
   }
}