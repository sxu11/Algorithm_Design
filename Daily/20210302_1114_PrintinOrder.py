using System.Threading;

public class Foo {

    private AutoResetEvent event1;
    private AutoResetEvent event2;

    public Foo() {
        event1 = new AutoResetEvent(false);
        event2 = new AutoResetEvent(false);
    }

    public void First(Action printFirst) {

        // printFirst() outputs "first". Do not change or remove this line.
        printFirst();
        event1.Set();
    }

    public void Second(Action printSecond) {

        // printSecond() outputs "second". Do not change or remove this line.
        event1.WaitOne();
        printSecond();
        event2.Set();
    }

    public void Third(Action printThird) {

        // printThird() outputs "third". Do not change or remove this line.
        event2.WaitOne();
        printThird();
    }
}