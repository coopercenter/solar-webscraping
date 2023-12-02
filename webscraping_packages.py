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
import win32com.client
from PyPDF2 import PdfReader
import tempfile

"""Firefox Options"""
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager