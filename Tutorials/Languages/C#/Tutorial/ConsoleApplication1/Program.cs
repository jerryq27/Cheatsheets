using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication1
{
    class Program
    {
        static void Main(string[] args)
        {
            int intExample = int.MaxValue;
            long longExample = (long)intExample; // Ok

            Console.WriteLine(intExample + "\n" + longExample);

            longExample = long.MaxValue;
            intExample = (int)longExample; // -1
            Console.WriteLine(intExample + "\n" + longExample);
        }
    }
}
