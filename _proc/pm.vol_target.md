---
output-file: pm.vol_target.html
title: Portfolio mananger

---



<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

Like a "human" portfolio mananger the job of this code is to take in predictions and output target positions. This particular PM allocates using vanilla volatility targeting ideas. 

---

[source](https://github.com/silvaac/backtest_sample/blob/main/backtest_sample/pm/vol_target.py#L11){target="_blank" style="float:right; font-size:smaller"}

### vol_target

>      vol_target (data, param)

*Initialize self.  See help(type(self)) for accurate signature.*


## Example

::: {.cell}
``` {.python .cell-code}
# Get data
from backtest_sample.data_interface import get_data
import_module = get_data()
df = import_module('BTC-USD').sim_data()
```

::: {.cell-output .cell-output-stderr}
```
[*********************100%***********************]  1 of 1 completed
```
:::
:::


::: {.cell}
``` {.python .cell-code}
prm = {}
prm['target_vol'] = 0.005
prm['AUM'] = 10e6
vt = vol_target(df.values,prm).allocation(1,0.04)
print(vt)
```

::: {.cell-output .cell-output-stdout}
```
{'N': 20}
{'N': 20}
```
:::
:::


