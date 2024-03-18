# Ticket_Management_App

A ticket management app created for my university software engineering and agile module.

## Functionality

This applications intended purpose is to serve as a tool for users to raise issues with their devices. Allowing administrators to assign them selves these tickets to work on.

## Installation/ Requirements

This app was built and tested on a Windows Subsystem for Linux machine running Ubuntu 22.04.

To use this app locally the following are required.

- Python3
- Django 5.0.2
- Installing the requirements.txt using pip
- PostgreSQL 14.11

## Usage

To start the web app run the following command from the root directory of the project `python3 manage.py runserver`.

## Features

This apps functionality has been split out into different directories, here is an explanation of each.

### admin

The admin directory stores the code for the following functionality.

- Users to request to be an admin.
- Admins to reject users administration privilege requests.
- Admins to reject users administration privilege requests.
- Unit test for a selection of the view functions.

### devices

The devices directory stores the code for the following functionality.

- Users and admins to view all devices.
- Admins to create, update and delete devices.
- Unit test for a selection of the view functions.

### tickets

The tickets directory stores the code for the following functionality.

- Users and admins to view all tickets.
- Users to view tickets created by them.
- Admins to view tickets assigned to them.
- Admins to view unassigned tickets.
- Users to create and update tickets.
- Admins to update, resolve and delete tickets.

### users

The tickets directory stores the code for the following functionality.

- Users and admins to log in.
- Users to sign up.
- Users to request admin access upon signup.

### ticket_app

This is the main django app folder containing the majority of the application configuration, some specifics are below.

- Custom admin_required decorator.
- Database configuration.
- Static CSS files for the application.

### templates

The templates directory stores the code for the following functionality.

- Base HTML template.

## Testing

The app contains a variety of unit tests on the devices, tickets and admin functionality. Note that not all view functions are covered by unit tests. Prior to each merge manual testing of all new features was completed.

## Deployment

The app is deployed on a heroku server.
