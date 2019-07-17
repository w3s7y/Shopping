# A Shopping List Application (Django)

This project is a little django rest backend and django frontend I'm using to explore the concepts and design principals of 
the Django and Django rest frameworks.

The project can be summarised as an application that can be used to provide a platform for virtual shopping lists 
that are updated as you shop: 

General functionality might include
* Create shopping lists, add products to them etc.
* Have favorites
* Create Offers when you see a shop has an offer on a certain product. 
* barcode data lookups
* using smartphone camera, scan barcodes in store as you shop
* auto removes (updates) shopping list with items scanned and added to trolley/basket
* leaves items in not scanned, so you don't miss vitals

additional:
-pre shop data update - provide info on the cheapest place to shop using online shopping channels for that specific shopping list


## API
This django app contains the base models and API portion of the solution. 

## WEB 
*in development*

## Installation and setup for local development

### Pre-req software
* Docker
* Docker Compose
* python 3.7 & pipenv

### Setup
Clone this repo then in the root of the cloned project run.
* `pipenv --three` Sets up a virtualenv using python3
* `pipenv sync --dev` Installs python deps.
* `cd misc; docker-compose up -d; cd -` Start DB in docker
* `pipenv shell` Starts a shell where you can run the server

