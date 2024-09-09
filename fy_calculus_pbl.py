import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
from tkinter import ttk

# Define the main window
root = tk.Tk()
root.title("Reaction Order GUI")
root.geometry("600x400")
root.configure(background="MediumPurple1")




# Define the labels and entry fields
lbl_order = tk.Label(root, text="Reaction order:",font='times 20 bold')
lbl_order.grid(row=0, column=0,ipadx=12,ipady=10,padx=5,pady=5)
entry_order = tk.Entry(root)
entry_order.grid(row=0, column=1,ipadx=12,ipady=10,pady=5)

lbl_conc0 = tk.Label(root, text="Initial concentration(M):",font='times 20 bold')
lbl_conc0.grid(row=1, column=0,padx=12,ipady=10,ipadx=5,pady=5)
entry_conc0 = tk.Entry(root)
entry_conc0.grid(row=1, column=1,padx=12,ipady=10,ipadx=5,pady=5)

lbl_concf = tk.Label(root, text="Final concentration(M):",font='times 20 bold')
lbl_concf.grid(row=2, column=0,padx=12,ipady=10,ipadx=5,pady=5)
entry_concf = tk.Entry(root)
entry_concf.grid(row=2, column=1,padx=12,ipady=10,ipadx=5,pady=5)

lbl_time = tk.Label(root, text="Reaction time:",font='times 20 bold')
lbl_time.grid(row=3, column=0,padx=12,ipady=10,ipadx=5,pady=5)
entry_time = tk.Entry(root)
entry_time.grid(row=3, column=1,padx=12,ipady=10,ipadx=5,pady=5)

# Define the labels to display the results
lbl_k = tk.Label(root)
lbl_k.grid(row=4, column=0)

lbl_time = tk.Label(root)
lbl_time.grid(row=5, column=0)

lbl_half_life = tk.Label(root)
lbl_half_life.grid(row=6, column=0)

lbl_90 = tk.Label(root)
lbl_90.grid(row=7, column=0)

# Define the function to calculate the concentration at time t
def concentration(t, k, order, conc0):
    if order == 0:
        c = conc0 * np.exp(-k * t)
    elif order == 1:
        c = conc0 / (1 + k * conc0 * t)
    elif order == 2:
        c = conc0 / np.sqrt(1 + k * conc0 * t)
    return c

# Define the function to calculate the rate constant, reaction time, and half-life
def calculate():
    # Get the values from the entry fields
    order = int(entry_order.get())
    conc0 = float(entry_conc0.get())
    concf = float(entry_concf.get())
    time = float(entry_time.get())

    # Calculate the rate constant
    if order == 0:
        k = -np.log(concf / conc0) / time
    elif order == 1:
        k = (conc0 - concf) / (conc0 * concf * time)
    elif order == 2:
        k = (conc0 - concf) / (conc0 * concf * time) ** 2

    # Calculate the reaction time and half-life
    if order == 0:
        t_half = np.log(2) / k
        t_90 = np.log(10) / k
    elif order == 1:
        t_half = np.log(2) / (k * conc0)
        t_90 = np.log(10) / (k * conc0)
    elif order == 2:
        t_half = 1 / (k * conc0) * np.log(2)
        t_90 = 1 / (k * conc0) * np.log(10)

    # Display the results
    lbl_k.config(text="Rate constant: {:.3e}".format(k))
    lbl_time.config(text="Reaction time: {:.2f} s".format(time))
    lbl_half_life.config(text="Half-life: {:.2f} s".format(t_half))
    lbl_90.config(text="Time for 90% completion: {:.2f} s".format(t_90))

    # Generate the plot
    t = np.linspace(0, time, 1000)
    c = concentration(t, k, order, conc0)
    plt.plot(t, c)
    plt.xlabel("Time (s)")
    plt.ylabel("Concentration (M)")
    plt.title("Concentration vs. Time")
    plt.show()

# Define the button to calculate the results
btn_calculate = tk.Button(root, text="Calculate", command=calculate,font='times 20 bold')
btn_calculate.grid(row=4, column=1)

# Run the main loop
root.mainloop()
