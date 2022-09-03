namespace Algorithms
{
    public static class Program
    {
        public static void Main(string[] args)
        {
            Console.WriteLine("Fibonacci numbers:");
            for (var i = 1; i < 10; i++)
            {
                Console.WriteLine($"{i}: {Fibonacci.FibonacciRec(i)}");
            }
            int[,] matrix = new int[3, 3]
            {
                { 1, -2, 3 }, 
                { -4, 5, -6 },
                { 7, -8, 9 }
            };
            Console.WriteLine("\ninteger square matrix:\n1, -2, 3\n-4, 5, -6\n7, -8, 9");
            Console.WriteLine($"matrix determinant: {Determinant.GetDeterminant(matrix)}");
        }
    }
}