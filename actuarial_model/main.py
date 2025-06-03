import pandas as pd
from dataclasses import dataclass

# Constants
OMEGA = 110
SEMANAS_500 = 0.45
INCREMENTO_PORCENTAJE = 0.02
INCREMENTO_REF = 50

# Global variables
calcul_date = None
SMLV = 0.0
flag_initialize = False

@dataclass
class TablasMortalidad:
    mort_f: pd.DataFrame = None
    mort_m: pd.DataFrame = None
    mort_f_inv: pd.DataFrame = None
    mort_m_inv: pd.DataFrame = None

mort_table = TablasMortalidad()

def read_mortality(file_path: str) -> None:
    """Reads mortality tables from an Excel file with named ranges or sheets."""
    global mort_table
    xls = pd.ExcelFile(file_path)
    
    mort_table.mort_f = pd.read_excel(xls, sheet_name="mort_f")
    mort_table.mort_m = pd.read_excel(xls, sheet_name="mort_m")
    mort_table.mort_f_inv = pd.read_excel(xls, sheet_name="mort_f_inv")
    mort_table.mort_m_inv = pd.read_excel(xls, sheet_name="mort_m_inv")

def initialize(file_path: str) -> None:
    """Initializes the mortality data and sets the flag."""
    global flag_initialize
    read_mortality(file_path)
    flag_initialize = True
