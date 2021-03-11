using System.Threading;
using System;

public class FizzBuzz {
    private int n;
    private int i;
    private AutoResetEvent fbEvent;
    private AutoResetEvent fEvent;
    private AutoResetEvent bEvent;
    private AutoResetEvent iEvent;

    public FizzBuzz(int n) {
        this.n = n;
        this.fbEvent = new AutoResetEvent(false);
        this.fEvent = new AutoResetEvent(false);
        this.bEvent = new AutoResetEvent(false);
        this.iEvent = new AutoResetEvent(false);
    }

    // printFizz() outputs "fizz".
    public void Fizz(Action printFizz) {
        while(this.fEvent.WaitOne() && this.i <= this.n)
        {
            //System.Console.WriteLine("fizz");
            printFizz();
            this.iEvent.Set();
        }
    }

    // printBuzzz() outputs "buzz".
    public void Buzz(Action printBuzz) {
        while(this.bEvent.WaitOne() && this.i <= this.n)
        {
            //System.Console.WriteLine("buzz");
            printBuzz();
            this.iEvent.Set();
        }
    }

    // printFizzBuzz() outputs "fizzbuzz".
    public void Fizzbuzz(Action printFizzBuzz) {
        while(this.fbEvent.WaitOne() && this.i <= this.n)
        {
            //System.Console.WriteLine("fizzbuzz");
            printFizzBuzz();
            this.iEvent.Set();
        }
    }

    // printNumber(x) outputs "x", where x is an integer.
    public void Number(Action<int> printNumber) {
        for(i=1;i<=this.n;i++)
        {

            if (i%3==0 && i%5==0)
            {
                this.fbEvent.Set();

                this.iEvent.WaitOne();
            }
            else if(i%3==0)
            {
                this.fEvent.Set();

                this.iEvent.WaitOne();
            }
            else if (i%5==0)
            {
                this.bEvent.Set();

                this.iEvent.WaitOne();
            }
            else
            {
                //System.Console.WriteLine(i);
                printNumber(i);
            }
        }
        this.fbEvent.Set();
        this.fEvent.Set();
        this.bEvent.Set();
    }
}


