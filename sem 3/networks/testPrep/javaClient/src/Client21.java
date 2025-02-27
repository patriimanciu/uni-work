import java.io.*;
import java.net.Socket;
import java.util.Scanner;

public class Client21 {
    public static void main(String[] args) {
        String ip = "192.168.1.143";
        int port = 1234;

        try (Socket clientSocket = new Socket(ip, port);
             OutputStream outputStream = clientSocket.getOutputStream();
             PrintWriter writer = new PrintWriter(new OutputStreamWriter(outputStream, "UTF-8"), true);
             Scanner scanner = new Scanner(System.in);
             BufferedReader reader = new BufferedReader(new InputStreamReader(clientSocket.getInputStream(), "UTF-8"))) {

            System.out.print("Enter the number of words to be sent: ");
            String num = scanner.nextLine();
            writer.println(num);

            System.out.print("Enter words to be sent (" + num.length() + ") :");
            int p = Integer.parseInt(num);
            for (int i = 0; i < p; i++) {
                System.out.print("> ");
                String w = scanner.nextLine();
                writer.println(w);
            }

            String response = reader.readLine();
            System.out.println("Server response: " + response);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
