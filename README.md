### The news Aggregator Version 2.

A program that collates cyber security news sources run from the CLI.
Relies on Simple_Term_Menu which is currently only linux supported. 

Usage:
Run main.py
 - By outlet 
- Recent News (grabs news from 4 outlets posted in the last 24 hours)
- Archive 
 - When you open a story its ID is copied to your clipboard.
 - To add an article to your archive select add archive ctrl+shift V and paste the ID in.
   -This stores the article in your archive.json which can be accessed later.
 - To remove an article from the archive the process is the same but you select remove archive.

This project basically just scrapes RSS feeds so can be customised to scrape any attom or RSS version 2 feed with the right headings.



**Known issue**
Currently the krebs on security feed is not being parsed because it does not use standardised published date headings. CBA to fix - feel free.
                                       



<img width="1237" height="938" alt="Screenshot from 2025-11-12 00-25-43" src="https://github.com/user-attachments/assets/f1400d26-f446-4da0-9cf8-9c3bbb2dcd96" />



<img width="3377" height="1399" alt="Screenshot from 2025-11-12 00-26-20" src="https://github.com/user-attachments/assets/a7569b63-0235-480d-8009-66e8845ecfea" />



<img width="3377" height="1399" alt="Screenshot from 2025-11-12 00-26-05" src="https://github.com/user-attachments/assets/55a79fdd-036e-4d0b-86b7-a342d417705a" />
