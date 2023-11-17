# Data Representation
## User-defined (or not, they mixed them with builtin) data types
**Purpose (9618/33/M/J/21)**
- To create a new data type
- To extend the flexibility of the programming language
### Composite
A data type that is derived from other types. Throw in that they used to extend functionality of programming language for good measure (9608/32/O/N/19).
#### Record
A collection of related items that may have different data types (9608/33/M/J/18)

Example (9618/33/M/J/21):
(SchoolDay and WeekEnd are enumerated types created in the previous question)

`
TYPE ClubMeet
    DECLARE FirstName : STRING
    DECLARE LastName : STRING
    DECLARE Schoolday : SchoolDay
    DECLARE Weekend : WeekEnd
ENDTYPE
`

Example with enum and range inside the declaration

`
TYPE MyContactDetail
    DECLARE Name : STRING
    DECLARE Area : (uptown, downtown, midtown)
    DECLARE HouseNumber : 1..499
ENDTYPE
`

#### Class
Data type that has properties and methods for an object (9608/33/M/J/18)
#### Set
Data type that allows storing a finite number of different values that have no order (9608/33/M/J/18)
### Non-composite
A **single** (9608/33/M/J/18) data type that is not composed of multiple other types.
- STRING, REAL, INTEGER etc, are non-composite (9608/33/O/N/20)
#### Enum
A data-type which provides a list of values that a variable of this type can take on.
Example (9618/33/M/J/21):
`TYPE SchoolDay = (Monday, Tuesday, Wednesday, Thursday, Friday)`

#### Pointer
A pointer is a variable that stores the address of a variable of a particular type.

Notice how these people put the ^ before the type and after the variable identifier.
Example (pointer to an INTEGER):
`
DECLARE IntPointer : ^INTEGER
DECLARE MyVar : INTEGER
DECLARE MyVar2 : INTEGER
MyVar <-- 57
// @ symbol before a variable identifier gives the address of the variable
IntPointer <-- @MyVar
// ^ after a pointer variable identifier dereferences the pointer variable
MyVar2 <-- IntPointer^
IntPointer^ <-- 100
`

## File Organisation
### Serial
Description and justification for usage (often the same thing)
- Records stored in chronological order/order they were added in
- New records added to end of file
- Sequential Access only
- Reorganisation not needed when new record added

Good where stuff comes in during the month

### Sequential
- Records ordered according to their key field
- Sequential Access and direct access with an index file
- High hit rate (everyone needs a statement)

Justification:
- Suitable for batch processing
- All customers need statement
- There's a unique key field (e.g. unique account number)
- Organised by unique key field, e.g. account number

Good where you need to produce a statement at the end of the month.

### Random
- Direct Access only (9608/32/M/J/17)
- Low waiting time
- Low hit rate (only one record will match your account number/username)

Justification:
- Real time access
- No need to search records

Good where you see "password" and "username"

#### Storage
(9608/32/M/J/18)
- Key field hashed to produce a location address
- If location is free, add the data there
- Otherwise use an overflow method to find a free location
- If no free location, data cannot be stored

## Floating Point
- If they ask you to convert anything to (normalised) FP and you get a result that doesn't fit, fill in the boxes from left to right.
- The _consequence_ of doing that is the precision is reduced because the least significant bits have been lost.
- If they ask why some binary representations lead to rounding errors, say:
    - No exact conversion to binary for some numbers
    - ...or more bits needed to store number than available
- If they give a specific example of an expression that leads to a rounding error (9608/32/M/J/19):
    - [Expression] cannot be represented exactly in binary
    - [part of expression] represented by value slightly larger/smaller
    - Operations with parts that can't be represented exactly increases inaccuracy
    - Inaccuracy may be significant enough to see

### + Denary to FP
1. Take denary number, convert to normal binary with point.
e.g. 4.5 -> 100.1
2. Then shift the point to match the required format
e.g. 12 bit mantissa, 4 bit exponent
100.1     -->      0(.)10010000000  0011
The point is in brackets because you should only imagine it being there.
We had to shift the point three places to the left (we were dividing by 2 each time) so we would have to make the exponent such that multiplying the mantissa by 2 to the power of the exponent would result in the original number (if we divided by $2^3$, we must multiply by $2^3$ to get back what we started with.)
### Make FP negative
Also do this if they ask convert negative denary to FP. First convert the positive denary to FP, then make the FP negative.
1. Take the mantissa and flip all the bits (1's complement)
e.g. 4.5  →  `0(.)10010000000  0011`
               →  `1(.)01101111111  0011`
2. Add 1 to the mantissa (2's complement)
`1(.)01110000000 0011`
(you have to write both 1's and 2's complement to get full marks)

Shortcut:
Look at mantissa from right to left. Ignore 0's and the first 1. After the first 1, flip all bits. Good for checking answers.

### Precision and Range
Trade-off between range and precision:
- More bits in mantissa → Greater precision
- More bits in exponent → Greater range
…and vice versa

### Normalisation
First and second bits of mantissa must be different for a floating point number to be normalised.

**Reasons for normalisation**
- To store maximum range of numbers with smallest number of bits
- To maximise the precision of the number for the given number of bits
- To prevent multiple representations of the same number
- To minimise the number of leading zeroes/ones.

### Overflow/Underflow
Overflow - number too big to be represented in the given format
Underflow - number too small to be represented in the given format

When they ask why you can't represent some number accurately:
- Requires n bits
- Give the value in binary
- Say overflow/underflow

When they ask how to fix it (overflow specifically, 9618/33/M/J/21):
- Increase number of bits in mantissa
- How many bits mantissa **and** exponent should have (steal some bits from exponent) 
