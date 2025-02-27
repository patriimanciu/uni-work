import java.io.*;
import java.net.Socket;
import java.util.Scanner;
// unchanged for Server 1_3 adn 1_4
public class Client12 {
    public static void main(String[] args) {
        String ip = "172.20.10.10";
        int port = 1234;

        try (Socket clientSocket = new Socket(ip, port);
             OutputStream outputStream = clientSocket.getOutputStream();
             PrintWriter writer = new PrintWriter(new OutputStreamWriter(outputStream, "UTF-8"), true);
             Scanner scanner = new Scanner(System.in);
             BufferedReader reader = new BufferedReader(new InputStreamReader(clientSocket.getInputStream(), "UTF-8"))) {

//            writer.println(num);
//            String response = reader.readLine();

            System.out.print("Enter a word: ");
            String word = scanner.nextLine();
            writer.println(word);

            String response = reader.readLine();
            System.out.println("Server response: " + response);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

