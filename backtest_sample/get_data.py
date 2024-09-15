# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/data_interface.ipynb.

# %% auto 0
__all__ = ['get_data']

# %% ../nbs/data_interface.ipynb 4
import importlib
import os

# %% ../nbs/data_interface.ipynb 5
def get_data(source="yahoo"):
    """
    Dynamically import a class from a file.
    
    Parameters:
    - source: The name of the class within data (and the file without .py extension).
    Note the convention: class and file name are equal
    
    Returns:
    - Ouput the class.
    """
    # Construct the module name from the folder path and class name
    module_name = f"backtest_sample.data.{source}"
    
    try:
        # Dynamically import the module
        module = importlib.import_module(module_name)
        
        # Get the class from the module
        cls = getattr(module, source)
        
        # Create an instance of the class
        #instance = cls()
        
        # Call the output method and return the result
        return cls
    except ModuleNotFoundError:
        raise ValueError(f"Module '{module_name}' not found.")
    except AttributeError:
        raise ValueError(f"Class '{class_name}' not found in module '{module_name}'.")



