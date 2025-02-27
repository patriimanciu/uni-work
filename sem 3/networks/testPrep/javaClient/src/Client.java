import java.io.*;
import java.net.Socket;
import java.util.Scanner;

public class Client {
    public static void main(String[] args) {
        String ip = "192.168.8.100";
        int port = 1234;

        try (Socket clientSocket = new Socket(ip, port);
             OutputStream outputStream = clientSocket.getOutputStream();
             PrintWriter writer = new PrintWriter(new OutputStreamWriter(outputStream, "UTF-8"), true);
             Scanner scanner = new Scanner(System.in);
             BufferedReader reader = new BufferedReader(new InputStreamReader(clientSocket.getInputStream(), "UTF-8"))) {

            // Send the number as a plain UTF-8 string
            System.out.print("Enter a number: ");
            String num = scanner.nextLine();
            writer.println(num);

            // Send each element as a plain UTF-8 string
            int count = Integer.parseInt(num);
            for (int i = 0; i < count; i++) {
                System.out.print("Enter the next element (word): ");
                String element = scanner.nextLine();
                writer.println(element);
            }

            // Read the server response
            String response = reader.readLine();
            System.out.println("Server response: " + response);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
