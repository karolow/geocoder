# geocoder

A Python package to batch geocode address points in Katowice area.

Although there are many geocoding services available online, most of them are either paid or do not return correct results for less popular locations such as Katowice, Poland. Moreover, geocoding thousands of points can be significantly slow.

geocoder is based on regularly updated data from state registers and allows for mass geocoding of tens of thousands of addresses in seconds.

### Details

Under the hood geocoder performs address matching in several steps: first, addresses are unified (via capitalization, prefix elimination etc.) and mapped directly to coordinates. In case of ambiguity, e.g. `Jordana 12` --> `Henryka Jordana 12`, geocoder uses cosine similarity via the [fuzzyset package](https://github.com/axiak/fuzzyset).

### Features

* batch geocode address points in Katowice
* keep the address database up-to-date by checking for daily updates

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

geocoder can be used right away from command line:

```shell
geocoder input_file.csv output_file.csv
```

`input_file.csv` must include addresses that you want to geocode, there are two options available:
1. Make sure the column name is `address`, e.g. Jordana 12.
2. Or store addresses in two separate columns: `street` & `number`.

```csv
city,street,number
Katowice,Armii Krajowej,102
Katowice,Jordana,20
```

The output file consists of four values: `original_address`, `found_address`, `lat`, `lon`. To review the mapping process, compare `original_address` with the best match in the `found_address` column.

Use --help to learn more.

```shell
geocoder --help
```
