[![Build Status](https://travis-ci.com/karolow/geocoder.svg?branch=main)](https://travis-ci.com/karolow/geocoder)
[![codecov](https://codecov.io/gh/karolow/geocoder/branch/main/graph/badge.svg?token=L7hjNvXOcg)](https://codecov.io/gh/karolow/geocoder)

# geocoder

A Python package to batch geocode address points in Katowice area.

Although there are many geocoding services available online, most of them are either paid or do not return correct results for less popular locations such as Katowice, Poland. Moreover, geocoding thousands of points can be significantly slow.

geocoder is based on regularly updated data from state registers and allows for mass geocoding of tens of thousands of addresses in seconds.

### Details

Under the hood, geocoder performs address matching in several steps: first, addresses are unified (via capitalization, prefix elimination etc.), then mapped directly to coordinates. In case of misspellings or ambiguity, e.g. `Jordana 12` --> `Henryka Jordana 12`, geocoder applies approximate string matching via the [fuzzyset package](https://github.com/axiak/fuzzyset).

### Features

* batch geocode address points in Katowice
* account for misspellings and differences in address wording with approximate string matching
* keep the address database up-to-date with weekly updates

### Installation

Download the package:

```shell
git clone https://github.com/karolow/geocoder.git
cd geocoder
```

and install it locally using pip:

```
pip install -e .
```

### Usage

geocoder can be used right away from command line, `input_file.csv` must include addresses that you want to geocode, there are two options available:

1. Address is stored in one CSV column.

```shell
geocoder input_file.csv output_file.csv
```

```csv
city,address
Katowice,1 Maja 26
Katowice,Adama Mickiewicza 20
Katowice,Aleja Roździeńskiego 98
Katowice,,
```

2. Address is stored in two columns.

```shell
geocoder --cols street_col_name number_col_name input_file.csv output_file.csv
```

```csv
address_city,street,number
Katowice,1 Maja,26
Katowice,Adama Mickiewicza,20
Katowice,Aleja Roździeńskiego,98
Katowice,,
```

The output file consists of four values: `original_address`, `found_address`, `lat`, `lon`. To review the mapping process, compare `original_address` with the best match in the `found_address` column.

```shell
original_address,match,coordinates
1 Maja 26,1 Maja 26,"('502895.4966', '265640.7773')"
Adama Mickiewicza 20,Adama Mickiewicza 20,"('501340.6193', '265963.528999999')"
Aleja Roździeńskiego 98,Aleja Walentego Roździeńskiego 98,"('502918.857', '265983.025900001')"
,,Missing or wrong address – no match found
```

Use --help to learn more.

```shell
geocoder --help
```
