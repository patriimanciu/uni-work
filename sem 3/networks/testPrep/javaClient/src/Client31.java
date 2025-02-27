import java.io.*;
import java.net.Socket;
import java.util.Scanner;
// unchanged for Server 3_2 - 3_5


public class Client31 {
    public static void main(String[] args) {
        String ip = "192.168.8.100";
        int port = 1234;

        try (Socket clientSocket = new Socket(ip, port);
             OutputStream outputStream = clientSocket.getOutputStream();
             PrintWriter writer = new PrintWriter(new OutputStreamWriter(outputStream, "UTF-8"), true);
             Scanner scanner = new Scanner(System.in);
             BufferedReader reader = new BufferedReader(new InputStreamReader(clientSocket.getInputStream(), "UTF-8"))) {
            System.out.println("Client connected");
            System.out.println("a= ");
            String n1 = scanner.nextLine();
            System.out.println("b= ");
            String n2 = scanner.nextLine();

            writer.println(n1);
            writer.println(n2);

            String response = reader.readLine();
            System.out.println("Server response: " + response);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
