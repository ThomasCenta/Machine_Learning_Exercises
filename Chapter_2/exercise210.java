import java.util.Random;

public class Main {
	
	public static Random rand = new Random();
	
	public static final String[] SKY = {"Sunny", "Cloudy", "Rainy"};
	public static final String[] AIR_TEMP = {"Warm", "Cold"};
	public static final String[] HUMIDITY = {"Normal", "High"};
	public static final String[] WIND = {"Strong", "Weak"};
	public static final String[] WATER = {"Warm", "Cool"};
	public static final String[] FORECAST = {"Same", "Change"};
	
	
	public static class FindS {
		
		public String[] hypothesis;
		
		public void addInput(String[] input, boolean positive) {
			if(!positive) { return; }
			if(hypothesis == null) {
				hypothesis = input;
			}else {
				for(int i = 0; i < 6; i += 1) {
					if(!hypothesis[i].equals("?") && !hypothesis[i].equals(input[i])) {
						hypothesis[i] = "?";
					}
				}
			}
		}
		
		public String[] getHypothesis() {
			return hypothesis;
		}
		
		public void printHypothesis() {
			if(hypothesis == null) {
				System.out.println("<0,0,0,0,0,0>");
				return;
			}
			System.out.print("<" + hypothesis[0]);
			for(int i = 1; i < 6; i += 1) {
				System.out.print(","+hypothesis[i]);
			}
			System.out.println(">");
		}
	}
	
	public static boolean classify(String[] input, String[] targetConcept) {
		for(int i = 0; i < 6; i += 1) {
			if(!targetConcept[i].equals("?") && !targetConcept[i].equals(input[i])) {
				return false;
			}
		}
		return true;
	}
	
	public static boolean arrayEquals(String[] one, String[] two) {
		if(one == null && two == null) return true;
		if(one == null || two == null) return false;
		if(one.length != two.length) return false;
		for(int i = 0; i < one.length; i += 1) {
			if(one[i] == null && two[i] == null) {continue; }
			if(one[i] == null || two[i] == null) return false;
			if(!one[i].equals(two[i])) return false;
		}
		return true;
	}
	
	public static String[] generateInput() {
		String[] input = new String[6];
		input[0] = SKY[rand.nextInt(3)];
		input[1] = AIR_TEMP[rand.nextInt(2)];
		input[2] = HUMIDITY[rand.nextInt(2)];
		input[3] = WIND[rand.nextInt(2)];
		input[4] = WATER[rand.nextInt(2)];
		input[5] = FORECAST[rand.nextInt(2)];
		return input;
	}
	
	public static void main(String[] args) {
		/*Test
		 * 
		 * FindS hypothesis = new FindS();
		 * String[][] test = {{"Sunny", "Warm", "Normal", "Strong", "Warm", "Same"},
				{"Sunny", "Warm", "High", "Strong", "Warm", "Same"},
				{"Sunny", "Warm", "High", "Strong", "Cool", "Change"}};
			for(String[] in: test) {
				hypothesis.addInput(in, true);
				hypothesis.printHypothesis();
			}
		 */
		
		String[] targetConcept = {"Sunny", "Warm", "?", "?", "?", "?"};
		int testCases = 100000;
		int totalTries = 0;
		for(int i = 0; i < testCases; i += 1) {
			FindS hypothesis = new FindS();
			int numTries = 0;
			while(!arrayEquals(targetConcept, hypothesis.getHypothesis())) {
				String[] input = generateInput();
				hypothesis.addInput(input, classify(input, targetConcept));
				numTries += 1;
			}
			System.out.println(numTries);
			totalTries += numTries;
		}
		System.out.println("average: "+ (totalTries/testCases));
	}
}
