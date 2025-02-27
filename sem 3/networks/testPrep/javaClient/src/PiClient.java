import java.io.*;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.Socket;
import java.util.Random;

public class PiClient {
    public static void main(String[] args) {
        String ip = "192.168.8.100";
        int TCP_PORT = 1234;
        int UDP_PORT = 7777;
        Random rand = new Random();

        try (Socket clientSocket = new Socket(ip, TCP_PORT);
             OutputStream outputStream = clientSocket.getOutputStream();
             PrintWriter writer = new PrintWriter(new OutputStreamWriter(outputStream, "UTF-8"), true);
             BufferedReader reader = new BufferedReader(new InputStreamReader(clientSocket.getInputStream(), "UTF-8"))) {

            System.out.println("Client connected to TCP port " + TCP_PORT);

            DatagramSocket udpSocket = new DatagramSocket(UDP_PORT);  // Bind explicitly to UDP_PORT for broadcast
            byte[] buf = new byte[1024];
            DatagramPacket packet = new DatagramPacket(buf, buf.length);

            for (int i = 0; i < 100; i++) {
                int n1 = rand.nextInt(100);  // Random x-coordinate
                int n2 = rand.nextInt(100);  // Random y-coordinate
                String mess = n1 + " " + n2;
                writer.println(mess);
                System.out.println("Message sent: " + mess);
            }
            while (true) {
                udpSocket.receive(packet);
                String pi = new String(packet.getData(), 0, packet.getLength());
                System.out.println("UPDATED PI: " + pi);
            }
        } catch (IOException e) {
            System.err.println("Error with TCP connection: " + e.getMessage());
        }
    }
}
