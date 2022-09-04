using Algorithms;

namespace Tests;

internal delegate int Gcd(int a, int b);

public class GcdTest
{
    private readonly Gcd _gcd = new Gcd(Program.GcdRecursive) + new Gcd(Program.GcdIterativeFast) 
                                                              + new Gcd(Program.GcdIterativeSlow);
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
    public void TestRandom()
    {
        GcdGenerator generator = new GcdGenerator();
        for (var i = 0; i < 10; i++)
        {
            generator.GenerateValues();
            Assert.Equal(generator.GcdValue, _gcd(generator.AValue, generator.BValue));
        }
    }
}