Dirble-Wrapper
--------------
This is a projekt of my sparetime, if more documentation is needed, feel free to open a issue.

HowTo
-----

```python
from dirble_wrapper import DirbleWrapper
dw = DirbleWrapper("your api key")
stations = dw.get_all_stations()
stations = dw.get_popular_stations()
stations = dw.get_recent_added_stations()
station = dw.get_specific_station(10)
stations = dw.search_stations("Antenne Bayern")
```

Install
-------
```bash
pip install Dirble-Wrapper
```

License
------
MIT
