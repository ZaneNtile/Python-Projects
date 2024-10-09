
#Function with 3 arguments: target, tolerance, max-tries
def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):

    #Condition 1: target is NOT REAL
    if square_target < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    
    #Condition 2: target equals 1
    if square_target == 1:
        root = 1
        print(f'The square root of {square_target} is 1')

    #Condition 3: target equals 0
    elif square_target == 0:
        root = 0
        print(f'The square root of {square_target} is 0')

    #Condition 4: Apply bisection
    else:
        #Variables for bisection method
        low = 0
        high = max(1, square_target)
        root = None
        
        #For loop for max interation=100
        for _ in range(max_iterations):
            mid = (low + high) / 2
            square_mid = mid**2

            #Use absolute to check if the condition is below tolerance
            if abs(square_mid - square_target) < tolerance:
                root = mid
                break

            #Condition of square_mid < square_target
            elif square_mid < square_target:
                low = mid

            else:
                high = mid

        #If loop for remaining condition
        if root is None:
            print(f"Failed to converge within {max_iterations} iterations.")
    
        else:   
            print(f'The square root of {square_target} is approximately {root}')
    
    return root

N = 16
square_root_bisection(N)