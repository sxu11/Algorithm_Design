using System.Threading;
using System;

public class H2O {

    private object m_lock;
    private int O_Cnt;
    private int H_Cnt;

    public H2O() {
        m_lock = new object();
        O_Cnt = 0;
        H_Cnt = 0;
    }

    public void Hydrogen(Action releaseHydrogen) {

        // releaseHydrogen() outputs "H". Do not change or remove this line.

        // when can start:
        //   - count is right

        Monitor.Enter(m_lock);
        while (H_Cnt==2)
        {
            Monitor.Wait(m_lock);
        }

        // now start

        releaseHydrogen();
        System.Console.WriteLine("release H");
        H_Cnt += 1;

        if (H_Cnt==2 && O_Cnt==1)
        {
            H_Cnt = 0;
            O_Cnt = 0;
            Monitor.PulseAll(m_lock);
        }

        Monitor.Exit(m_lock);
    }

    public void Oxygen(Action releaseOxygen) {

        // releaseOxygen() outputs "O". Do not change or remove this line.
        Monitor.Enter(m_lock);
        while (O_Cnt==1)
        {
            Monitor.Wait(m_lock);
        }

        // now start

        releaseOxygen();
        System.Console.WriteLine("release O");
        O_Cnt += 1;

        if (H_Cnt==2 && O_Cnt==1)
        {
            H_Cnt = 0;
            O_Cnt = 0;
            Monitor.PulseAll(m_lock);
        }

        Monitor.Exit(m_lock);

    }
}