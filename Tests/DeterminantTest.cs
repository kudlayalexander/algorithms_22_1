using Algorithms;

namespace Tests;

public class DeterminantTest
{
    [Fact]
    public void TestEmptyMatrix()
    {
        Assert.Throws<ArgumentException>(() => Determinant.GetDeterminant(new int[0,0]));
    }
    
    [Fact]
    public void TestRectangleMatrix()
    {
        int[,] matrix = new int[1, 2] { { 1, 1 } };
        Assert.Throws<ArgumentException>(() => Determinant.GetDeterminant(matrix));
    }

    [Fact]
    public void TestFirstOrder()
    {
        int[,] matrix = new int[1, 1] { { 1 } };
        Assert.Equal(1, Determinant.GetDeterminant(matrix));
    }
    
    [Fact]
    public void TestSecondOrder()
    {
        int[,] matrix = new int[2, 2]
        {
            { 1, 2 }, 
            { 3, 4 }
        };
        Assert.Equal(-2, Determinant.GetDeterminant(matrix));
    }
    
    [Fact]
    public void TestThirdOrder()
    {
        int[,] matrix = new int[3, 3]
        {
            { 1, -2, 3 }, 
            { -4, 5, -6 },
            { 7, -8, 9 }
        };
        Assert.Equal(0, Determinant.GetDeterminant(matrix));
    }
    
    [Fact]
    public void TestFourthOrder()
    {
        int[,] matrix = new int[4, 4]
        {
            { 3, -3, -5, 8 }, 
            { -3, 2, 4, -6 },
            { 2, -5, -7, 5 },
            { -4, 3, 5, -6 }
        };
        Assert.Equal(18, Determinant.GetDeterminant(matrix));
    }
}