# geocoder

A Python package to batch geocode address points in the city of Katowice.

Although there are many geocoding services available online, most of them are either paid or do not return correct results for less popular locations such as Katowice, Poland. Moreover, geocoding thousands of points can be significantly slow.

geocoder is based on regularly updated data from state registers and allows for mass geocoding of tens of thousands of addresses in seconds.

The next version of the tool will allow for geocoding addresses from all over Poland.

### Features

* batch geocode address points in Katowice
* keep the address database up-to-date by checking for daily updates

### Installation

Download the package:

```
git clone https://github.com/karolow/geocoder.git
cd geocoder
```

and install it locally using pip:

```
pip install -e .
```

### Usage

```python
from geocoder.geocoding import
from geocoder.preprocessing import
```
