import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def test_login_blank():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/accounts/login")
    
    elemName = driver.find_element_by_name("username")
    elemName.send_keys("")

    elemPassword = driver.find_element_by_name("password")
    elemPassword.send_keys("")

    elemPassword.send_keys(Keys.RETURN)

def test_login_no_password():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/accounts/login")

    elemName = driver.find_element_by_name("username")
    elemName.send_keys("muhdikmal")

    elemPassword = driver.find_element_by_name("password")
    elemPassword.send_keys("")

    elemPassword.send_keys(Keys.RETURN)

def test_login_no_username():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/accounts/login")

    elemName = driver.find_element_by_name("username")
    elemName.send_keys("")

    elemPassword = driver.find_element_by_name("password")
    elemPassword.send_keys("ikmal2000")

    elemPassword.send_keys(Keys.RETURN)

def test_login():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/accounts/login")

    elemName = driver.find_element_by_name("username")
    elemName.send_keys("muhdikmal")

    elemPassword = driver.find_element_by_name("password")
    elemPassword.send_keys("ikmal2000")

    elemPassword.send_keys(Keys.RETURN)
