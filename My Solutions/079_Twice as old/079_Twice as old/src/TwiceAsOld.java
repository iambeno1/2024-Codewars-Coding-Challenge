public class TwiceAsOld {
    public static int TwiceAsOld(int dadYears, int sonYears) throws Exception {
        int ageDifference = dadYears - sonYears;
        int targetAge = sonYears * 2;
        int yearsDifference = Math.abs(targetAge - dadYears);
        return yearsDifference;
    }
}
