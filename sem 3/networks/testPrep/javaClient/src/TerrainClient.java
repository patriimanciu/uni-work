import java.io.*;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.Socket;
import java.util.Random;
import java.util.Scanner;
import java.util.concurrent.TimeUnit;

public class TerrainClient {
    public static void main(String[] args) {
        String ip = "192.168.8.100";
        int TCP_PORT = 1234;
        int UDP_PORT = 7777;
        Random rand = new Random();

        try (Socket clientSocket = new Socket(ip, TCP_PORT);
             OutputStream outputStream = clientSocket.getOutputStream();
             PrintWriter writer = new PrintWriter(new OutputStreamWriter(outputStream, "UTF-8"), true);
             Scanner scanner = new Scanner(System.in);
             BufferedReader reader = new BufferedReader(new InputStreamReader(clientSocket.getInputStream(), "UTF-8"))) {
            System.out.println("Client connected to TCP port " + TCP_PORT);

            while (true) {
                DatagramSocket udpSocket = new DatagramSocket(UDP_PORT);
                byte[] buf = new byte[1024];
                DatagramPacket packet = new DatagramPacket(buf, buf.length);
                System.out.println("Listening on UDP port " + UDP_PORT + "...");
                udpSocket.receive(packet);

                String map = new String(packet.getData(), 0, packet.getLength());
                System.out.println("UPDATED MAP: " + map);
                udpSocket.close();

                int r = rand.nextInt(10);
                char c = (char)(rand.nextInt(26) + 'a');
                while (c == 'u')
                    c = (char)(rand.nextInt(26) + 'a');

                String s = String.valueOf(r) + " " + String.valueOf(c);
                writer.println(s);
                TimeUnit.SECONDS.sleep(3);
            }
        } catch (IOException e) {
            System.err.println("Error with TCP connection: " + e.getMessage());
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }
    }
}
