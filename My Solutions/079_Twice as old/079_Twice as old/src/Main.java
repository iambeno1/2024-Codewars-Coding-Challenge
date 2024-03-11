public class Main {
    public static void main(String[] args) {
        int yearsAgo;
        try {
            yearsAgo = TwiceAsOld.TwiceAsOld(30, 5);
            System.out.println("Years ago: " + yearsAgo);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}


/*
 * Sample Tests
 * import org.junit.Test;
import static org.junit.Assert.assertEquals;
import org.junit.runners.JUnit4;


public class TwiceAsOldTest {
    @Test
    public void testSomething() {
      assertEquals(30, TwiceAsOld.TwiceAsOld(30,0));
      assertEquals(16, TwiceAsOld.TwiceAsOld(30,7));
      assertEquals(15, TwiceAsOld.TwiceAsOld(45,30));
      
    }
}
 */