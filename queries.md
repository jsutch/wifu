Wifu was created to better understand wireless networks and traffic and is helpful in answering the following questions:  

- What are the most common network names?  
`SELECT essid AS [Network Name], COUNT(*) AS [Number of Networks] FROM networks GROUP BY essid ORDER BY COUNT(*) DESC`

- What are the networks most probed for by clients?  
`SELECT ssid AS [Network Name], COUNT(*) AS [Number of Probe Requests] FROM probe_requests GROUP BY ssid ORDER BY COUNT(*) DESC`

- What is most common access point encryption used? How prevalent is WEP?  
`SELECT encryption AS [Encryption], COUNT(*) AS [Number of Networks] FROM network_encryptions GROUP BY encryption ORDER BY COUNT(*) DESC`

- How many times have you seen the same client?  
`SELECT client_mac, hostname, number_of_times_seen, seen_first_time, seen_last_time FROM clients ORDER BY number_of_times_seen DESC`

- What is the furthest distance apart that you have seen the same client?  
`SELECT client_mac, max_metres_between_locations, number_of_times_seen, seen_first_time, seen_last_time FROM clients ORDER BY CAST(max_metres_between_locations AS INT) DESC`

- What networks have the most clients?  
`SELECT N.essid AS [Network Name], N.network_bssid AS [Network BSSID], COUNT(*) AS [Number of Clients] from network_clients NC INNER JOIN networks N ON N.network_bssid = NC.network_bssid GROUP BY N.network_bssid ORDER BY COUNT(*) DESC`

- How many networks have changed their name?  
`SELECT N.essid AS [Current Network Name], N.network_bssid AS [Network BSSID], COUNT(*) AS [Number of Name Changes] FROM network_essids NE INNER JOIN networks N ON n.network_bssid = NE.network_bssid GROUP BY NE.network_bssid ORDER BY COUNT(*) DESC`

### for ipython/jupyter versions of these queries

You can load queries.py in ipython once you've run the importer to get a set of static functions to return the example queries. This permits multiple database connections per notebook if you want to run comparisons. Check out queries.md for more details.

Run %load queries.py

Check the functions loaded properly  
```
In [122]: whos
Variable               Type           Data/Info
-----------------------------------------------
Error                  type           <class 'sqlite3.Error'>
ap_encryption          function       <function ap_encryption at 0xffff804b1310>
client_distance        function       <function client_distance at 0xffff8059eca0>
client_frequency       function       <function client_frequency at 0xffff805c7790>
common_network_names   function       <function common_network_names at 0xffff81aff430>
create_connection      function       <function create_connection at 0xffff80ade4c0>
most_clients           function       <function most_clients at 0xffff828ea820>
most_probed            function       <function most_probed at 0xffff804b1670>
network_name_change    function       <function network_name_change at 0xffff81b08670>
```

Create a connection with: 
```
conn = sqlite3.connect('wifu.sqlite')
```

Then call the connection in the function:  
e.g.

```
In [120]: most_clients(conn)
Out[120]:
[('doghouse', 'CC:F4:21:52:C1:19', 9),
 (None, '60:38:E0:7B:01:12', 7),
 ('marys-5g', '6C:B0:BC:FA:CA:6E', 5),
 ('I like to dance', '60:38:D1:B2:B0:BB', 3),
 ('doghouse', 'CC:F4:21:52:C1:15', 2),
...
```
or

```
In [121]: ap_encryption(conn)
Out[121]: [('WPA+PSK', 13), ('WPA+AES-CCM', 13), ('WPA+TKIP', 1), ('None', 1)]
```

*Added - 2021 - Jeff Sutch - Collett Park Networks*
