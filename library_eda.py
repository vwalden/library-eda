{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "bd613e67",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Dependencies & setup\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import scipy.stats as st\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "9aa38258",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Raw data files\n",
    "fy17state_path = \"data/PLS_FY17_State_pud17i.csv\"\n",
    "fy18state_path = \"data/pls_fy18_state_pud18i.csv\"\n",
    "fy19state_path = \"data/pls_state_pud19i.csv\"\n",
    "fy20state_path = \"data/PLS_FY20_State_pud20i.csv\"\n",
    "\n",
    "# Read data\n",
    "fy17state_raw_df = pd.read_csv(fy17state_path)\n",
    "fy18state_raw_df = pd.read_csv(fy18state_path)\n",
    "fy19state_raw_df = pd.read_csv(fy19state_path)\n",
    "fy20state_raw_df = pd.read_csv(fy20state_path)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "0879cb85",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Slice state data\n",
    "fy17state_df = pd.DataFrame().assign(STABR=fy17state_raw_df['STABR'],\n",
    "                      STARTDAT=fy17state_raw_df['STARTDAT'], \n",
    "                      ENDDATE=fy17state_raw_df['ENDDATE'], \n",
    "                      POPU_LSA=fy17state_raw_df['POPU_LSA'], \n",
    "                      OBEREG=fy17state_raw_df['OBEREG'],\n",
    "                      TOTOPEXP=fy17state_raw_df['TOTOPEXP'], \n",
    "                      TOTINCM=fy17state_raw_df['TOTINCM'], \n",
    "                      PRMATEXP=fy17state_raw_df['PRMATEXP'], \n",
    "                      ELMATEXP=fy17state_raw_df['ELMATEXP'], \n",
    "                      OTHMATEX=fy17state_raw_df['OTHMATEX'], \n",
    "                      TOTEXPCO=fy17state_raw_df['TOTEXPCO'],                    \n",
    "                      TOTPRO=fy17state_raw_df['TOTPRO'], \n",
    "                      TOTATTEN=fy17state_raw_df['TOTATTEN'],\n",
    "                      VISITS=fy17state_raw_df['VISITS'], \n",
    "                      TOTCIR=fy17state_raw_df['TOTCIR'],\n",
    "                      ELMATCIR=fy17state_raw_df['ELMATCIR'], \n",
    "                      REGBOR=fy17state_raw_df['REGBOR'], \n",
    "                      ELCONT=fy17state_raw_df['ELCONT'])\n",
    "\n",
    "fy18state_df = pd.DataFrame().assign(STABR=fy18state_raw_df['STABR'],\n",
    "                      STARTDAT=fy18state_raw_df['STARTDAT'], \n",
    "                      ENDDATE=fy18state_raw_df['ENDDATE'], \n",
    "                      POPU_LSA=fy18state_raw_df['POPU_LSA'], \n",
    "                      OBEREG=fy18state_raw_df['OBEREG'],\n",
    "                      TOTOPEXP=fy18state_raw_df['TOTOPEXP'], \n",
    "                      TOTINCM=fy18state_raw_df['TOTINCM'], \n",
    "                      PRMATEXP=fy18state_raw_df['PRMATEXP'], \n",
    "                      ELMATEXP=fy18state_raw_df['ELMATEXP'], \n",
    "                      OTHMATEX=fy18state_raw_df['OTHMATEX'], \n",
    "                      TOTEXPCO=fy18state_raw_df['TOTEXPCO'],                    \n",
    "                      TOTPRO=fy18state_raw_df['TOTPRO'], \n",
    "                      TOTATTEN=fy18state_raw_df['TOTATTEN'],\n",
    "                      VISITS=fy18state_raw_df['VISITS'], \n",
    "                      TOTCIR=fy18state_raw_df['TOTCIR'],\n",
    "                      ELMATCIR=fy18state_raw_df['ELMATCIR'], \n",
    "                      REGBOR=fy18state_raw_df['REGBOR'], \n",
    "                      ELCONT=fy18state_raw_df['ELCONT'])\n",
    "\n",
    "fy19state_df = pd.DataFrame().assign(STABR=fy19state_raw_df['STABR'],\n",
    "                      STARTDAT=fy19state_raw_df['STARTDAT'], \n",
    "                      ENDDATE=fy19state_raw_df['ENDDATE'], \n",
    "                      POPU_LSA=fy19state_raw_df['POPU_LSA'], \n",
    "                      OBEREG=fy19state_raw_df['OBEREG'],\n",
    "                      TOTOPEXP=fy19state_raw_df['TOTOPEXP'], \n",
    "                      TOTINCM=fy19state_raw_df['TOTINCM'], \n",
    "                      PRMATEXP=fy19state_raw_df['PRMATEXP'], \n",
    "                      ELMATEXP=fy19state_raw_df['ELMATEXP'], \n",
    "                      OTHMATEX=fy19state_raw_df['OTHMATEX'], \n",
    "                      TOTEXPCO=fy19state_raw_df['TOTEXPCO'],                    \n",
    "                      TOTPRO=fy19state_raw_df['TOTPRO'], \n",
    "                      TOTATTEN=fy19state_raw_df['TOTATTEN'],\n",
    "                      VISITS=fy19state_raw_df['VISITS'], \n",
    "                      TOTCIR=fy19state_raw_df['TOTCIR'],\n",
    "                      ELMATCIR=fy19state_raw_df['ELMATCIR'], \n",
    "                      REGBOR=fy19state_raw_df['REGBOR'], \n",
    "                      ELCONT=fy19state_raw_df['ELCONT'])\n",
    "\n",
    "fy20state_df = pd.DataFrame().assign(STABR=fy20state_raw_df['STABR'],\n",
    "                      STARTDAT=fy20state_raw_df['STARTDAT'], \n",
    "                      ENDDATE=fy20state_raw_df['ENDDATE'], \n",
    "                      POPU_LSA=fy20state_raw_df['POPU_LSA'], \n",
    "                      OBEREG=fy20state_raw_df['OBEREG'],\n",
    "                      TOTOPEXP=fy20state_raw_df['TOTOPEXP'], \n",
    "                      TOTINCM=fy20state_raw_df['TOTINCM'], \n",
    "                      PRMATEXP=fy20state_raw_df['PRMATEXP'], \n",
    "                      ELMATEXP=fy20state_raw_df['ELMATEXP'], \n",
    "                      OTHMATEX=fy20state_raw_df['OTHMATEX'], \n",
    "                      TOTEXPCO=fy20state_raw_df['TOTEXPCO'],                    \n",
    "                      TOTPRO=fy20state_raw_df['TOTPRO'], \n",
    "                      TOTATTEN=fy20state_raw_df['TOTATTEN'],\n",
    "                      VISITS=fy20state_raw_df['VISITS'], \n",
    "                      TOTCIR=fy20state_raw_df['TOTCIR'],\n",
    "                      ELMATCIR=fy20state_raw_df['ELMATCIR'], \n",
    "                      REGBOR=fy20state_raw_df['REGBOR'], \n",
    "                      ELCONT=fy20state_raw_df['ELCONT'])"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.15"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
