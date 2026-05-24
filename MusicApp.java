import java.util.Arrays;
public class MusicApp{
public static void main(String[] args){

String[] playlist = {"Stay - Justin Bieber", "Blinding Lights - The Weeknd", "Stay - Kid LAROI", "Hello - Adele"};
String target = "Hello - Adele";
boolean play = searchPlayList(playlist,target);
System.out.println("PLAYLIST: " + play);
String [] case1 = toLowerCase(playlist);
System.out.println(Arrays.toString(case1) + " "); 

    String [] case2 = miniMix(playlist);
    System.out.print(Arrays.toString(case2)+ " ");
}

public static boolean searchPlayList(String[] playlist, String target){
    
    for(String list : playlist){
    if(list.contains(target)){
    return true;
    }
    }
    return false;
}
public static String [] toLowerCase(String [] playlist){
String [] lowerCase = new String [playlist.length];
for(int count = 0; count < playlist.length; count++){
lowerCase[count] = playlist[count].toLowerCase();

}
return lowerCase;
}
public static String [] miniMix(String [] playlist){
int count = 0;
for(String list: playlist){
if(list.length() < 15){
count++;
}
}
        
        String[] newCount = new String [count];
        int newCounts = 0;
        for(String list : playlist){
        if(list.length() < 15){
        newCount[newCounts] = list;
        }
        } 
return newCount;

}
}
