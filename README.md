# Project Readme

This readme file provides step-by-step instructions to set up and run two different projects that involve MySQL, Python, and the Streamlit and mysql-connector libraries. Please follow the instructions below carefully for each project.

## Project 1: Streamlit Application with MySQL

### Prerequisites
1. **Download and Configure MySQL:**
   - Download MySQL from [MySQL Downloads](https://dev.mysql.com/downloads/).
   - Follow the installation instructions for your specific operating system.
   - Configure MySQL with a user account and a database for your project.

2. **Python Setup:**
   - Download and install Python from the [official Python website](https://www.python.org/downloads/).
   - Ensure Python is properly added to your system's PATH.

### Project Setup
3. **Install Streamlit Library:**
   - Open your terminal or command prompt.
   - Run the following command to install Streamlit:
     ```
     pip install streamlit
     ```

4. **Install mysql-connector Library:**
   - Run the following command to install the mysql-connector-python library:
     ```
     pip install mysql-connector-python
     ```

5. **Download the Source Code:**
   - Clone or download the source code for **eBike_with_streamlit** from the project's repository.
   - [Download from here](https://github.com/Tirthraj1605/Simple_eBike_DBMS_SQL)

6. **Configuring Code and schema:**
   - Set your mysql password and username in database.py file.
   - Create a database called 'e_bike' in your mysql.
    ```
    create database if not exists e_bike;
    ```

7. **Run the Streamlit Application:**
   - Navigate to the project directory in your terminal.
   - Run the following command to start the Streamlit application:
     ```
     streamlit run app.py
     ```
   - Access the application in your web browser at the specified URL.

## Project 2: Python Application with MySQL

### Prerequisites
1. **Download and Configure MySQL:**
   - Ensure MySQL is already downloaded and configured as per the above instructions.

2. **Python Setup:**
   - Make sure Python is installed and configured as per Project 1 instructions.

### Project Setup
3. **Install mysql-connector Library:**
   - If not already installed from Project 1, run the following command to install the mysql-connector-python library:
     ```
     pip install mysql-connector-python
     ```

4. **Download the Source Code:**
   - Clone or download the source code for **Simple_eBike** from the project's repository.
   - [Download from here](https://github.com/Tirthraj1605/Simple_eBike_DBMS_SQL)

5. **Configuring Code and schema:**
   - Set your mysql password and username in database.py file.
   - Create a database called 'e_bike' in your mysql.
    ```
    create database if not exists e_bike;
    ```
6. **Run the Python Application:**
   - Navigate to the project directory in your terminal.
   - Run the following command to start the Python application:
     ```
     python app.py
     ```
   - Follow the application's instructions to interact with it.

That's it! You have successfully set up and configured both projects involving MySQL, Python, and the Streamlit and mysql-connector libraries. Happy coding!
