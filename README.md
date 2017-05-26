# Djangazon!! Bangazon on Django
[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

A django webapp where users can buy and sell products!

## Table of Contents

- [About](#about)
- [Installation](#installation)
- [Usage](#usage)   
- [Contribute](#contribute)
- [Credits](#credits)
- [License](#license)

## About
We are.. The Trashy Armadillos. Agile AF, and Donut Mondays. That's just how we role.
We give you.. Djangazon

### Prerequisites
Install [pip](https://packaging.python.org/installing/)

Install [Python 3.6](https://www.python.org/downloads/)

Install Django and REST framework:
```
pip install django
```

## Installation
```
git clone https://github.com/Trashy-Armadillos/djangazon.git
cd djangazon
```
Setting up the database:

```
./refresh_database.sh
```
Run project in browser:

```
python manage.py runserver
```

Wanna be a superUser of the future. Try this:

```
python manage.py createsuperuser:
url: '/login'
```




## Usage
1. Customer can add a product to sell
2. User Can Complete an Order
3. User can delete product from shopping cart
4. User can delete a payment type
5. User can cancel an order
6. User can select product category when selling product
7. User can view all product categories
8. User can view all products that are of a particular product type
9. User can view product detail
10. User can view latest products on home page
11. User can add a payment type


## Contribute
1. Fork it!
2. Create your feature branch:
```git checkout -b <new-feature-branch-name-here>```
3. Commit your changes:
```git commit -m 'Add some feature'```
4. Push to the branch:
```git push origin <new-feature-branch-name-here-too>```
5. Submit a pull request :D

Small note: If editing the Readme, please conform to the [standard-readme](https://github.com/RichardLitt/standard-readme) specification.

## Credits
Project Manager:
  - Gilberto Diaz

API Build Contributors:
  * [Miriam Rozenbaum](https://github.com/mrozenbaum)
  * [Justin Short](https://github.com/short880)
  * [Casey Daley](https://github.com/caseydailey)
  * [Taylor Perkins](https://github.com/taylorperkins)

## License
[MIT © Trashy Armadillos](./LICENSE)
