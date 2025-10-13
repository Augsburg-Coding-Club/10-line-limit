public class Henry{
	public static void main(String[] args){
		for (int i = 0; i < (int)(Math.random()*100)+10; i++){
			for (int j = 0; j < (int)(Math.random()*50)+1; j++){
				System.out.print(" ");
			}
			System.out.println("*");
		}
	}
}