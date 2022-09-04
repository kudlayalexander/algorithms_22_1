using Algorithms;

namespace Tests;

public class LcmTest
{
    [Fact]
    public void TestPrimes()
    {
        Assert.Equal(21, Program.Lcm(7, 3));
    }

    [Fact]
    public void TestSimple()
    {
        Assert.Equal(24, Program.Lcm(6, 8));
    }

    [Fact]
    public void TestSimpleLong()
    {
        Assert.Equal(680386354, Program.Lcm(1005002, 1354));
    }

    [Fact]
    public void TestRandom()
    {
        GcdGenerator generator = new GcdGenerator();
        for (var i = 0; i < 10; i++)
        {
            generator.GenerateValues();
            Assert.Equal(generator.LcmValue, Program.Lcm(generator.AValue, generator.BValue));
        }
    }
}