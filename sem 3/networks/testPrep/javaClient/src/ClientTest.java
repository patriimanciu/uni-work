import java.io.*;
import java.net.Socket;
import java.util.Scanner;

public class ClientTest {
    public static void main(String[] args) {
        String ip = "172.20.10.10";
        int port = 7777;

        try (Socket clientSocket = new Socket(ip, port);
             OutputStream outputStream = clientSocket.getOutputStream();
             PrintWriter writer = new PrintWriter(new OutputStreamWriter(outputStream, "UTF-8"), true);
             Scanner scanner = new Scanner(System.in);
             BufferedReader reader = new BufferedReader(new InputStreamReader(clientSocket.getInputStream(), "UTF-8"))) {

            System.out.println("Try guessing the number generated from server.");
            while (true) {
                System.out.print("Enter a number: ");
                String word = scanner.nextLine();
                writer.println(word);

                String response = reader.readLine();
                System.out.println("Server response: " + response);
                if (response.equals("Congrats!")) {
                    break;
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

