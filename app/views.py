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

@app.route("/catalogue")
def catalogue():
    return render_template('catalogue.html')


@app.route("/plans")
def plans():
    return render_template('plans.html')
