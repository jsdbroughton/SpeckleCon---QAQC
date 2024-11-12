"""
This main entry point is the command line interface for the Speckle Automate function.
"""

from speckle_automate import (
    execute_automate_function,
)

import Exercises.exercise_0.inputs.FunctionInputs as FunctionInputs
import Exercises.exercise_0.function.automate_function as automate_function

# make sure to call the function with the executor
# Pass in the function reference with the inputs schema to the executor.
# If the function has no arguments, the executor can handle it like so
# execute_automate_function(automate_function_without_inputs)
if __name__ == "__main__":
    execute_automate_function(automate_function, FunctionInputs)
