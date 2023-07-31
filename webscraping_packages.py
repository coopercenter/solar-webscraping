"""Package Loading"""

"""General"""
import time
import pandas as pd 
import dateutil
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By  
import requests
import smtplib
import dotenv
import os
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

"""Firefox Options"""
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager