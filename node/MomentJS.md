# MomentJS
MomentJS is a javascript library that parses, validates, manipulates, and format dates. 

First, install the moment js library in your project by running this command in your terminal: 

```bash
npm install moment
```

Now, let's create a variable for moment that requires moment package through js file in your project:

```javascript
var moment = require("moment");
```

Note: moment variable will take today's date if not specified and today's date in the following examples is 10/12/2021

First, we can format a date in different formats using format() method:

```javascript
moment().format("MMMM Do YYYY"); // October 12th 2021
moment().format("MM Do YYYY"); // 10 12th 2021
moment().format("MM DD YYYY"); // 10 12 2021
```

Second, we can find out how many years ago was a particular date from today using fromNow() method:

```javascript
moment("20161031", "YYYYMMDD").fromNow(); // 5 years ago
moment("20181031", "YYYYMMDD").fromNow(); // 3 years ago
moment("20111031", "YYYYMMDD").fromNow(); // 10 years ago
```

Finally, we can also subtract days from today's date and output the subtracted date:

```javascript
moment().subtract(10, "days").calendar(); // 10/02/2021
moment().subtract(12, "days").calendar(); // 09/30/2021
moment().subtract(30, "days").calendar(); // 09/12/2021
```

I hope this quick little tutorial was fun. Now you can use moment js package in your upcoming projects!
