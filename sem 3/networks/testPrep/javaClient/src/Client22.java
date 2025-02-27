import java.io.*;
import java.net.Socket;
import java.util.Scanner;
// unchanged for Server 2_3, 2_4, 2_5

public class Client22 {
    public static void main(String[] args) {
        String ip = "192.168.1.143";
        int port = 1234;

        try (Socket clientSocket = new Socket(ip, port);
             OutputStream outputStream = clientSocket.getOutputStream();
             PrintWriter writer = new PrintWriter(new OutputStreamWriter(outputStream, "UTF-8"), true);
             Scanner scanner = new Scanner(System.in);
             BufferedReader reader = new BufferedReader(new InputStreamReader(clientSocket.getInputStream(), "UTF-8"))) {
            System.out.println("Client connected. Start entering words (until \"stop\" is entered).");
            while (true) {
                System.out.print("> ");
                String line = scanner.nextLine();
                writer.println(line);
                if (line.strip().equals("stop"))
                    break;
            }

            String response = reader.readLine();
            System.out.println("Server response: " + response);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
