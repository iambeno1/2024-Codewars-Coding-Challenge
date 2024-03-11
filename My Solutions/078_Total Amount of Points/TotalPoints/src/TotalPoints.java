public class TotalPoints {
    public static int points(String[] games) {
        int totalPoints = 0;

        for(String game : games){
            String[] scores = game.split(":");
            int ourScore = Integer.parseInt(scores[0]);
            int opponentScore = Integer.parseInt(scores[1]);

            if(ourScore > opponentScore){
                totalPoints += 3; // menang, tambahkan 3 poin
            } else if(ourScore == opponentScore){
                totalPoints += 1; // seri, tambah 1 poin
            }
        }
        return totalPoints;
    }
}

/*
 Sample Tests
 * 
 * import org.junit.Test;
import static org.junit.Assert.assertEquals;
import org.junit.runners.JUnit4;

public class SolutionTest {
    @Test
    public void basicTests() {
        assertEquals(30, TotalPoints.points(new String[]
                         {"1:0","2:0","3:0","4:0","2:1","3:1","4:1","3:2","4:2","4:3"}));
                     
        assertEquals(10, TotalPoints.points(new String[]
                         {"1:1","2:2","3:3","4:4","2:2","3:3","4:4","3:3","4:4","4:4"}));
                     
        assertEquals(0, TotalPoints.points(new String[]
                         {"0:1","0:2","0:3","0:4","1:2","1:3","1:4","2:3","2:4","3:4"}));
        
        assertEquals(15, TotalPoints.points(new String[]
                         {"1:0","2:0","3:0","4:0","2:1","1:3","1:4","2:3","2:4","3:4"}));
                     
        assertEquals(12, TotalPoints.points(new String[]
                         {"1:0","2:0","3:0","4:4","2:2","3:3","1:4","2:3","2:4","3:4"}));
    }
}
 */
