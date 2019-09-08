from app import app
import os
import sys
import json
import threading
import time

from flask import Flask, render_template, request, redirect, url_for

@app.route("/login")
@app.route("/admin/login")
def main():
    return render_template('login.html')

@app.route("/")
def landing():
    return render_template('landingTasker.html')

@app.route("/landingEco")
def landingEco():
    return render_template('landingEco.html')
