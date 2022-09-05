using Algorithms;

namespace Tests;

internal delegate Int64 Gcd(Int64 a, Int64 b);

public class GcdTest
{
    private readonly Gcd _gcd = new Gcd(Program.GcdRecursive) + new Gcd(Program.GcdIterativeFast) 
                                                              + new Gcd(Program.GcdIterativeSlow);
    private readonly Gcd _gcdSlow = new Gcd(Program.GcdRecursive) + new Gcd(Program.GcdIterativeSlow);
    private readonly Gcd _gcdFast = new Gcd(Program.GcdIterativeFast);
    [Fact]
    public void TestSimple()
    {
        Assert.Equal(3, _gcd(9, 3));
    }
    
    [Fact]
    public void TestSimpleLong()
    {
        Assert.Equal(2, _gcd(1005002, 1354));
    }

    [Fact]
    public void TestRandomFast()
    {
        GcdGenerator generator = new GcdGenerator();
        for (var i = 0; i < 10; i++)
        {
            generator.GenerateValues(5, 3);
            Assert.Equal(generator.GcdValue, _gcdFast(generator.AValue, generator.BValue));
        }
    }

    [Fact]
    public void TestRandomSlow()
    {
        GcdGenerator generator = new GcdGenerator();
        for (var i = 0; i < 10; i++)
        {
            generator.GenerateValues(3, 2);
            Assert.Equal(generator.GcdValue, _gcdSlow(generator.AValue, generator.BValue));
        }
    }
}