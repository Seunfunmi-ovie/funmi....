import java.util.Arrays; 

public class ShoppingMall { 
    public static void main(String [] funmi){ 
        String [] cart = { "Milk", "Eggs", "Bread", "Chocolate" }; 
        String [] myCart = { "Organic Milk", "Organic Eggs", "Organic Bread", "Chocolate" }; 
        String target1 = "Eggs"; 
        String target2 = "Fish"; 
        
        boolean goods = findItem(cart, target1); 
        System.out.println(goods); 
        
        int itemCount = countItems(cart); 
        System.out.println(itemCount); 
        
        int back = countItemsInCart(cart); 
        System.out.println(back); 
        
        System.out.println(Arrays.toString(upperCase(cart))); 
        System.out.println(countOrganic(myCart)); 
        System.out.println(Arrays.toString(expressCheck(cart))); 
    } 

    public static boolean findItem(String[] cart, String target1){ 
        for(String items : cart){ 
            if(items.equals(target1)){ 
                return true; 
            } 
        } 
        return false; 
    } 

    public static int countItems(String [] cart){ 
        int count = 0; 
        for(String items : cart){ 
            count = count + items.length(); 
        } 
        return count; 
    } 

    public static int countItemsInCart(String [] cart){ 
        int count = 0; 
        for(String items: cart){ 
            count++; 
        } 
        return count; 
    } 

    public static String[] upperCase(String[] cart){ 
        String [] upperCart = new String [cart.length]; 
        for(int count = 0; count < cart.length; count++){ 
            upperCart[count] = cart[count].toUpperCase(); 
        } 
        return upperCart; 
    } 

    public static int countOrganic(String [] myCart){ 
        int count = 0; 
        for(String items : myCart){ 
            if(items.startsWith("Organic")){ 
                count++; 
            } 
        } 
        return count; 
    } 

    public static String[] expressCheck(String[] cart){ 
        int count = 0; 
       
        for(String items : cart){ 
            if(items.length() < 6){ 
                count++; 
            } 
        } 
        
        String[] express = new String [count]; 
        int newCount = 0; 
        for(String items : cart){ 
            if(items.length() < 6){ 
                express[newCount] = items; 
                newCount++; 
            } 
        } 
        return express; 
    } 
}

