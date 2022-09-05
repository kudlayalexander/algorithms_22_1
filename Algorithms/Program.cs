namespace Algorithms
{
    public static class Program
    {
        /// <summary>
        /// Calculates the greatest common divisor of two numbers
        /// </summary>
        /// <param name="a">first number</param>
        /// <param name="b">second number</param>
        /// <returns>greatest common divisor</returns>
        public static Int64 GcdRecursive(Int64 a, Int64 b)
        {
            throw new NotImplementedException();
        }
        /// <summary>
        /// Calculates the greatest common divisor of two numbers
        /// </summary>
        /// <param name="a">first number</param>
        /// <param name="b">second number</param>
        /// <returns>greatest common divisor</returns>
        public static Int64 GcdIterativeSlow(Int64 a, Int64 b)
        {
            throw new NotImplementedException();
        }
        /// <summary>
        /// Calculates the greatest common divisor of two numbers
        /// </summary>
        /// <param name="a">first number</param>
        /// <param name="b">second number</param>
        /// <returns>greatest common divisor</returns>
        public static Int64 GcdIterativeFast(Int64 a, Int64 b)
        {
            throw new NotImplementedException();
        }
        /// <summary>
        /// Calculates the least common multiple of two numbers
        /// </summary>
        /// <param name="a">first number</param>
        /// <param name="b">second number</param>
        /// <returns>least common multiple</returns>
        public static Int64 Lcm(Int64 a, Int64 b)
        {
            throw new NotImplementedException();
        }
        
        public static void Main(string[] args)
        {
            Console.WriteLine($"a = 9\nb = 3\ngcd(a, b) = {GcdIterativeFast(9, 3)}");
            Console.WriteLine($"a = 6\nb = 8\nlcm(a, b) = {Lcm(6, 8)}");
        }
    }
}