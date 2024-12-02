import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

public class GitLabApiExample {
    public static void main(String[] args) throws Exception {
        String url = "https://gitlab.example.com/api/v4/groups";
        String token = "YOUR_ACCESS_TOKEN";

        HttpURLConnection connection = (HttpURLConnection) new URL(url).openConnection();
        connection.setRequestMethod("GET");
        connection.setRequestProperty("Authorization", "Bearer " + token);

        BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()));
        String line;
        StringBuilder response = new StringBuilder();

        while ((line = reader.readLine()) != null) {
            response.append(line);
        }
        reader.close();

        System.out.println("Response:");
        System.out.println(response.toString());

        connection.disconnect();
    }
}
