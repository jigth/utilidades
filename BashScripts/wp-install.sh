#!/usr/bin/bash

# General variables
DOWNLOAD_NAME=wordpress
CONFIG_FILE=wp-config.php

# Get user details to be used in database
read -p "Please enter the name of your application: " APPNAME
read -p "Please enter your Username: " USERNAME
read -p "Please enter your Database Name: " DBNAME
read -s -p "Please enter your Database Password: " DBPWD


# Get current version of wordpress from official page and extract it!
echo "======================================== Downloading wordpress... ========================================"
wget https://wordpress.org/latest.tar.gz
tar -xzf latest.tar.gz && rm latest.tar.gz


# Rename it and create wp-config.php
echo "======================================== Configuring wordpress instalation... ========================================"
mv $DOWNLOAD_NAME $APPNAME
cd $APPNAME
cp wp-config-sample.php wp-config.php


# Configure wp-config.php with provided data
SED_ROUTE=$(which sed)
echo $SED_ROUTE

if [ -z $SED_ROUTE ]
	then
		echo "'sed' is not installed in your machine, please install it to execute this script correctly"
	else
		sed -i "s/username_here/$USERNAME/g" "$CONFIG_FILE"
		sed -i "s/database_name_here/$DBNAME/g" "$CONFIG_FILE"
		sed -i "s/password_here/$DBPWD/g" "$CONFIG_FILE"
fi


echo "TODO: Add the salt here!!"
echo "TODO: Configure correct permissions for apache here!! (Security)"

echo "======================================== Done :D ========================================"