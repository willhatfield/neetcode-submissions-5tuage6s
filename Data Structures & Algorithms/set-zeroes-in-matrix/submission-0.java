class Solution {
    public void setZeroes(int[][] matrix) {
        boolean tl = false;
        boolean toprow = false;
        boolean leftcol = false;
        if(matrix[0][0] == 0) tl = true;

        for(int i = 0; i < matrix.length; i++)  {
            if (matrix[i][0] == 0) {
                leftcol = true;
                break;
            } 
        }

        for(int i = 0; i < matrix[0].length; i++)  {
            if (matrix[0][i] == 0) {
                toprow = true;
                break;
            } 
        }

        for(int i = 0; i < matrix.length; i++)  {
            for(int j = 0; j < matrix[0].length; j++)   {
                if(matrix[i][j] == 0)   {
                    matrix[0][j] = 0;
                    matrix[i][0] = 0;
                }
            }
        }

        for(int i = 1; i < matrix.length; i++)  {
            if(matrix[i][0] == 0)   {
                setRowZero(matrix, i);
            }
        }

        for(int j = 1; j < matrix[0].length; j++)  {
            if(matrix[0][j] == 0)   {
                setColZero(matrix, j);
            }
        }

        if(tl)  {
            setRowZero(matrix, 0);
            setColZero(matrix, 0);
        } else  {
            if(toprow)  {
                setRowZero(matrix, 0);
            }

            if(leftcol) {
                setColZero(matrix, 0);
            }
        }
    }

    public void setRowZero(int[][] matrix, int row)   {
        for(int j = 0; j < matrix[row].length; j++) {
            matrix[row][j] = 0;
        }
    }

    public void setColZero(int[][] matrix, int col)   {
        for(int j = 0; j < matrix.length; j++) {
            matrix[j][col] = 0;
        }
    }
}
