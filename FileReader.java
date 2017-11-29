import java.io.*;
import java.util.Scanner;

public class FileReader {

    private Scanner file;

    public void openFile() {
        try {
            file = new Scanner(new File("credentials.txt"));
        }
        catch(Exception e){
            System.out.println("could not find file");
        }
    }

    public void readFile() {
        while(file.hasNext()) {
            String userName = file.next();
            String hashedPassword = file.next();
            String password = file.next();
            String role = file.next();

            System.out.printf("%s %s %s %s\n", userName, hashedPassword, password, role);
        }

    }

    public void closeFile() {
        file.close();
    }
}
