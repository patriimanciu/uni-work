import java.io.*;
import java.net.Socket;
import java.util.Scanner;
// unchanged for Server 3_9


public class Client38 {
    public static void main(String[] args) {
        String ip = "192.168.8.100";
        int port = 1234;

        try (Socket clientSocket = new Socket(ip, port);
             OutputStream outputStream = clientSocket.getOutputStream();
             PrintWriter writer = new PrintWriter(new OutputStreamWriter(outputStream, "UTF-8"), true);
             Scanner scanner = new Scanner(System.in);
             BufferedReader reader = new BufferedReader(new InputStreamReader(clientSocket.getInputStream(), "UTF-8"))) {
            System.out.println("Client connected");

            System.out.println("a = ");
            String a = scanner.nextLine();
            System.out.println("b = ");
            String b = scanner.nextLine();

            writer.println(a);
            writer.println(b);

            String response = reader.readLine();
            System.out.println("Server response: " + response);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
