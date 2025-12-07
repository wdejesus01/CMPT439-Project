
# Table of Contents

1.  [Implementation Details](#org8bb6d1c)
    1.  [Front Page](#org917287f)
        1.  [Matrix](#org8022e61)
        2.  [Buttons](#org625fe05)
        3.  [Options](#org38eecdf)

-   System should be able to solve systems of $n$ linear algebraic equations with
    $n$ unknowns
-   System should utilize (with approximate MAE and RMSE and true MAE and RMSE
    stopping criteria)
    -   Gauss-Seidel iterative method
    -   Jacobi iterative method
-   User should be able to:
    -   Enter an augmented matrix of a system or load it from a text file
    -   Choose between previously mentioned methods
    -   Choose a stopping criterion for said methods
    -   Enter a threshold parameter for said stopping criterion
    -   Choose a starting approximation for method or default
        to system default
-   Output should include:
    -   The approximated roots of the system or that they could not be found
        -   Throw warning if 
            -   system is not diagonally dominant
    -   True mean absolute error


<a id="org8bb6d1c"></a>

# Implementation Details

-   **Programming Language:** Python
-   **GUI Framework:** tkinter


<a id="org917287f"></a>

## Front Page


<a id="org8022e61"></a>

### Matrix

-   Displays input for n x n + 1 matrix
    -   n is a persistent option the user can change
        in the options page
    -   The n + 1 column representing the constants to be solved for
    -   The n x n matrix representing the coefficient matrix


<a id="org625fe05"></a>

### Buttons

-   Display a option button that takes you to the option
    page where you can change options for solving
-   Display a solving button that when all matrix inputs
    are entered will attempt to solve for given inputs
-   Display a file button that will request a csv file from the user

1.  File

    -   Open's file navigation application for OS for GUI selection
    -   File should be csved formatted file whose columns are no greater
        than n + 1
        -   Exception may be handled as [solve](#org6159255) usage or time of reading
            file
    -   Stores contents into corresponding matrix and proceed to solve
        matrix

2.  Options

    -   Opens menu to with input fields to enter values for
        respective option
    -   Save button to store new values into [variables](#org38eecdf)
    -   Back button to go back to [main page](#org917287f)

3.  Solve

    -   Takes matrix from either user entered [matrix](#org8022e61) or [file](#org5edb308)
        and appropriate [options](#org38eecdf) as arguments for respective [method](#org22a4a3a)
    -   Return solution vector and error to be displayed either back
        on main [main page](#org917287f) or in a new window


<a id="org38eecdf"></a>

### Options

1.  Method

    -   Function corresponding to either Jacobi or Gauss-Seidel
        function as defined in your code
    -   Your function parameters names should be in the following convention 
        
            #Coefficient matrix, constant vector, initial approximations, error method, threshold 
            def func_nam(coe_matrix, c_vec, init_aprox, error, threshold):

2.  Threshold

    -   A floating point variable to which the result of the [error](#orgc23e446) 
        method will be compared to determine termination of [method](#org22a4a3a)

3.  Size

    -   A integer that determines the dimensions of the square
        coefficient [matrix](#org8022e61)

4.  Starting Approximation

    -   A list of floating point values who's size corresponds to the [size](#org80f6be9) of the
        square coefficient matrix
    -   Defaults to all ones unless user provides alternative

5.  Error Method

    -   The method by which the error is calculated
    -   A enumeration where
        -   Approximate mean absolute error(MAE) = 0
        -   Approximate root mean square error(RMSE) = 1
        -   True mean absolute error(MAE) = 2
        -   True root mean square error(RMSE) = 3
    -   You will have to define a case match in your own code
        for each integer value and the usage of the corresponding
        error method

