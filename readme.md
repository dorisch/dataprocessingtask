# Data Processing Task
## 1. How to run script
```sh
python main.py yourfile.json
```
## 2. Supported formats
### JSON
Example:
```json
[
  {
    "message": "abc",
    "airline_code": "A1",
    "number_of_fellow_passenger": 10,
    "did_receive_compensation": true,
    "total_compensation_amount": 3000
  },
  {
    "message": "def",
    "airline_code": "B2",
    "number_of_fellow_passenger": 5,
    "did_receive_compensation": false,
    "total_compensation_amount": 2000
  }
]
```

### CSV
Example:
```csv
message ,airline_code ,number_of_fellow_passenger,did_receive_compensation ,total_compensation_amount 
abc,A1,10,true,3000
def,B2,5,false,2000
ghi,C3,1,true,1000
jkl,C3,2,true,2500
```
The order of the columns must be as in the example!
## 3. Example output
```
Distribution of number of fellow passengers per user: 4.5
Average compensation per passenger: 472.22222222222223
Most popular airline is: ['C3']
Percentage of users who got compensation: 72.22222222222221
```