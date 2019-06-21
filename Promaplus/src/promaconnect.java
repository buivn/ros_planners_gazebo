/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Keerthi Sreerangaiah
 */
import java.sql.*;
import javax.swing.*;
public class promaconnect {
    
    Connection conn =null;
    public static Connection ConnecrDb(){
        try{
            Class.forName("org.sqlite.JDBC");
            Connection conn= DriverManager.getConnection("jdbc:sqlite:C:\\Users\\Keerthi Sreerangaiah\\Documents\\NetBeansProjects\\Promaplus\\promaplus.sqlite");
            //JOptionPane.showMessageDialog(null,"Connection Established");
            return conn;
        }catch(Exception e){
            JOptionPane.showMessageDialog(null, e);
        return null;
        }
    }
    
    
    
}
