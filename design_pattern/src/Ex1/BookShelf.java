package Ex1;
import java.util.*;

public class BookShelf implements Aggregate {
//	private Book[] books;
	private ArrayList<Book> books = new ArrayList<Book>();
	private int last = 0;
	public BookShelf(int maxsize) {
//		this.books = new Book[maxsize];
		this.books = new ArrayList<Book>();
	}
	public Book getBookAt(int index) {
//		return books[index];
		return (Book)books.get(index);
	}
	public void appendBook(Book book) {
//		this.books[last] = book;
		this.books.add(book);
		last++;
	}
	public int getLength() {
		return last;
	}
	public Iterator iterator() {
		return new BookShelfIterator(this);
	}
}
