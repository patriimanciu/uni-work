import java.io.*;
import java.net.Socket;
import java.util.Scanner;

// Clientul trimite serverului un sir de caractere (de exemplu numele utilizatorului citit de la tastatura). Serverul
// afiseaza pe ecran sirul primit si portul clientului si ii raspunde acestuia cu suma cifrelor din Portul clientului.
//C lientul va afisa pe ecran numarul primit.

public class Client41 {
    public static void main(String[] args) {
        String ip = "192.168.8.100";
        int port = 1234;

        try (Socket clientSocket = new Socket(ip, port);
             OutputStream outputStream = clientSocket.getOutputStream();
             PrintWriter writer = new PrintWriter(new OutputStreamWriter(outputStream, "UTF-8"), true);
             Scanner scanner = new Scanner(System.in);
             BufferedReader reader = new BufferedReader(new InputStreamReader(clientSocket.getInputStream(), "UTF-8"))) {
            System.out.println("Client connected");

            System.out.println("Enter the string you want to send: ");
            String message = scanner.nextLine();
            writer.println(message);

            String response = reader.readLine();
            System.out.println("Received from server: " + response);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
