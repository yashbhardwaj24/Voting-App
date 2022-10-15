package in.one2n.exercise;

public class Student {

    private String firstname;
    private String lastname;
    private String university;
    private Double test1Score;
    private Double test2Score;
    private Double test3Score;
    private Double test4Score;

    // computed fields
    private Double finalScore;
    private Grade grade;

    public Student(String firstname, String lastname, String university) {
        this.firstname = firstname;
        this.lastname = lastname;
        this.university = university;
    }

    public Student(String firstname, String lastname, String university, Double test1Score, Double test2Score, Double test3Score, Double test4Score) {
        this.firstname = firstname;
        this.lastname = lastname;
        this.university = university;
        this.test1Score = test1Score;
        this.test2Score = test2Score;
        this.test3Score = test3Score;
        this.test4Score = test4Score;
        this.finalScore = (this.test1Score + this.test2Score + this.test3Score + this.test4Score) / 4;
    }

    public Double getFinalScore() {
        return this.finalScore;
    }

    public Grade getGrade() {
        return this.grade;
    }

    public void setGrade(Grade grade){
        this.grade = grade;
    }

    public String getUniversity(){
        return this.university;
    }

    public Grade get_Grade(){
        double finalScore = this.getFinalScore();
        if(finalScore < 35){
            return Grade.F;
        }else if (finalScore >= 35 && finalScore < 50) {
            return Grade.C;
        }else if (finalScore >= 50 && finalScore < 70) {
            return Grade.B;
        }else return Grade.A;
    }

    @Override
    public boolean equals(Object obj) {
        if(this == obj) return true;
        if(obj == null || this.getClass() != obj.getClass()) {
            return false;
        }
        Student student = (Student) obj;
        return this.firstname.equals(student.firstname)
                && this.lastname.equals(student.lastname)
                && this.university.equals(student.university);
    }
}

