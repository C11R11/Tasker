from app import app
from app.TaskRepo import TaskRepo
from app.TaskJob import TaskJob
from app.TaskCaller import TaskCaller

import os
import sys
import json
import threading
import time

from flask import Flask, render_template, request, redirect, url_for

@app.route("/")
@app.route("/admin/login")
def main():
    return render_template('login.html')
