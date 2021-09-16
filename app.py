from flask import Flask, render_template, request
import uuid
import requests
from flask import Flask, render_template, session, request, redirect, url_for
from flask_session import Session  # https://pythonhosted.org/Flask-Session
import msal




from flask import Flask, render_template, request
from flask import Flask, jsonify, request, render_template
import socket, os, json, sys
import requests
import random, os
from azure.common.client_factory import get_client_from_cli_profile
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.web import WebSiteManagementClient
import subprocess
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import mysql
import mysql.connector
import sys, getopt
import pymysql
import subprocess
from subprocess import PIPE, run
import sys,os
from azure.cli.core import get_default_cli
from flask import Flask, jsonify, request, render_template
import socket, os, json, sys
import requests
import random, os
from azure.common.client_factory import get_client_from_cli_profile
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.web import WebSiteManagementClient
import subprocess

#Use the get_client_from_auth_file method to create the client object:
from azure.common.client_factory import get_client_from_auth_file
from azure.mgmt.resource import SubscriptionClient
import sys, yaml
from flask import send_file, send_from_directory, safe_join, abort, Response


######## New libs added
import pyodbc
import struct
import adal
from msrestazure.azure_active_directory import AADTokenCredentials

import smtplib,ssl
import socket
from smtplib import SMTP_SSL
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path
app = Flask(__name__)

@app.route("/")
def index():    
    return render_template("index.html")

@app.route("/managevm")
def managevm() :
    vmname = request.args.get("vmname")
    action = request.args.get("action")
    cmd = "bash azure_manage_vm1.sh "+vmname+" "+action
    print (cmd)
    ansibleOut = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    ansibleOutput = ansibleOut.stdout.read()
    print (ansibleOutput)
    return str(ansibleOutput)


if __name__ == '__main__':
    app.run(debug=True)
        