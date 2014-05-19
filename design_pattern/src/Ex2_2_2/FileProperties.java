package Ex2_2_2;

import java.io.*;
import java.util.*;

public class FileProperties implements FileIO{
	private Properties property = new Properties();
	public FileProperties() {
	}
	public void readFromFile(String filename) throws IOException{
		try {
			FileInputStream in = new FileInputStream(filename);
			property.load(in);
		} catch (IOException e) {
			System.err.println("IO Error." + e);
		}
		property.list(System.out);
	}
	public void writeToFile(String filename) throws IOException{
		try{
			FileOutputStream out = new FileOutputStream(filename);
			property.store(out, "writen by FileProperties");
		} catch (IOException e) {
			System.err.println("IO Error." + e);
		}
	}
	public void setValue(String key, String value){
		property.setProperty(key, value);
	}
	public String getValue(String key){
		return property.getProperty(key);
	}
}
