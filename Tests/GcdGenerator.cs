namespace Tests;
/// <summary>
/// A class for generating three numbers from multiplication of primes, raised to a random power. The multipliers
/// from gcd_value contains in a_value and b_value, but the other multipliers in the a_value and b_value does not
/// intersect. The class is used for unit testing of the gcd and lcm functions.
/// </summary>
public class GcdGenerator
{
    private int[] primes;
    private int[] values;
    /// <summary>
    ///Returns the greatest common divisor of AValue and BValue
    /// </summary>
    public int GcdValue
    {
        get => this.values[0];
    }
    /// <summary>
    /// Returns the number obtained as a result of multiplying primes raised to a random power. The number has both
    /// the same and different multipliers with b_value
    /// </summary>
    public int AValue
    {
        get => this.values[1] * GcdValue;
    }
    /// <summary>
    /// Returns the number obtained as a result of multiplying primes raised to a random power. The number has both
    /// the same and different multipliers with a_value
    /// </summary>
    public int BValue
    {
        get => this.values[2] * GcdValue;
    }
    /// <summary>
    /// Returns the number obtained as a result of multiplying primes raised to a random power. The number has both
    /// the same and different multipliers with a_value
    /// </summary>
    public int LcmValue
    {
        get => this.values[0] * this.values[1] * this.values[2];
    }
    /// <summary>
    ///Returns the number of primes for the generated values
    /// </summary>
    public int MaxFactorCnt
    {
        get => this.primes.Length;
    }

    public GcdGenerator()
    {
        this.primes = new[] { 2, 3, 5, 7, 11, 13, 17, 19, 23 };
        this.values = new[] { 1, 1, 1 };
    }
    /// <summary>
    /// Generates new values of a, b and gcd
    /// </summary>
    /// <param name="factorCnt">the number of primes for the generated values, must be less or equal than
    /// MaxFactorCnt property. The default value is 5.</param>
    /// <param name="maxPow"></param>
    public void GenerateValues(int factorCnt = 5, int maxPow = 5)
    {
        if (factorCnt > this.primes.Length) factorCnt = this.primes.Length;
        this.values = new[] { 1, 1, 1 };
        Random rnd = new Random();
        int rand_idx;
        int rand_pow;
        for (var i = 0; i < factorCnt; i++)
        {
            rand_idx = rnd.Next(0, this.values.Length);
            rand_pow = rnd.Next(0, maxPow);
            this.values[rand_idx] *= (int)Math.Pow(this.primes[i], rand_pow);
        }
    }
}