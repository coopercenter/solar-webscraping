"""Package Loading"""

"""General"""
import time
import pandas as pd
import dateutil
from datetime import datetime
from dateparser.search import search_dates
from selenium import webdriver
from selenium.webdriver.common.by import By  
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import smtplib
#import dotenv
import os
import ssl
#import win32com.client
from PyPDF2 import PdfReader
import tempfile

"""Firefox Options"""
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager