
# Table of Contents

1.  [Implementation Details](#org92349d1)
    1.  [Front Page](#org323855f)
        1.  [Matrix](#orga0f62b2)
        2.  [Buttons](#org67c3976)
        3.  [Options](#orgd78ea12)

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


<a id="org92349d1"></a>

# Implementation Details

-   **Programming Language:** Python
-   **GUI Framework:** tkinter


<a id="org323855f"></a>

## Front Page


<a id="orga0f62b2"></a>

### Matrix

-   Displays input for n x n + 1 matrix
    -   n is a persistent option the user can change
        in the options page
    -   The n + 1 column representing the constants to be solved for
    -   The n x n matrix representing the coefficient matrix


<a id="org67c3976"></a>

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
        -   Exception may be handled as [solve](#org33e95b4) usage or time of reading
            file
    -   Stores contents into corresponding matrix and proceed to solve
        matrix

2.  Options

    -   Opens menu to with input fields to enter values for
        respective option
    -   Save button to store new values into [variables](#orgd78ea12)
    -   Back button to go back to [main page](#org323855f)

3.  Solve

    -   Takes matrix from either user entered [matrix](#orga0f62b2) or [file](#org177a410)
        and appropriate [options](#orgd78ea12) as arguments for respective [method](#orgae7974f)
    -   Return solution vector and error to be displayed either back
        on main [main page](#org323855f) or in a new window


<a id="orgd78ea12"></a>

### Options

1.  Method

    -   Function corresponding to either Jacobi or Gauss-Seidel
        function as defined in your code
        -   Your function parameters should be in the following order
            if you want your code to function by default else you will
            have to alter some things:
            1.  Matrix
            2.  Threshold
            3.  Stopping Criteria

2.  Error

    -   Either a function, string or integer that will determine the
        function to calculate error for a value gotten as a result of
        [method](#orgae7974f)

3.  Threshold

    -   A floating point variable to which the result of the [error](#org52f8cf0) 
        method will be compared to determine termination of [method](#orgae7974f)

4.  Size

    -   A integer that determines the dimensions of [matrix](#orga0f62b2)

5.  Starting Approximation

    -   A vector of size n initialized at index $n_i$ to some floating
        point number
        -   where n is the [size](#orgbefd6c4)

