# Mean, Median, Mode & Range Calculator
Welcome to a very simple script that I whipped up during class because manually figuring out mean, median, mode & range was driving me insane. It is a very simple project mostly relying on the [statistics library](https://docs.python.org/3/library/statistics.html "statistics library") for the calculations. And uses [Colorama](https://github.com/tartley/colorama "Colorama") to make everything look pretty.

## Setting up
Due to this being very basic to setup just do the following

- Make sure to have the latest verion of python installed
- Install [Colorama](https://github.com/tartley/colorama)
- Run the python file like you normally would
- Have a cup of tea

## Making it work on Linux & Mac
Now I got no clue if this works at all on Linux & Mac, but it should. With one small script change. 

on line **11** you will find this small bit of code. All it does is clear the console to make it look nicer
```python
os.system("cls")
```

But apparently cls dosen't work on Mac & Linux, so to make it work you can either delete that line or swap **cls** with  **clear** like so.
```python
os.system("clear")
```


### But why?
I dunno, but enjoy. or judge tf out if it I don't care.
