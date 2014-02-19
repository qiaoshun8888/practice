package CrackInterview.ArraysandStrings;

/**
 * Created by xin on 2/18/14.
 */
public class ReplaceSpaces {
    public String replace(String s, int trueLength){
        int last = trueLength;
        char[] cl = s.toCharArray();
        for(int i = 0; i < trueLength; i++){
            if(cl[i] == ' '){
                last += 2;
            }
        }
        while(last > 0){
            if(cl[--trueLength] == ' '){
                cl[--last] = '0';
                cl[--last] = '2';
                cl[--last] = '%';
            }else{
                cl[--last] = cl[trueLength];
            }
        }
        return new String(cl);
    }
    public static void main(String[] args){
        ReplaceSpaces s = new ReplaceSpaces();
        System.out.print(s.replace("hello world  ", 11));

    }
}

