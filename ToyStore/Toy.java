import java.io.*;
import java.util.ArrayList;

public class Toy implements Serializable{
    private int id;
    private String name;
    private int quantity;
    private int frequency;
    static int ch = 0;
    static String filename = "toys.dat";
    static ArrayList<Toy> allToys = readFile();

    public Toy(String name, int quantity, int frequency) {
        allToys = readFile();

        Toy tToys = findToyAllToys(name);

        if (tToys == null) {
            ch += 1;
            this.id = ch;
            this.name = name;
            this.quantity = quantity;
            this.frequency = frequency;
            allToys.add(this);
            safeFile();
            return;
        }

        tToys.quantity += quantity;
        if(tToys.quantity < 0 ){
            tToys.quantity = 0;
        }
        tToys.frequency = frequency;
        safeFile();
    }

     public String getName() {
        return name;
    }

    @Override
    public String toString(){
        return "id - " + this.id + ", наименование - " + this.name + ", количество - " + this.quantity + ", частота - " + this.frequency;
    }

    public static void safeFile(){
        try(ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(filename)))
        {
            oos.writeObject(allToys);
        }
        catch(Exception ex){
            System.out.println(ex.getMessage());
        }
    }

    public static ArrayList<Toy> readFile(){

        try(ObjectInputStream ois = new ObjectInputStream(new FileInputStream(filename)))
        {

            allToys = ((ArrayList<Toy>)ois.readObject());
            ch = allToys.size();
        }
        catch(Exception ex){

            allToys = new ArrayList<>();
            System.out.println(ex.getMessage());
        }

        return allToys;

    }

    public Toy findToyAllToys(
            String name) {

        if(allToys != null) {
            for (Toy toy : allToys) {
                if (toy.getName().equals(name)) {
                    return toy;
                }
            }
        }
        return null;
    }

    static void getPrizeToy(int y) {
        int totalFrequency = 0;

        allToys = readFile();
        for (Toy toy : allToys) {
            if(toy.quantity > 0) {
                totalFrequency += toy.frequency;
            }
        }

        if(totalFrequency == 0){
            return;
        }

        int randomNumber = (int) (Math.random() * totalFrequency);

        int currentFrequency = 0;

            for (Toy t : allToys) {
                if(y <= 0){
                    break;
                }
                if (t.quantity <= 0) {
                    continue;
                }
                currentFrequency += t.frequency;
                if (currentFrequency >= randomNumber) {
                    y -= 1;
                    System.out.println(t.toString());
                    t.quantity -= 1;
                    safeFile();
                }
            }
            if (y > 0){
                getPrizeToy(y);
            }
    }


    public static void testData(){
        Toy toy1 = new Toy("Мягкая игрушка", 1, 10);
        Toy toy2 = new Toy("Жесткая игрушка", 2, 15);
        Toy toy3 = new Toy("Погремушка", 2, 5);
        Toy toy4 = new Toy("Очень жесткая игрушка", 2, 50);
        Toy toy5 = new Toy("Опасная игрушка", 2, 60);
        Toy toy6 = new Toy("Страшная игрушка", 2, 70);
    }
}
