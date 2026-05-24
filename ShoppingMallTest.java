import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

public class ShoppingMallTest{


@Test

public void testThatFunctionChecksIfAnItemExistInTheCart(){
        
        
        String [] cart = { "Milk", "Eggs", "Bread", "Chocolate" };
        String target1 = "Eggs";
        boolean expectedItems = true;
        boolean actualItems = ShoppingMall.findItem(cart, target1);
        
        assertEquals(expectedItems,actualItems);
        
        }
        
        @Test

public void testThatFunctionCountEachCharactersFoundInTheCart(){
        
        
        String [] cart = { "Milk", "Eggs", "Bread", "Chocolate" };
       
        int expectedItems = 22;
        int actualItems = ShoppingMall.countItems(cart);
        
        assertEquals(expectedItems,actualItems);
        
        }
        
        @Test

public void testThatFunctionCountTheNumberOfItemsInTheCart(){
        
        
        String [] cart = { "Milk", "Eggs", "Bread", "Chocolate" };
       
        int expectedItems = 4;
        int actualItems = ShoppingMall.countItemsInCart(cart);
        
        assertEquals(expectedItems,actualItems);
        
        }
}

