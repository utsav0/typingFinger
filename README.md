
# TypingFinger

TypingFinger is a a tool for tech geeks to speed up their 10-finger typing without internet.
This tool is build on vanilla JavaScript and django (a python framework)

TypingFinger basically let you practice and analyze your typing speed.

Initially it is built using vanilla JavaScript but I'm planning to convert it into a ReactJs app.
## Getting Started

These instructions will give you a copy of the project up and running on
your local machine for development and testing purposes. See deployment
for notes on deploying the project on a live system.

### Prerequisites

Requirements for the software and other tools to build, test and push 
- [Django](https://www.djangoproject.com/download/)
- [MySQL](https://dev.mysql.com/downloads/installer/)
- [Python](https://www.python.org/downloads/)

### Installing

Firstly, clone this repo in your local repo using the following command:

    git clone git@github.com:utsav0/typingFinger.git

After cloning this, cd into the typing finger folder by the following command:

    cd .\typingFinger\
    
Then start the django server with the following command:
    
    python manage.py runserver

So, now the app is up and running. So, go to the following address in any browser:
    
    127.0.0.1:8000
    
Now you can simply signup or login and start practicing.

## Additional Required Steps

You also have to setup your mysql database and create a new database there.

For that, install the mysql workbench, open and login in it.

Then run the following command in that terminal:
    
    create database typingfingerdb;
 
After that:
 
    use typingfingerdb;
    
Then create a new table named "usertable":

    create table usertable(mail varchar(50), password varchar(30));
    
Now the last step is to go to views.py file and change the dbPassword variable equal to your password.
like, if your password is "12345", then make it like:

    dbPassword = "12345"


## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code
of conduct, and the process for submitting pull requests to us.


## Authors

  - **Utsav Meena** - *Maintainer of this repo*

See also the list of
[contributors](https://github.com/utsav0/typingFinger/graphs/contributors)
who participated in this project.

## License

This project is licensed under the [MIT](LICENSE)
Creative Commons License - see the [LICENSE](LICENSE) folder for
details

## Acknowledgments

  - Django documentation
  - CodwWithHarry YouTube channel
  - A little inspiratin from [monkeytype.com](http://monkeytype.com)
