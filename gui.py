import userbenchmark
import scrape
import data_integrator
import data_to_db
import tkinter as tk

window=tk.Tk()
window.title('CPU UserBenchMark Scraper')
 
width=50
activebackground='#777777'
activeforeground='#ffffff'
border=0
background='#000000'
foreground='#ffffff'

userbench=tk.Button(window, text='Scrape UserBenchMark', width=width, command=lambda : userbenchmark.scrape(), activebackground=activebackground, activeforeground=activeforeground, bd=border, bg=background, fg=foreground)
userbench.pack()

amazon=tk.Button(window, text='Scrape Amazon', width=width, command=lambda : scrape.Amazon(), activebackground=activebackground, activeforeground=activeforeground, bd=border, bg=background, fg=foreground)
amazon.pack()

mdcomp=tk.Button(window, text='Scrape MDComputers', width=width, command=lambda : scrape.MDComputers(), activebackground=activebackground, activeforeground=activeforeground, bd=border, bg=background, fg=foreground)
mdcomp.pack()

gnc=tk.Button(window, text='Scrape GamesNComps', width=width, command=lambda : scrape.GamesNComps(), activebackground=activebackground, activeforeground=activeforeground, bd=border, bg=background, fg=foreground)
gnc.pack()

pabgb=tk.Button(window, text='Scrape PrimeABGB', width=width, command=lambda : scrape.PrimeABGB(), activebackground=activebackground, activeforeground=activeforeground, bd=border, bg=background, fg=foreground)
pabgb.pack()

tanotis=tk.Button(window, text='Scrape Tanotis', width=width, command=lambda : scrape.Tanotis(), activebackground=activebackground, activeforeground=activeforeground, bd=border, bg=background, fg=foreground)
tanotis.pack()

dataint=tk.Button(window, text='Integrate Data', width=width, command=lambda : data_integrator.integrate(), activebackground=activebackground, activeforeground=activeforeground, bd=border, bg=background, fg=foreground)
dataint.pack()

datatodb=tk.Button(window, text='Add Data to Database', width=width, command=lambda : data_to_db.add_data(), activebackground=activebackground, activeforeground=activeforeground, bd=border, bg=background, fg=foreground)
datatodb.pack()

window.mainloop()
