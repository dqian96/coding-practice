import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

import java.time.LocalTime;
import java.time.format.DateTimeFormatter;

public class LogSearcher {
        public Collection<String> search(Collection<String> logLines, LocalTime startDate, LocalTime endDate) {
        Collection<String> filteredLogs = new LinkedList<>();
        DateTimeFormatter formatter = DateTimeFormatter.ISO_DATE_TIME;
        boolean previousLogLineAccepted = false;
        for (String logLine: logLines) {
            String[] tokens = logLine.split("\t");
            LocalTime logDate;
            try {
                // try to parse the first token in the log line as a date
                logDate = LocalTime.parse(tokens[0], formatter);
            } catch (Exception e) {
                // first token is not a date - continuation of previous log line
                if (previousLogLineAccepted) {
                    // accept the continuation if the last log line was accepted
                    filteredLogs.add(logLine);
                }
                continue;
            }
            if (startDate.equals(logDate) || (startDate.isBefore(logDate) && endDate.isAfter(logDate))) {
                // accept new log line
                filteredLogs.add(logLine);
                previousLogLineAccepted = true;
                continue;
            }
            previousLogLineAccepted = false;
        }
        return filteredLogs;
    }

    public static void main(String[] args) throws IOException{
        Scanner in = new Scanner(System.in);
        final String fileName = System.getenv("OUTPUT_PATH");
        BufferedWriter bw = new BufferedWriter(new FileWriter(fileName));
        
        DateTimeFormatter formatter = DateTimeFormatter.ISO_DATE_TIME;
        
        LocalTime startDate = LocalTime.parse(in.nextLine(), formatter);
        LocalTime endDate = LocalTime.parse(in.nextLine(), formatter);
        
        final int numberOfLogLines = Integer.parseInt(in.nextLine());
        Collection<String> logLines = new ArrayList<String>();
        for (int i = 0; i < numberOfLogLines; i++) {
            logLines.add(in.nextLine());
        }
        in.close();
       
        Collection<String> res = new LogSearcher().search(logLines, startDate, endDate);
        for (String logLine : res) {
            bw.write(logLine);
            bw.newLine();
        }
        
        bw.close();
    }
}