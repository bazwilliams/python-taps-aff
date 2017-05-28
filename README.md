# Taps Aff Python Api

This provides a simple python library to determine if it is 'taps aff' or 'taps oan' for a specified location using Colin Waddell's www.taps-aff.co.uk service.

https://github.com/ColinWaddell/tapsaff

## Installation

```bash
pip install tapsaff
```

## API

### Constructor

`location` can be a UK postcode or city. 

```python
TapsAff(location)
```

### Methods

```python
is_taps_aff() # Returns True if taps aff for this location
```

## Example

```python
from tapsaff import TapsAff

glasgow = TapsAff("Glasgow")
print(glasgow.is_taps_aff())
```