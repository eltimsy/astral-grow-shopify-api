# Astral Grow Shopify API

The main goal of this project is to integrate shopify data with our excel amazon data.

## How it works

The script will first create a store object with all the products in the excel sheet.
Next it will try to update the excelsheet with shopify data. (WIP)

## Installation

The script is built using python 3.8

- Install requirements from requirements.txt
- Create a secrets folder with a secrets.py fill and add your shopify details to it
    - Things to add: API_KEY, API_PASSWORD, API_VERSION, SHOP_NAME

## How to run

The script currently is run in the terminal with `python api_test.py`
