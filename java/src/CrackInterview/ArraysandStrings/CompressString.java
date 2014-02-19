package CrackInterview.ArraysandStrings;

/**
 * Created by xin on 2/18/14.
 */
public class CompressString {
    public String compress(String s){
        StringBuilder sb = new StringBuilder();
        char tmp = 0;
        int count = 0;
        for(char c : s.toCharArray()){
            if(c==tmp){
                count += 1;
            }
            else{
                if(tmp != 0) sb.append(tmp);
                if(count > 0) sb.append(count);
                count = 1;
            }
            tmp = c;
        }
        sb.append(tmp);
        if(count > 1) sb.append(count);
        if(sb.length() >= s.length()) return s;
        return sb.toString();
    }
    public static void main(String[] args){
        CompressString s = new CompressString();
        String result = s.compress("aabcccccaaa ");
        System.out.println(result);
    }
}
