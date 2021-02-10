# coding: utf-8
"""
This is a quick importer for the wifu demo commands in python.
Easy to load into ipython/jupyter for ad-hoc analysis - %load queries.py

"""
import os
import sqlite3
from sqlite3 import Error

# change this to whatever your wifu file is
conn = sqlite3.connect('wifu.sqlite')

# test function
def test_connection(db_file):
        """ create a database connection to a SQLite database """
            conn = None
try:
        conn = sqlite3.connect(db_file)
            print(sqlite3.version)
except Error as e:
        print(e)

# Example queries
def client_frequency(c):
    cur = c.execute('SELECT client_mac, hostname, number_of_times_seen, seen_first_time, seen_last_time FROM clients ORDER BY number_of_times_seen DESC;')
    return [row for row in cur]
    
def client_distance(c):
    cur = c.execute('SELECT client_mac, max_metres_between_locations, number_of_times_seen, seen_first_time, seen_last_time FROM clients ORDER BY CAST(max_metres_between_locations AS INT) DESC;')
    return [row for row in cur]
    
def most_clients(c):
    cur = c.execute('SELECT N.essid AS [Network Name], N.network_bssid AS [Network BSSID], COUNT(*) AS [Number of Clients] from network_clients NC INNER JOIN networks N ON N.network_bssid = NC.network_bssid GROUP BY N.network_bssid ORDER BY COUNT(*) DESC;')
    return [row for row in cur]
    
def network_name_change(c):
    cur = c.execute('SELECT N.essid AS [Current Network Name], N.network_bssid AS [Network BSSID], COUNT(*) AS [Number of Name Changes] FROM network_essids NE INNER JOIN networks N ON n.network_bssid = NE.network_bssid GROUP BY NE.network_bssid ORDER BY COUNT(*) DESC;')
    return [row for row in cur]
    
def ap_encryption(c):
    cur = c.execute('SELECT encryption AS [Encryption], COUNT(*) AS [Number of Networks] FROM network_encryptions GROUP BY encryption ORDER BY COUNT(*) DESC;')
    return [row for row in cur]
        
def ap_encryption(c):
    cur = c.execute('SELECT encryption AS [Encryption], COUNT(*) AS [Number of Networks] FROM network_encryptions GROUP BY encryption ORDER BY COUNT(*) DESC;')
    return [row for row in cur]
        
def most_probed(c):
    cur = c.execute('SELECT ssid AS [Network Name], COUNT(*) AS [Number of Probe Requests] FROM probe_requests GROUP BY ssid ORDER BY COUNT(*) DESC;')
    return [row for row in cur]
        
def common_network_names(c):
    cur = c.execute('SELECT essid AS [Network Name], COUNT(*) AS [Number of Networks] FROM networks GROUP BY essid ORDER BY COUNT(*) DESC;')
    return [row for row in cur]
    
