**Authoritative Server is AS** <br />
**Fibonacci Server is FS**
**User Server is US**

The User will interact with the US to find the fibonacci number at a given index.

The actual fibonacci number is calculated at FS

The AS acts a DNS that maintains the actual IP addresses of the FS as well as the domain names assigned to the IP addresses.

1. The US will query the AS using the domain name provided by the user
2. The AS will return the corresponding IP addr to the US
3. The US will then query the IP addr with the index value provided by the User and the FS will calculate the Fibonacci number at the queried index and return the Fibonacci number to the US
