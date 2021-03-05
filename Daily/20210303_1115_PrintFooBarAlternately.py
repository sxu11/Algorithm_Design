using
System.Threading;

public class FooBar {
private int n;
private AutoResetEvent event1;
private AutoResetEvent event2;

public FooBar(int n) {
this.n = n;
event1 = new AutoResetEvent(false);
event2 = new AutoResetEvent(true);
}

public void Foo(Action printFoo) {

for (int i = 0; i < n; i++) {

// printFoo() outputs "foo".Do not change or remove this line.
event2.WaitOne();
printFoo();
event1.Set();
}
}

public void Bar(Action printBar) {

for (int i = 0; i < n; i++) {

// printBar() outputs "bar".Do not change or remove this line.
event1.WaitOne();
printBar();
event2.Set();
}
}
}