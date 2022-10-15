package in.one2n.exercise;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;
import java.util.function.Function;
import java.util.stream.Collectors;

public class Grader {

    public List<Student> parseCSV(String filepath) {
        List <Student> all_students = new ArrayList <> ();

        try {
            BufferedReader br = new BufferedReader(new FileReader(new File(filepath)));
            all_students = br.lines().skip(1).map(mapToItem).collect(Collectors.toList());
            br.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return all_students;
    }
    private final Function <String, Student> mapToItem = (line) -> {
        String[] items = line.split(",");
        return new Student(items[0], items[1], items[2], Double.parseDouble(items[3]), Double.parseDouble(items[4]), Double.parseDouble(items[5]), Double.parseDouble(items[6]));
    };

    public List<Student> calculateGrade(List<Student> students) {
        students.forEach(everyStudent -> everyStudent.setGrade(everyStudent.get_Grade()));
        return students;
    }

    public Student findOverallTopper(List<Student> gradedStudents) {
        return gradedStudents.stream().max(Comparator.comparingDouble(Student::getFinalScore)).get();
    }

    public Map<String, Student> findTopperPerUniversity(List<Student> gradedStudents) {
        return gradedStudents.stream().collect(Collectors.toMap(Student::getUniversity, Function.identity(), this::getHighestScore));
    }
    private Student getHighestScore(Student s1, Student s2){
        return s1.getFinalScore() > s2.getFinalScore() ? s1 : s2;
    }
}
