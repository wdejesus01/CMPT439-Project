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

