import javax.xml.crypto.Data;
import java.io.*;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.Socket;
import java.util.Scanner;

public class PracticeClient {
    public static void main(String[] args) {
        String ip = "192.168.8.100";
        int TCP_PORT = 1234;
        int UDP_PORT = 7777;

        try {
            // bradcast
            DatagramSocket udpSocket = new DatagramSocket(UDP_PORT);
            byte[] buf = new byte[1024];
            DatagramPacket packet = new DatagramPacket(buf, buf.length);
            System.out.println("Listening for quiz on UDP port " + UDP_PORT + "...");
            udpSocket.receive(packet);

            String quiz = new String(packet.getData(), 0, packet.getLength());
            System.out.println("Quiz: " + quiz);
            udpSocket.close();

            String[] questions = quiz.split(";");
            String[] answers = new String[questions.length];

            Scanner scan = new Scanner(System.in);
            for (int i = 0; i < questions.length; i++) {
                System.out.println("Question: " + questions[i]);
                System.out.println("Answer: ");
                answers[i] = scan.nextLine().strip();
            }
            scan.close();

            try (Socket clientSocket = new Socket(ip, TCP_PORT);
                 OutputStream outputStream = clientSocket.getOutputStream();
                 PrintWriter writer = new PrintWriter(new OutputStreamWriter(outputStream, "UTF-8"), true);
                 Scanner scanner = new Scanner(System.in);
                 BufferedReader reader = new BufferedReader(new InputStreamReader(clientSocket.getInputStream(), "UTF-8"))) {
                System.out.println("Client connected to TCP port " + TCP_PORT);

                for (int i = 0; i < answers.length; i++) {

                    writer.println(i);
                    writer.println(answers[i]);
                }

                String response = reader.readLine();
                System.out.println("Received from server: " + response);

            } catch (IOException e) {
                System.err.println("Error with TCP connection: " + e.getMessage());
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
