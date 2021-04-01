#!/bin/bash

export FLASK_APP=manage
flask db upgrade
